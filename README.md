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


## How to Run the Project

### 1. Environment Setup
```bash
# Clone repository
git clone https://github.com/HermonaDev/fraud-detection.git
cd fraud-detection

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt 
```


### 2. Download Datasets
Place the following files in data/raw/:

Fraud_Data.csv

ipAddress_to_Country.csv

creditcard.csv

(These datasets are not included in the repo due to size and licensing.)

### . Run Notebooks in Order
Execute the Jupyter notebooks sequentially:

1. notebooks/eda-fraud-data.ipynb – Exploratory analysis of e‑commerce fraud data.

2. notebooks/eda-creditcard.ipynb – Exploratory analysis of credit card fraud data.

3. notebooks/feature-engineering.ipynb – Feature engineering and preprocessing.

4. notebooks/modeling.ipynb – Model training, tuning, and evaluation.

5. notebooks/shap-explainability.ipynb – Model explainability with SHAP.

### 4. Relationship Between Notebooks and src/ Modules
The notebooks import reusable functions from src/:

src/data_loader.py – loading and cleaning data.

src/features.py – feature engineering and resampling.

src/geolocation.py – IP‑to‑country mapping.

This separation ensures production‑ready code is kept modular and testable.

### 5. Generated Artifacts
Processed datasets are saved in data/processed/.

Trained models are saved in models/ (excluded from Git via .gitignore).

Figures and reports are saved in reports/figures/.

### 6. Run Tests
bash
pytest tests/ -v
text


## CI/CD
GitHub Actions runs linting (`black`, `flake8`) and unit tests on every push.