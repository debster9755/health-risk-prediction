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



project/
├── sampling.py             # Script for training the Random Forest model
├── streamlit_fhs9.py       # Streamlit app for user input and predictions
├── fhs_rf_model.pkl        # Trained model file
├── README.md               # Documentation
