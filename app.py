import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# Streamlit UI
st.title("Loan Status Prediction")
st.write("Enter details to check if your loan will be approved.")

# User input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income", min_value=0, step=500)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0, step=500)
loan_amount = st.number_input("Loan Amount ", min_value=0, step=10)
loan_term = st.selectbox("Loan Term ", [360])
credit_history = st.selectbox("Credit History (1: Good, 0: Bad)", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Convert categorical values to match model input
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
dependents = 3 if dependents == "3+" else int(dependents)
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
property_mapping = {"Urban": 2, "Semiurban": 1, "Rural": 0}
property_area = property_mapping[property_area]

# Prepare input for the model (only 8 features)
user_input = np.array([[gender, married, dependents, education, self_employed, 
                        applicant_income, coapplicant_income, loan_amount]])

# Predict on button click
if st.button("Predict Loan Status"):
    prediction = model.predict(user_input)
    loan_status = "Approved (Y)" if prediction[0] == "Y" else "Rejected (N)"
    st.success(f"Loan Status: **{loan_status}**")
