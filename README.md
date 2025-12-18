# Fraud Detection for E-commerce and Bank Transactions

## Project Overview
Improve detection of fraud cases using machine learning and geolocation analysis.

## Structure
- `data/raw/`: original datasets (ignored in Git)
- `data/processed/`: cleaned and feature-engineered data
- `notebooks/`: exploratory analysis, modeling, explainability
- `src/`: reusable Python modules
- `tests/`: unit tests
- `models/`: saved model artifacts

## Setup
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Place datasets in `data/raw/`:
   - `Fraud_Data.csv`
   - `ipAddress_to_Country.csv`
   - `creditcard.csv`

## Usage
Run notebooks in order:
1. `eda-fraud-data.ipynb`
2. `eda-creditcard.ipynb`
3. `feature-engineering.ipynb`
4. `modeling.ipynb`
5. `shap-explainability.ipynb`