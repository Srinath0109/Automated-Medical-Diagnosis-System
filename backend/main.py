from flask import Flask, request, jsonify
from models.predict import predict_disease
from database.db import session, Patient

app = Flask(__name__)

@app.route("/diagnose", methods=["POST"])
def diagnose():
    """API to predict disease from symptoms"""
    data = request.json
    symptoms = data.get("symptoms")

    if not symptoms:
        return jsonify({"error": "No symptoms provided"}), 400

    diagnosis = predict_disease(symptoms)

    # Store patient record
    patient = Patient(name=data.get("name"), age=data.get("age"), symptoms=str(symptoms), diagnosis=diagnosis)
    session.add(patient)
    session.commit()

    return jsonify({"diagnosis": diagnosis})

if __name__ == "__main__":
    app.run(debug=True)
