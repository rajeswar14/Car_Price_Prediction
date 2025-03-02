import streamlit as st
import joblib
import numpy as np

# Load trained models
lin_reg = joblib.load("linear_reg_model.pkl")
lasso_reg = joblib.load("lasso_reg_model.pkl")

# Title
st.title("Car Price Prediction App 🚗")

# User Inputs
year = st.number_input("Year of Purchase", min_value=2000, max_value=2025, step=1)
present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, step=0.1)
kms_driven = st.number_input("Kilometers Driven", min_value=0, step=1000)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.number_input("Number of Previous Owners", min_value=0, max_value=3, step=1)

# Encode Categorical Data
fuel_dict = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_dict = {"Dealer": 0, "Individual": 1}
trans_dict = {"Manual": 0, "Automatic": 1}

fuel_type = fuel_dict[fuel_type]
seller_type = seller_dict[seller_type]
transmission = trans_dict[transmission]

# Create Input Array
input_data = np.array([[year, present_price, kms_driven, fuel_type, seller_type, transmission, owner]])

# Prediction Buttons
if st.button("Predict with Linear Regression"):
    price = lin_reg.predict(input_data)
    st.success(f"Predicted Selling Price (Linear Regression): ₹{price[0]:.2f} Lakhs")

if st.button("Predict with Lasso Regression"):
    price = lasso_reg.predict(input_data)
    st.success(f"Predicted Selling Price (Lasso Regression): ₹{price[0]:.2f} Lakhs")