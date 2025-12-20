import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def load_fraud_data(data_path: Path) -> pd.DataFrame:
    """Load e-commerce fraud dataset."""
    df = pd.read_csv(
        data_path / "Fraud_Data.csv",
        parse_dates=["signup_time", "purchase_time"],
        dtype={"ip_address": str},
    )
    logger.info(f"Fraud data shape: {df.shape}")
    return df


def load_ip_country(data_path: Path) -> pd.DataFrame:
    """Load IP to country mapping."""
    df = pd.read_csv(data_path / "ipAddress_to_Country.csv")
    logger.info(f"IP-country data shape: {df.shape}")
    return df


def load_creditcard(data_path: Path) -> pd.DataFrame:
    """Load credit card fraud dataset."""
    df = pd.read_csv(data_path / "creditcard.csv")
    logger.info(f"Creditcard data shape: {df.shape}")
    return df


def validate_data(df: pd.DataFrame, expected_columns: list) -> bool:
    """Check if required columns exist."""
    missing = set(expected_columns) - set(df.columns)
    if missing:
        logger.error(f"Missing columns: {missing}")
        return False
    return True

