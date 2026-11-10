# Bank Marketing Campaign Prediction

## Project Overview

This project develops a machine learning classification model to predict whether a bank customer will subscribe to a term deposit, using customer profile information and previous campaign history available before a new marketing campaign.

The goal is to support more informed campaign planning by helping identify customers who are more likely to subscribe.

## Problem Statement

Bank marketing campaigns involve contacting potential customers, but not every customer will subscribe to the offered term deposit. A predictive model can help the bank prioritize its outreach efforts.

**Target variable:** `deposit` (Yes / No)

## Workflow

1. Business understanding and problem definition
2. Data understanding and exploratory data analysis
3. Data cleaning and preprocessing
4. Feature engineering and feature selection
5. Model training and comparison
6. Hyperparameter tuning
7. Model evaluation and threshold selection
8. Model interpretation
9. Model persistence and Streamlit deployment prototype

## Final Model

The project compares multiple classification algorithms, including Logistic Regression, K-Nearest Neighbors, Decision Tree, ensemble methods, and boosting models.

The final model selected during validation was **Gradient Boosting**, using a decision threshold of **0.40**. The selection was based on validation F1-score.

## Evaluation Results

| Metric | Result |
|---|---:|
| Accuracy | 0.6688 |
| Precision | 0.6300 |
| Recall | 0.7440 |
| F1-score | 0.6822 |
| ROC AUC | 0.7402 |

**Evaluation limitation:** The test set had also been used in earlier experiments with a different feature configuration. Therefore, these results should not be interpreted as coming from a completely untouched independent holdout.

## Project Files

- `BankMarketingCamp_Caps3_RayhanAkmal.ipynb` — analysis, feature engineering, model comparison, tuning, evaluation, and model saving.
- `deployment.py` — Streamlit prediction interface.
- `bank_marketing_model.joblib` — saved model pipeline, decision threshold, and feature list.
- `requirements.txt` — Python dependencies.

## Run the Streamlit App

1. Clone or download this repository.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure `deployment.py` and `bank_marketing_model.joblib` are in the same project folder.
4. Run:

   ```bash
   streamlit run deployment.py
   ```

The app accepts customer profile and previous campaign information, derives `age_group` and `previously_contacted`, and displays the predicted subscription probability and classification using the saved threshold.

## Dataset

The dataset is not included in this repository. Add the original dataset source and access instructions here before reproducing the notebook. The notebook expects the CSV file to be named `data_bank_marketing_campaign.csv` in its working directory.

## Tools & Technologies

- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn, XGBoost
- SHAP
- Streamlit, Joblib

## Notes

- The saved model was serialized with scikit-learn **1.9.1**. Use the version specified in `requirements.txt` when loading the artifact.
- This is a portfolio/learning project and a prototype, not a validated production banking decision system.
- Model predictions indicate estimated likelihoods and should not be interpreted as causal conclusions.

---

*Developed as part of my Data Science learning journey at Purwadhika Digital Technology School.*
