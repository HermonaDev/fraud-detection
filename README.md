# Fraud Detection for E-commerce and Bank Transactions

[![CI Status](https://github.com/HermonaDev/fraud-detection/actions/workflows/unittests.yml/badge.svg)](https://github.com/HermonaDev/fraud-detection/actions)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Project Overview

This project delivers a **production-ready machine learning system** to detect fraudulent transactions for **Adey Innovations Inc.**, addressing critical business challenges in both e-commerce and banking domains. By integrating **geolocation analysis** and **advanced feature engineering**, we built models that achieve an optimal balance between fraud recall (76-80%) and precision (83-98%), directly reducing false positives that harm customer experience.

**Key Features:**
- 🎯 **Dual-Model Solution**: Separate optimized models for e-commerce and credit card fraud
- 🌍 **Geolocation Intelligence**: IP-to-country mapping for geographic risk profiling
- ⚖️ **Imbalance Handling**: SMOTE sampling with stratified validation
- 🔍 **Full Explainability**: SHAP analysis for global and local interpretability
- 🏗️ **Production Ready**: Modular code, CI/CD pipeline, and comprehensive testing

## 📊 Key Results & Performance

| **Dataset** | **Best Model** | **Avg Precision** | **Recall** | **Precision** | **F1-Score** |
|-------------|----------------|-------------------|------------|---------------|--------------|
| E-commerce | Tuned Random Forest | 0.615 | 0.53 | **0.98** | 0.683 |
| Credit Card | Tuned Random Forest | **0.809** | 0.76 | 0.83 | **0.791** |

**Cross-Validation Stability:**
- E-commerce Model: AP = 0.9927 ± 0.0002 (mean ± std)
- Credit Card Model: AP = 0.99996 ± 0.00002 (mean ± std)

## 🚀 Quick Start

### 1. Prerequisites
```bash
git clone https://github.com/HermonaDev/fraud-detection.git
cd fraud-detection
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Installation
```bash
pip install -r requirements.txt
```

### 3. Dataset Setup
Download and place these files in `data/raw/`:
- [`Fraud_Data.csv`](https://www.kaggle.com/datasets/)
- [`ipAddress_to_Country.csv`](https://www.kaggle.com/datasets/)
- [`creditcard.csv`](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

*Note: Due to size and licensing, datasets are not included in this repository.*

### 4. Run the Analysis Pipeline
Execute notebooks in sequential order:

| Notebook | Purpose | Output |
|----------|---------|--------|
| `1_data_validation.ipynb` | Initial data loading and validation | Validated datasets |
| `2_geolocation_integration.ipynb` | IP-to-country mapping | Enriched fraud data |
| `eda-fraud-data.ipynb` | E-commerce data exploration | Key insights and visualizations |
| `eda-creditcard.ipynb` | Credit card data exploration | Imbalance analysis |
| `feature-engineering.ipynb` | Feature creation and preprocessing | Processed datasets |
| `modeling.ipynb` | Model training, tuning, and evaluation | Trained models and performance metrics |
| `shap-explainability.ipynb` | Model interpretability analysis | SHAP plots and business insights |

## 🏗️ Project Architecture

```
fraud-detection/
├── data/                   # Data directory
│   ├── raw/               # Original datasets (gitignored)
│   └── processed/         # Cleaned and engineered data
├── notebooks/             # Jupyter notebooks (analysis pipeline)
├── src/                   # Reusable Python modules
│   ├── data_loader.py    # Data loading and validation
│   ├── features.py       # Feature engineering and preprocessing
│   └── geolocation.py    # IP-to-country mapping utilities
├── models/                # Saved model artifacts (gitignored)
├── reports/               # Generated reports and visualizations
├── tests/                 # Unit tests
└── .github/workflows/     # CI/CD configuration
```

## 📈 Key Insights from Analysis

### 🔍 Fraud Patterns Discovered
1. **Temporal Patterns**: Fraud peaks during evening hours (7-10 PM) and on Tuesdays
2. **Behavioral Signals**: >40% of fraud occurs within 48 hours of account creation
3. **Geographic Risks**: Transactions from certain countries show 3x higher fraud rates
4. **Source Vulnerability**: Direct traffic has 18% higher fraud rate than SEO

### 🛡️ Business Recommendations (from SHAP Analysis)
1. **Implement time-based verification** for transactions within 2 hours of signup
2. **Enhance monitoring for Direct traffic sources** during evening hours
3. **Create geo-specific rules** for high-risk countries identified in analysis

## 🔧 Technical Implementation

### Feature Engineering
- **Temporal Features**: `purchase_hour`, `day_of_week`, `time_since_signup_hours`
- **Behavioral Features**: `transactions_last_24h` (velocity tracking)
- **Geographic Features**: Country encoding with "Unknown" category
- **Demographic Features**: Age, source, browser encoding

### Model Development
- **Baseline**: Logistic Regression for interpretability
- **Ensemble Models**: Random Forest and XGBoost with hyperparameter tuning
- **Validation**: 5-fold stratified cross-validation
- **Selection Criteria**: Average Precision + business-aligned precision/recall tradeoff

## 📚 Additional Resources

- **Final Report**: [Download PDF](reports/final_report.pdf) - Comprehensive project narrative
- **Presentation**: [View Slides](reports/presentation.pptx) - Stakeholder summary
- **API Documentation**: [View Docs](src/README.md) - Module reference

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- Dataset providers: Kaggle IEEE-CIS Fraud Detection and Credit Card Fraud Detection
- Tools: Scikit-learn, XGBoost, SHAP, Pandas, Jupyter
- Mentorship: 10 Academy AI Mastery Program
