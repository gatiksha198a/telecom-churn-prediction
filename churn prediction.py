# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 17:24:08 2026

@author: gatik
"""

import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("C:/Users/gatik/Downloads/churn telecom/churn_model.sav", "rb"))

st.title("📊 Telecom Customer Churn Prediction System")
st.write("Enter customer details to predict churn")

# -------- User Inputs --------
gender = st.selectbox("Gender", ["Female", "Male"])
SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])
Partner = st.selectbox("Partner", ["No", "Yes"])
Dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.number_input("Tenure (months)", 0, 72, 12)

PhoneService = st.selectbox("Phone Service", ["No", "Yes"])
MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])

InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
OnlineBackup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
DeviceProtection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
TechSupport = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
StreamingTV = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.selectbox("Paperless Billing", ["No", "Yes"])
PaymentMethod = st.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])

MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 800.0)

# -------- Encoding (must match training) --------
binary_map = {"No": 0, "Yes": 1}
gender_map = {"Female": 0, "Male": 1}
internet_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
three_map = {"No": 0, "Yes": 1, "No internet service": 2}
multi_map = {"No": 0, "Yes": 1, "No phone service": 2}
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
payment_map = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer (automatic)": 2,
    "Credit card (automatic)": 3
}

gender = gender_map[gender]
SeniorCitizen = binary_map[SeniorCitizen]
Partner = binary_map[Partner]
Dependents = binary_map[Dependents]
PhoneService = binary_map[PhoneService]
PaperlessBilling = binary_map[PaperlessBilling]

MultipleLines = multi_map[MultipleLines]
InternetService = internet_map[InternetService]
OnlineSecurity = three_map[OnlineSecurity]
OnlineBackup = three_map[OnlineBackup]
DeviceProtection = three_map[DeviceProtection]
TechSupport = three_map[TechSupport]
StreamingTV = three_map[StreamingTV]
StreamingMovies = three_map[StreamingMovies]

Contract = contract_map[Contract]
PaymentMethod = payment_map[PaymentMethod]

# -------- Prediction --------
if st.button("Predict Churn"):
    input_data = np.array([[gender, SeniorCitizen, Partner, Dependents,
                            tenure, PhoneService, MultipleLines,
                            InternetService, OnlineSecurity, OnlineBackup,
                            DeviceProtection, TechSupport, StreamingTV,
                            StreamingMovies, Contract, PaperlessBilling,
                            PaymentMethod, MonthlyCharges, TotalCharges]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("❌ Customer is likely to CHURN")
    else:
        st.success("✅ Customer is likely to STAY")
