import streamlit as st
import pickle
import numpy as np

# Set the page configuration with the desired font
st.set_page_config(
    page_title="Loan Prediction App",
    page_icon=":money_with_wings:",
    layout="centered",
    initial_sidebar_state="auto",
)


# Load the saved loan prediction model
with open('loan_prediction_model.pkl', 'rb') as file:
    classifier = pickle.load(file)

def predict_loan_approval(inputs):
# Convert the dictionary to a numerical array
    input_array = np.array(list(inputs.values())).reshape(1, -1)
    result = classifier.predict(input_array)    
    return result[0]

def main():
    st.title("Loan Prediction App")
    st.write("Please enter the following details to check loan approval status:")

    gender = st.radio("Gender", ['Male', 'Female'])
    married = st.radio("Married", ['Yes', 'No'])
    education = st.radio("Education", ['Graduate', 'Not Graduate'])
    self_employed = st.radio("Self Employed", ['Yes', 'No'])
    dependents = st.selectbox("Dependents", [0, 1, 2, 3])
    applicant_income = st.number_input("Applicant Income", min_value=0, max_value=100000, step=100)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0, max_value=100000, step=100)
    loan_amount = st.number_input("Loan Amount", min_value=0, max_value=100000, step=10)
    # Loan Amount Term in Years and Months
    loan_term_years = st.selectbox("Loan Amount Term (Years)", range(1, 31), format_func=lambda x: f"{x} year(s)")
    loan_term_months = st.selectbox("Loan Amount Term (Months)", range(12), format_func=lambda x: f"{x} month(s)")
    credit_history = st.slider("Credit History", 0, 5, 2)
    property_area = st.selectbox("Property Area", ['Urban', 'Semiurban', 'Rural'])

    # Convert user inputs to numerical values
    gender = 1 if gender == 'Male' else 0
    married = 1 if married == 'Yes' else 0
    education = 0 if education == 'Graduate' else 1
    self_employed = 1 if self_employed == 'Yes' else 0
    
    # Convert years and months to the total number of months
    loan_amount_term = (loan_term_years * 12) + loan_term_months

    # Map property area to numerical values
    property_area_mapping = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}
    property_area = property_area_mapping[property_area]

    inputs = {
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': applicant_income,
        'CoapplicantIncome': coapplicant_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_amount_term,
        'Credit_History': credit_history,
        'Property_Area': property_area
    }

    if st.button("Check Loan Approval"):
        result = predict_loan_approval(inputs)

        if result == 1:
            st.markdown("<p style='text-align: center; font-size: xx-large; font-weight: bold; color: #2C5F2D;'>Congratulations! Loan Approved.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='text-align: center; font-size: xx-large; font-weight: bold; color: #990011;'>Sorry, Loan Not Approved.</p>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
