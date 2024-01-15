import joblib

# Test loading the model
try:
    model = joblib.load('random_forest_classifier.joblib')
    print("Model loaded successfully")
except Exception as e:
    print("Error loading model:", e)

