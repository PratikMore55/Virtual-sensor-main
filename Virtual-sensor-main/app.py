from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("humidity_prediction_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the ESP32
    data = request.get_json()
    temperature = data.get('temperature')

    if temperature is None:
        return jsonify({'error': 'Temperature value is missing!'}), 400

    # Predict humidity using the model
    prediction = model.predict(pd.DataFrame([[temperature]], columns=['temperature']))
    predicted_humidity = prediction[0]

    # Send the predicted humidity back as a JSON response
    return jsonify({'predicted_humidity': predicted_humidity})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
