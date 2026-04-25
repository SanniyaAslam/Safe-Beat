# Safe-Beat
# SafeBeat — Heart Disease Risk Prediction System

A machine learning web application that predicts a patient's 10-year risk 
of developing coronary heart disease based on their medical information.

## Project Overview

SafeBeat takes 14 medical inputs from a patient and uses a trained 
Logistic Regression model to predict whether they are at high risk or 
low risk of heart disease in the next 10 years.

## Group Members

- Sanniya Aslam
- Fatima Habib  
- Khadija Bilal

## Dataset

Framingham Heart Study Dataset — a publicly available medical dataset 
with records of over 4000 patients.

## Features Used

male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentHyp, 
diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose

## Model

- Algorithm: Logistic Regression
- Library: scikit-learn
- class_weight: balanced (to handle class imbalance)
- Feature Scaling: StandardScaler

## Results

| Metric    | Value  |
|-----------|--------|
| Accuracy  | 66.86% |
| Precision | 25.16% |
| Recall    | 59.69% |
| F1-Score  | 35.40% |

## Project Files

| File | Description |
|------|-------------|
| training.ipynb | Model training and evaluation notebook |
| app.py | Streamlit web application |
| heart_model.pkl | Trained model |
| scaler.pkl | Fitted StandardScaler |
| framingham.csv | Dataset |

## How to Run

1. Install dependencies:
pip install streamlit scikit-learn numpy pandas

2. Run the app:
python -m streamlit run app.py

3. Enter patient details in the form and click Predict Risk

## Tech Stack

Python, scikit-learn, Streamlit, pandas, numpy, Google Colab
