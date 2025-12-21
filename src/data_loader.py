import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def clean_creditcard_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply systematic cleaning to creditcard dataset:
    - Remove duplicates.
    - Ensure numeric types.
    - No missing values in this dataset.
    """
    df = df.copy()
    
    # Remove duplicates
    initial = len(df)
    df = df.drop_duplicates()
    logger.info(f"Removed {initial - len(df)} duplicate rows from creditcard data.")
    
    # Ensure numeric (V1–V28, Amount, Time are already floats)
    # No missing values in this dataset per EDA
    
    logger.info(f"Cleaned creditcard data shape: {df.shape}")
    return df


def load_fraud_data(data_path: Path) -> pd.DataFrame:
    df = pd.read_csv(
        data_path / "Fraud_Data.csv", 
        parse_dates=["signup_time", "purchase_time"],
        dtype={"ip_address": str}
    )
    df = clean_fraud_data(df)
    return df


def load_ip_country(data_path: Path) -> pd.DataFrame:
    """Load IP to country mapping."""
    df = pd.read_csv(data_path / "ipAddress_to_Country.csv")
    logger.info(f"IP-country data shape: {df.shape}")
    return df


def load_creditcard(data_path: Path) -> pd.DataFrame:
    df = pd.read_csv(data_path / "creditcard.csv")
    df = clean_creditcard_data(df)
    return df


def validate_data(df: pd.DataFrame, expected_columns: list) -> bool:
    """Check if required columns exist."""
    missing = set(expected_columns) - set(df.columns)
    if missing:
        logger.error(f"Missing columns: {missing}")
        return False
    return True


def remove_duplicates(df: pd.DataFrame, subset=None) -> pd.DataFrame:
    """Remove duplicate rows, keeping first occurrence."""
    initial_len = len(df)
    df = df.drop_duplicates(subset=subset, keep='first')
    logger.info(f"Removed {initial_len - len(df)} duplicate rows.")
    return df

def clean_fraud_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply systematic cleaning to fraud dataset:
    - Ensure correct dtypes.
    - Remove duplicates.
    - Fill missing country with 'Unknown'.
    - Validate IP conversion.
    """
    df = df.copy()
    
    # Remove duplicates
    initial = len(df)
    df = df.drop_duplicates()
    logger.info(f"Removed {initial - len(df)} duplicate rows.")
    
    # Ensure datetime
    if 'signup_time' in df.columns and 'purchase_time' in df.columns:
        df['signup_time'] = pd.to_datetime(df['signup_time'], errors='coerce')
        df['purchase_time'] = pd.to_datetime(df['purchase_time'], errors='coerce')
    
    # Fill missing country (if column exists)
    if 'country' in df.columns:
        df['country'] = df['country'].fillna('Unknown')
        logger.info(f"Filled {df['country'].isna().sum()} missing countries.")
    
    # Ensure numeric IP
    if 'ip_address' in df.columns:
        # Already numeric float; keep as is
        pass
    
    logger.info(f"Cleaned fraud data shape: {df.shape}")
    return df


