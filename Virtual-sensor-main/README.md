# Humidity Prediction System Using ESP32 and Flask

This project demonstrates a system where an **ESP32 microcontroller** collects temperature data using a **DHT11 sensor**, sends it to a Flask server, and receives predicted humidity as a response.

---

## Features
1. **ESP32 Code**:
   - Reads temperature from the DHT11 sensor.
   - Sends the temperature as a JSON payload to the Flask server.
   - Displays the server's predicted humidity response.

2. **Flask Server**:
   - Hosts an API endpoint (`/predict`) to receive temperature data.
   - Uses a pre-trained model to predict humidity based on the input temperature.
   - Sends the prediction back as a JSON response.

---

## Prerequisites

### Hardware:
- ESP32 microcontroller
- DHT11 sensor
- Wi-Fi network

### Software:
- Python (for Flask server)
- Required Python libraries: `Flask`, `joblib`, `pandas`
- ESP32 board setup in Arduino IDE

---

## ESP32 Code Instructions

1. **Connect Hardware**:
   - Connect the DHT11 sensor to the ESP32 pin specified in the code (`DHTPIN` is set to GPIO 5).

2. **Update Wi-Fi Credentials**:
   Replace the placeholders with your Wi-Fi network's SSID and password:
   ```cpp
   const char* ssid = "Your_SSID";
   const char* password = "Your_PASSWORD";
   
---

## Library Installation

### Python Libraries (For Flask Server)
Ensure you have Python installed. Install the required libraries by running the following commands:
    ```bash
    
    pip install Flask pandas joblib

---
