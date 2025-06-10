import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('heart_disease_model.pkl')

# App title
st.title("💓 Heart Disease Prediction App")

st.markdown("Enter the patient's data below:")

# User input
age = st.slider("Age", 20, 100, 50)
sex = st.selectbox("Sex", ("Female", "Male"))
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.slider("Resting Blood Pressure", 80, 200, 120)
chol = st.slider("Serum Cholesterol (mg/dl)", 100, 600, 240)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ("False", "True"))
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.slider("Max Heart Rate Achieved", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina", ("No", "Yes"))
oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2])
ca = st.selectbox("No. of Major Vessels (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", [0, 1, 2])

# Convert inputs
sex = 1 if sex == "Male" else 0
fbs = 1 if fbs == "True" else 0
exang = 1 if exang == "Yes" else 0

# Create input array
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope, ca, thal]])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High risk of heart disease. Please consult a doctor.")
    else:
        st.success("✅ No major signs of heart disease.")
