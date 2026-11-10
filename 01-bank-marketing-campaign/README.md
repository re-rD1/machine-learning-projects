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
9. Deployment prototype using Streamlit

## Modeling

The project compares multiple classification algorithms, including Logistic Regression, K-Nearest Neighbors, Decision Tree, ensemble methods, and boosting models.

The final model selected during validation was **Gradient Boosting**, using a decision threshold of **0.40**. The selection was based on validation F1-score.

## Evaluation

The final reported test-set results for the selected Gradient Boosting model were:

| Metric | Result |
|---|---:|
| Accuracy | 0.6688 |
| Precision | 0.6300 |
| Recall | 0.7440 |
| F1-score | 0.6822 |
| ROC AUC | 0.7402 |

**Evaluation note:** The test set had also been used in earlier experiments with a different feature configuration. Therefore, these results should not be interpreted as coming from a completely untouched independent holdout.

## Tools & Technologies

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- SHAP
- Streamlit
- Joblib

## Project Files

Project notebooks, application code, model artifacts, and setup instructions will be added to this folder as they are prepared for publication.

## Key Takeaway

This project demonstrates an end-to-end machine learning workflow, from defining a business problem and preparing data to comparing classification models, interpreting model behavior, and preparing a deployment prototype.

---

*This project was developed as part of my Data Science learning journey at Purwadhika Digital Technology School.*
