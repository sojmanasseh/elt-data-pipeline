import pandas as pd
import numpy as np


def load_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)


def sanitize_financials(series: pd.Series) -> pd.Series:
    """
    Extracts numeric values from alphanumeric currency strings.
    Forces unparseable anomalies to NaN for standardized downstream handling.
    """
    # Regex strips everything except digits, negative signs, and decimals
    cleaned = series.astype(str).str.replace(r'[^\d.-]', '', regex=True)
    # Coerce double-decimals (e.g., '750..00') or extreme noise to NaN
    return pd.to_numeric(cleaned, errors='coerce')


def standardize_temporal_data(series: pd.Series) -> pd.Series:
    """
    Parses heterogeneous date formats into standard datetime64[ns].
    """
    return pd.to_datetime(series, errors='coerce')


def normalize_text_vectors(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Executes vectorized string normalization (strip whitespace, lowercase).
    """
    for col in columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()
            # Restore np.nan that get cast to string 'nan'
            df[col] = df[col].replace('nan', np.nan)
    return df


def resolve_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """
    Executes domain-specific imputation and critical-path dropping.
    """
    # Drop rows missing critical analytical vectors
    df = df.dropna(subset=['transaction_id', 'purchase_date', 'revenue'])

    # Impute categorical nulls
    df['status'] = df['status'].fillna('unknown')
    df['customer_email'] = df['customer_email'].fillna('missing_email@system.local')

    return df


def execute_etl_pipeline(input_path: str, output_path: str):
    print(f"[System] Initiating ETL pipeline on {input_path}...")
    df = load_data(input_path)

    # 1. Type Coercion & Extraction
    df['revenue'] = sanitize_financials(df['revenue'])
    df['purchase_date'] = standardize_temporal_data(df['purchase_date'])

    # 2. Text Normalization
    df = normalize_text_vectors(df, ['customer_email', 'status'])

    # 3. Null Handling
    df = resolve_nulls(df)

    # Export sanitized payload
    df.to_csv(output_path, index=False)
    print(f"[System] Pipeline complete. Clean dataset exported to: {output_path}")
    return df


if __name__ == "__main__":
    execute_etl_pipeline("raw_transactions.csv", "clean_transactions.csv")