import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

# Load the dataset
data = pd.read_csv(r"C:\Users\Pratik\Downloads\Virtual-sensor-main\Virtual-sensor-main\sensor_data.csv")

print("Columns in the dataset:", data.columns)

# Clean and preprocess data
data.columns = data.columns.str.strip().str.lower()
data['temperature'] = data['temperature'].replace(r'T=', '', regex=True) 
data['temperature'] = pd.to_numeric(data['temperature'], errors='coerce') 
data['humidity'] = data['humidity'].replace(r'H=', '', regex=True)  
data['humidity'] = pd.to_numeric(data['humidity'], errors='coerce')  

# Check for required columns
if 'temperature' not in data.columns or 'humidity' not in data.columns:
    print("Error: Missing 'temperature' or 'humidity' columns!")
else:
    data = data.dropna(subset=['temperature', 'humidity'])

    # Split data
    X = data[['temperature']]  
    y = data['humidity']      
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"R-squared (R²): {r2}")

    # Save the model as a .pkl file
    with open("humidity_prediction_model.pkl", "wb") as file:
        pickle.dump(model, file)
    print("Model saved as 'humidity_prediction_model.pkl'")

    # Predict for new temperature
    new_temperature = 22.0 
    new_data = pd.DataFrame([[new_temperature]], columns=['temperature'])
    predicted_humidity = model.predict(new_data)
    print(f"Predicted humidity for temperature {new_temperature}°C: {predicted_humidity[0]}%")
