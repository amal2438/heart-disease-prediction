🫀 Heart Disease Prediction Using Machine Learning
This project aims to predict the presence of heart disease using clinical and demographic data from the UCI Heart Disease dataset. It walks through the full machine learning workflow including data cleaning, exploratory data analysis (EDA), model building, evaluation, and feature importance analysis.

📊 Dataset
Source: UCI Machine Learning Repository – Heart Disease Dataset

Attributes: Age, Sex, Chest Pain Type, Cholesterol, Fasting Blood Sugar, Resting ECG, Max Heart Rate, Exercise Induced Angina, Oldpeak, Slope, Number of Vessels, Thalassemia, etc.

Target: Presence of heart disease (converted to binary: 0 = No disease, 1 = Disease)

🚀 Workflow Overview
1. Exploratory Data Analysis (EDA)
Distribution plots of age, sex, and disease prevalence

Correlation analysis

Feature-wise visual inspection

2. Data Preprocessing
Binary encoding of target values

One-hot encoding of categorical variables

Handling missing values

3. Model Training & Evaluation
✅ Models Used:
Decision Tree Classifier

Accuracy: ~80%

Random Forest Classifier

Accuracy: ~90%

XGBoost Classifier

Accuracy: ~86%

AUC ROC and feature importance plotted

📊 Evaluation Metrics:
Accuracy, Precision, Recall, F1-score

Confusion Matrix

ROC-AUC Curve

Feature Importance

4. Hyperparameter Tuning
Applied GridSearchCV for XGBoost with parameters:

max_depth, learning_rate, n_estimators

📈 Results Summary
Model	Accuracy	Precision	Recall	F1-score
Decision Tree	80%	76%	76%	76%
Random Forest	90%	91%	91%	90%
XGBoost	86%	84%	84%	84%

🧠 Feature Importance Highlights
Top predictors of heart disease:

thalach (Max Heart Rate Achieved)

oldpeak (ST depression)

cp (Chest Pain Type)

ca (Number of Major Vessels)

thal (Thalassemia type)