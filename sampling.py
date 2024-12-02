import pandas as pd
framingham = pd.read_csv('framingham.csv')# Dropping null values
framingham = framingham.dropna()
framingham.head()

#framingham['TenYearCHD'].value_counts()



from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
X = framingham.drop('TenYearCHD',axis=1)
y = framingham['TenYearCHD']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20)
oversample = RandomOverSampler(sampling_strategy='minority')
X_over, y_over = oversample.fit_resample(X_train,y_train)
rf = RandomForestClassifier()
rf.fit(X_over,y_over)

preds = rf.predict(X_test)
print(accuracy_score(y_test,preds))

import joblib
joblib.dump(rf, 'fhs_rf_model.pkl')



from sklearn.ensemble import RandomForestClassifier
import pickle

# Train the model (example)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
with open('fhs_rf_model.pkl', 'wb') as file:
    pickle.dump(model, file)
