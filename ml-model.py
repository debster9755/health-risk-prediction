from sklearn.ensemble import RandomForestClassifier
import pickle

# Train the model (example)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
with open('fhs_rf_model.pkl', 'wb') as file:
    pickle.dump(model, file)
