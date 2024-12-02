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



