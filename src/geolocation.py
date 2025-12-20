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
    if "." in ip_str:
        octets = ip_str.split(".")
        if len(octets) != 4:
            raise ValueError(f"Invalid IPv4 address: {ip}")
        return (
            (int(octets[0]) << 24)
            + (int(octets[1]) << 16)
            + (int(octets[2]) << 8)
            + int(octets[3])
        )
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
    fraud_df: pd.DataFrame, ip_country_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge fraud data with country using IP integer ranges.
    Returns all fraud rows, with country = NaN where no match.
    """
    # Convert bounds to integers
    ip_country_df = ip_country_df.copy()
    ip_country_df["lower_int"] = ip_country_df["lower_bound_ip_address"].apply(
        ip_to_int
    )
    ip_country_df["upper_int"] = ip_country_df["upper_bound_ip_address"].apply(
        ip_to_int
    )

    # Sort for merge_asof
    ip_country_df = ip_country_df.sort_values("lower_int")

    # Merge all fraud rows (including invalid IPs)
    merged = pd.merge_asof(
        fraud_df.sort_values("ip_int"),
        ip_country_df[["lower_int", "upper_int", "country"]],
        left_on="ip_int",
        right_on="lower_int",
        direction="backward",
    )

    # Mark country as NaN where IP not within range
    merged["country"] = merged.apply(
        lambda row: (
            row["country"]
            if (row["ip_int"] >= row["lower_int"] and row["ip_int"] <= row["upper_int"])
            else pd.NA
        ),
        axis=1,
    )

    # Drop helper columns
    merged = merged.drop(columns=["lower_int", "upper_int"])

    return merged
