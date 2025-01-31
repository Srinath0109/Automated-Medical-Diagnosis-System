import joblib
import numpy as np
from config import MODEL_PATH

# Load trained model
model = joblib.load(MODEL_PATH)

def predict_disease(symptoms):
    """Predict disease based on input symptoms"""
    symptoms_array = np.array(symptoms).reshape(1, -1)
    prediction = model.predict(symptoms_array)
    return prediction[0]
