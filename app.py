import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load('heart_disease_model.pkl')

st.title("Heart Disease Risk Predictor")
st.write("Enter patient details to assess risk of heart disease.")

# Input fields
age = st.number_input("Age", min_value=20, max_value=100, value=50)
trestbps = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Serum Cholesterol (mg/dL)", value=200)
thalach = st.number_input("Max Heart Rate Achieved", value=150)
oldpeak = st.number_input("ST depression", value=1.0)
ca = st.selectbox("Number of major vessels (0–3)", [0, 1, 2, 3])

cp_typical = st.checkbox("Typical Angina Chest Pain")
sex_male = st.checkbox("Male")
exang_true = st.checkbox("Exercise-Induced Angina")
fbs_true = st.checkbox("Fasting Blood Sugar > 120")

# Build input DataFrame
input_df = pd.DataFrame([{
    'age': age,
    'trestbps': trestbps,
    'chol': chol,
    'thalach': thalach,
    'oldpeak': oldpeak,
    'ca': ca,
    'cp_typical angina': int(cp_typical),
    'sex_Male': int(sex_male),
    'exang_True': int(exang_true),
    'fbs_True': int(fbs_true)
}])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    st.success("Prediction: " + ("Heart Disease" if prediction == 1 else "No Heart Disease"))
    st.info(f"Risk Probability: {probability:.2f}")