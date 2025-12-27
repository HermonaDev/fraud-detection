- Purpose: store datasets used for model development and evaluation. `raw/` contains original downloads; `processed/` contains cleaned, feature-engineered outputs ready for modeling.

- Original datasets:
  - `Fraud_Data.csv` — e‑commerce fraud transactions (source: project data provider).
  - `ipAddress_to_Country.csv` — IP-to-country mapping (source: geolocation provider).
  - `creditcard.csv` — credit card transactions (source: public dataset).

- Processed files:
  - `fraud_data_processed.csv` — cleaned timestamps, filled missing countries, deduplicated, and added geolocation features.
  - `creditcard_processed.csv` — deduplicated and validated numeric features, time-based features added.

- Note: Raw files are not tracked in Git (see `.gitignore`).