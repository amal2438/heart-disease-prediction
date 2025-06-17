# heart-disease-prediction
# 🫀 Heart Disease Prediction Using Machine Learning

This project predicts the presence of heart disease using clinical and demographic data from the UCI Heart Disease dataset. It walks through the full ML pipeline: data cleaning, exploratory analysis, model building, evaluation, and visualization.

---

## 📊 Dataset

- **Source**: [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
- **Features**: Age, Sex, Chest Pain Type, Cholesterol, Fasting Blood Sugar, Resting ECG, Max Heart Rate, Exercise Induced Angina, Oldpeak, Slope, Number of Vessels, Thalassemia, etc.
- **Target**: Presence of heart disease (binary: 0 = No disease, 1 = Disease)

---

## 🚀 Workflow Overview

1. **Exploratory Data Analysis (EDA)**
   - Distribution plots (age, sex, target)
   - Correlation matrix and heatmaps

2. **Data Preprocessing**
   - Target conversion (multi → binary)
   - One-hot encoding of categorical variables
   - Handling missing values

3. **Model Training & Evaluation**
   - ✅ Decision Tree Classifier – Accuracy: ~80%
   - ✅ Random Forest Classifier – Accuracy: ~90%
   - ✅ XGBoost Classifier – Accuracy: ~86%
   - Metrics: Accuracy, Precision, Recall, F1-score, Confusion Matrix, ROC-AUC

4. **Hyperparameter Tuning**
   - GridSearchCV for XGBoost using:
     - `max_depth`, `learning_rate`, `n_estimators`

---

## 📈 Results Summary

| Model         | Accuracy | Precision | Recall | F1-score |
|---------------|----------|-----------|--------|----------|
| Decision Tree | 80%      | 76%       | 76%    | 76%      |
| Random Forest | 90%      | 91%       | 91%    | 90%      |
| XGBoost       | 86%      | 84%       | 84%    | 84%      |

---

## 🧠 Feature Importance Highlights

Top predictors of heart disease:
- `thalach` (Max Heart Rate Achieved)
- `oldpeak` (ST depression)
- `cp` (Chest Pain Type)
- `ca` (Number of Major Vessels)
- `thal` (Thalassemia type)

---

## 💻 Run Locally

```bash
streamlit run app/streamlit_app.py
