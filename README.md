# Fraud Detection for E‑Commerce & Bank Transactions

## Overview
This project builds machine‑learning models to detect fraudulent transactions in e‑commerce and credit card datasets. It includes geolocation integration, feature engineering, handling severe class imbalance, and model explainability (SHAP).

## Repository Structure
fraud‑detection/
├── data/raw/ # Original datasets (not in git)
├── data/processed/ # Cleaned & feature‑engineered data
├── notebooks/ # Jupyter notebooks (EDA → modeling → SHAP)
├── src/ # Reusable Python modules
├── models/ # Saved model artifacts (not in git)
├── tests/ # Unit tests
└── .github/workflows/ # CI pipeline


## Setup
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Place the three datasets (`Fraud_Data.csv`, `ipAddress_to_Country.csv`, `creditcard.csv`) in `data/raw/`.
4. Run notebooks in order:
   - `eda-fraud-data.ipynb`
   - `eda-creditcard.ipynb`
   - `feature-engineering.ipynb`
   - `modeling.ipynb`
   - `shap-explainability.ipynb`

## Model Artifacts
Trained models are saved locally in `models/` after running `modeling.ipynb`. They are excluded from git via `.gitignore`.

## CI/CD
GitHub Actions runs linting (`black`, `flake8`) and unit tests on every push.