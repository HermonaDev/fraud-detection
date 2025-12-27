import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import logging
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

logger = logging.getLogger(__name__)


def add_time_features_fraud(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add time-based features for e-commerce fraud data.
    Assumes columns: 'signup_time', 'purchase_time'.
    """
    df = df.copy()
    # Already added in EDA, but ensure they exist
    if 'purchase_hour' not in df.columns:
        df['purchase_hour'] = df['purchase_time'].dt.hour
    if 'purchase_dayofweek' not in df.columns:
        df['purchase_dayofweek'] = df['purchase_time'].dt.dayofweek
    if 'time_since_signup_hours' not in df.columns:
        df['time_since_signup_hours'] = (
            (df['purchase_time'] - df['signup_time']).dt.total_seconds() / 3600
        )
    # Transaction velocity: number of purchases per user in last 24h window
    # This is simplified; for production you'd need a rolling window per user
    df['transactions_last_24h'] = df.groupby('user_id')['purchase_time'].transform(
        lambda x: x.rolling('24h', closed='left').count()
    ).fillna(0)

    logger.info("Added time features for fraud data.")
    return df


def add_time_features_creditcard(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add time-based features for creditcard data.
    'Time' is seconds since first transaction.
    """
    df = df.copy()
    # Convert to hour of day (assuming Time is in seconds)
    df['hour_of_day'] = (df['Time'] // 3600) % 24
    # Day of week (assuming data spans multiple days)
    df['day_of_week'] = (df['Time'] // (3600 * 24)) % 7
    logger.info("Added time features for creditcard data.")
    return df


def scale_numeric(
    df: pd.DataFrame,
    numeric_cols: list
) -> (pd.DataFrame, StandardScaler):
    """Scale numeric columns using StandardScaler."""
    df = df.copy()
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    logger.info(f"Scaled numeric columns: {numeric_cols}")
    return df, scaler


def encode_categorical(
    df: pd.DataFrame,
    cat_cols: list
) -> (pd.DataFrame, OneHotEncoder):
    """One-hot encode categorical columns."""
    df = df.copy()
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    encoded = encoder.fit_transform(df[cat_cols])
    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(cat_cols),
        index=df.index
    )
    df = pd.concat([df.drop(columns=cat_cols), encoded_df], axis=1)
    logger.info(f"Encoded categorical columns: {cat_cols}")
    return df, encoder


def resample_smote(X_train, y_train, random_state=42):
    """Apply SMOTE to training data."""
    sm = SMOTE(random_state=random_state)
    X_res, y_res = sm.fit_resample(X_train, y_train)
    logger.info(f"SMOTE applied: {len(y_train)} -> {len(y_res)} samples.")
    return X_res, y_res


def resample_undersample(X_train, y_train, random_state=42):
    """Random undersample majority class."""
    rus = RandomUnderSampler(random_state=random_state)
    X_res, y_res = rus.fit_resample(X_train, y_train)
    logger.info(f"Undersampling applied: {len(y_train)} -> {len(y_res)} samples.")
    return X_res, y_res
