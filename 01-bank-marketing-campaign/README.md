# Bank Marketing Campaign Prediction

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-1.9.1-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)
![Model](https://img.shields.io/badge/Model-Gradient%20Boosting-success)

## Project Overview

This project develops a machine learning classification model to predict whether a bank customer will subscribe to a term deposit, using customer profile information and previous campaign history available before a new marketing campaign.

The goal is to support more informed campaign planning by helping identify customers who are more likely to subscribe.

## Problem Statement

Bank marketing campaigns involve contacting potential customers, but not every customer will subscribe to the offered term deposit. A predictive model can help the bank prioritize its outreach efforts.

**Target variable:** `deposit` (Yes / No)

## Features & Input Attributes

The final model uses **9 features**. The Streamlit app asks users to enter 7 customer/history attributes and automatically derives the remaining 2 features.

| Feature | Description | App input |
|---|---|---|
| `age` | Customer's age in years | Manual input |
| `job` | Customer's occupation category | Manual selection |
| `balance` | Customer's account balance | Manual input |
| `housing` | Whether the customer has a housing loan (`yes`/`no`) | Manual selection |
| `loan` | Whether the customer has a personal loan (`yes`/`no`) | Manual selection |
| `pdays` | Days since the customer was last contacted in a previous campaign; `-1` means no previous contact | Manual input |
| `poutcome` | Outcome of the previous marketing campaign | Manual selection |
| `age_group` | Age category derived automatically from `age` | Automatically generated |
| `previously_contacted` | Indicates previous contact: `no` when `pdays = -1`, otherwise `yes` | Automatically generated |

**Age group categories:** Young Adult, Adult, Middle Adult, Mature Adult, Senior, and Elderly.

The target variable `deposit` is used for model training and evaluation; it is not an input feature in the prediction app.

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

## Streamlit App Features

- Enter customer profile and previous campaign information through an interactive form.
- Automatically generate `age_group` and `previously_contacted`.
- Display the estimated subscription probability.
- Apply the saved decision threshold of **0.40** to produce a Yes/No prediction.
- Show the model threshold and number of input features.

## Presentation

- **Presentation slides:** [View or download the Bank Marketing Campaign presentation (PPTX)](./PPT%20Bank%20Marketing%20Campaign.pptx).
- **Presentation video:** [Watch the project presentation on YouTube](https://youtu.be/9kcfu-9PJ3Y).

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

The dataset is included in this project folder as `data_bank_marketing_campaign.csv`. The notebook expects this filename in its working directory.

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
