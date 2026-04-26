import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("heart_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Heart Disease Risk Prediction System")

st.write("Please enter patient medical details below:")

# INPUTS (same order as training)

male = st.selectbox("Sex (1 = Male, 0 = Female)", [0, 1])
age = st.number_input("Age")
education = st.selectbox("Education Level (1-4)", [1,2,3,4])
currentSmoker = st.selectbox("Current Smoker (1 = Yes, 0 = No)", [0,1])
cigsPerDay = st.number_input("Cigarettes Per Day")
BPMeds = st.selectbox("On BP Medication (1 = Yes, 0 = No)", [0,1])
prevalentHyp = st.selectbox("Hypertension (1 = Yes, 0 = No)", [0,1])
diabetes = st.selectbox("Diabetes (1 = Yes, 0 = No)", [0,1])
totChol = st.number_input("Total Cholesterol")
sysBP = st.number_input("Systolic BP")
diaBP = st.number_input("Diastolic BP")
BMI = st.number_input("BMI")
heartRate = st.number_input("Heart Rate")
glucose = st.number_input("Glucose Level")

if st.button("Predict Risk"):

    input_data = np.array([[male, age, education, currentSmoker,
                            cigsPerDay, BPMeds,
                            prevalentHyp, diabetes, totChol,
                            sysBP, diaBP, BMI, heartRate, glucose]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("High Risk of Heart Disease in 10 Years")
    else:
        st.success("Low Risk of Heart Disease in 10 Years")
