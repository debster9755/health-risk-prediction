# Random Forest Classifier - Health Risk Prediction App

This project uses a Random Forest Classifier to predict the chances of health risks based on user-provided input variables. The app is developed using **Streamlit** for a web-based interface.

---

## **Project Files**
1. **`sampling.py`**:
   - Prepares the Random Forest Classifier model using the Framingham dataset.
   - Performs oversampling on the minority class using `RandomOverSampler`.
   - Trains a Random Forest model.
   - Saves the trained model as `fhs_rf_model.pkl`.

2. **`streamlit_fhs9.py`**:
   - A web application built with Streamlit.
   - Allows users to input health-related variables.
   - Predicts the likelihood of health risk based on user input using the trained model.

3. **`fhs_rf_model.pkl`**:
   - A serialized Random Forest model trained on the Framingham dataset.

---

## **Steps to Run the Application**

### **1. Prepare the Environment**
- Ensure you have Python installed (version 3.7 or later).
- Install the required dependencies:
  ```bash
  pip install -r requirements.txt



# WORKFLOW

# Train the Model
Run the sampling.py script to train the Random Forest model and generate the fhs_rf_model.pkl file:

python sampling.py


# Start the Streamlit App
Run the Streamlit app using the following command:

streamlit run streamlit_fhs9.py

# Open the Web Application
Navigate to your browser and open

http://localhost:8501


# Using the Application
## Enter the following details in the form:


Gender (Male/Female)

Age

Highest Academic Qualification

Smoking Habits (Yes/No) and Number of Daily Cigarettes

Whether on BP Medication (Yes/No)

History of Stroke (Yes/No)

Hypertension and Diabetes Status (Yes/No)

Cholesterol Level

Systolic and Diastolic Blood Pressure

BMI (Body Mass Index)

Resting Heart Rate

Glucose Level


Click the "Predict" button.

The app will display:


"Yes": If there is a health risk.

"No": If there is no health risk.


# Dependencies
Python Libraries:
pandas
numpy
scikit-learn
imbalanced-learn
streamlit

## To install dependencies:

pip install pandas numpy scikit-learn imbalanced-learn streamlit




