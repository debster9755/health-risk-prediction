import streamlit as st
import pickle
import numpy as np

# Load the Random Forest model
try:
    with open('fhs_rf_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # Verify the model type
    if not hasattr(model, "predict"):
        raise ValueError("The loaded object is not a valid scikit-learn model.")
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()  # Stop execution if the model is not loaded properly

# App title
st.title("Random Forest Classifier - Health Risk Prediction App")

# Description
st.write("""
This app uses a pre-trained Random Forest Classifier to predict health risks. 
Please provide the required details below.
""")

# Input fields for user data
st.header("Enter Your Details")

# Collecting user input for the specified variables
gender = st.selectbox("Enter your gender", ["Male", "Female"])
age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)

qualification = st.selectbox(
    "Highest academic qualification",
    ["High school diploma", "Undergraduate degree", "Postgraduate degree", "PhD"]
)

smoker = st.selectbox("Are you currently a smoker?", ["Yes", "No"])
daily_cigarettes = st.number_input("Number of daily cigarettes", min_value=0, value=0)

bp_medication = st.selectbox("Are you currently on BP medication?", ["Yes", "No"])
stroke = st.selectbox("Have you ever experienced a stroke?", ["Yes", "No"])
hypertension = st.selectbox("Do you have hypertension?", ["Yes", "No"])
diabetes = st.selectbox("Do you have diabetes?", ["Yes", "No"])

cholesterol = st.number_input("Enter your cholesterol level", min_value=0.0, value=200.0)
systolic_bp = st.number_input("Enter your systolic blood pressure", min_value=0.0, value=120.0)
diastolic_bp = st.number_input("Enter your diastolic blood pressure", min_value=0.0, value=80.0)
bmi = st.number_input("Enter your BMI", min_value=0.0, value=25.0)
resting_hr = st.number_input("Enter your resting heart rate", min_value=0.0, value=70.0)
glucose = st.number_input("Enter your glucose level", min_value=0.0, value=100.0)

# Convert categorical inputs into numeric values for the model
gender_numeric = 1 if gender == "Male" else 0
smoker_numeric = 1 if smoker == "Yes" else 0
bp_medication_numeric = 1 if bp_medication == "Yes" else 0
stroke_numeric = 1 if stroke == "Yes" else 0
hypertension_numeric = 1 if hypertension == "Yes" else 0
diabetes_numeric = 1 if diabetes == "Yes" else 0

qualification_mapping = {
    "High school diploma": 0,
    "Undergraduate degree": 1,
    "Postgraduate degree": 2,
    "PhD": 3
}
qualification_numeric = qualification_mapping[qualification]

# Combine all inputs into a single array for the model
input_data = np.array([
    gender_numeric,
    age,
    qualification_numeric,
    smoker_numeric,
    daily_cigarettes,
    bp_medication_numeric,
    stroke_numeric,
    hypertension_numeric,
    diabetes_numeric,
    cholesterol,
    systolic_bp,
    diastolic_bp,
    bmi,
    resting_hr,
    glucose
]).reshape(1, -1)

# Prediction button
if st.button("Predict"):
    try:
        # Make prediction
        prediction = model.predict(input_data)

        # Display result as "Yes" or "No"
        if prediction[0] == 1:
            st.success("Yes")
        else:
            st.error("No")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
