import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
data = pd.read_csv("../dataset/disease_data.csv")

X = data.drop(columns=["Disease"])
y = data["Disease"]

# Train ML model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "../models/medical_model.pkl")
