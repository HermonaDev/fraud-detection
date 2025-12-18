import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

def ip_to_int(ip) -> int:
    """
    Convert IP (float, int, or dotted string) to integer.
    Handles numeric IPs (like 7.327584e+08) directly.
    """
    if pd.isna(ip):
        return -1  # sentinel for missing
    # If it's numeric (float/int), convert directly
    if isinstance(ip, (int, np.integer, float, np.floating)):
        return int(ip)
    # If it's a string
    ip_str = str(ip)
    if '.' in ip_str:
        octets = ip_str.split('.')
        if len(octets) != 4:
            raise ValueError(f"Invalid IPv4 address: {ip}")
        return (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
    # String without dots (already integer representation)
    try:
        return int(float(ip_str))
    except ValueError:
        return -1

def add_ip_integer(df: pd.DataFrame, ip_col: str = "ip_address") -> pd.DataFrame:
    """Add integer version of IP address column."""
    df = df.copy()
    df["ip_int"] = df[ip_col].apply(ip_to_int)
    return df

def merge_country_by_ip(
    fraud_df: pd.DataFrame,
    ip_country_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge fraud data with country using IP integer ranges.
    Expects ip_country_df columns: lower_bound_ip_address, upper_bound_ip_address, country.
    """
    # Convert bounds to integers
    ip_country_df = ip_country_df.copy()
    ip_country_df["lower_int"] = ip_country_df["lower_bound_ip_address"].apply(ip_to_int)
    ip_country_df["upper_int"] = ip_country_df["upper_bound_ip_address"].apply(ip_to_int)
    
    # Sort for merge_asof
    ip_country_df = ip_country_df.sort_values("lower_int")
    
    # Separate rows with valid IP (non-negative)
    fraud_df_valid = fraud_df[fraud_df["ip_int"] >= 0].copy()
    fraud_df_invalid = fraud_df[fraud_df["ip_int"] < 0].copy()
    
    if not fraud_df_valid.empty:
        merged_valid = pd.merge_asof(
            fraud_df_valid.sort_values("ip_int"),
            ip_country_df[["lower_int", "upper_int", "country"]],
            left_on="ip_int",
            right_on="lower_int",
            direction="backward"
        )
        # Filter where IP falls within range
        merged_valid = merged_valid[
            (merged_valid["ip_int"] >= merged_valid["lower_int"]) & 
            (merged_valid["ip_int"] <= merged_valid["upper_int"])
        ]
        merged_valid = merged_valid.drop(columns=["lower_int", "upper_int"])
    else:
        merged_valid = pd.DataFrame()
    
    # Add null country for invalid IP rows
    fraud_df_invalid["country"] = pd.NA
    
    # Combine
    merged = pd.concat([merged_valid, fraud_df_invalid], ignore_index=True)
    
    return merged