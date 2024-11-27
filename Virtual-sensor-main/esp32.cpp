#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

#define DHTPIN 5      
#define DHTTYPE DHT11  
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "Pratik_2.4G";
const char* password = "Ganesh@348";

const char* serverURL = "http://192.168.1.40:5000";  

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to Wi-Fi...");
  }
  Serial.println("Connected to Wi-Fi");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    float temperature = dht.readTemperature();

    if (isnan(temperature)) {
      Serial.println("Failed to read temperature from DHT11 sensor!");
    } else {
      Serial.print("Temperature: ");
      Serial.print(temperature);
      Serial.println("°C");

      String jsonPayload = "{\"temperature\": " + String(temperature) + "}";

      http.begin("http://192.168.1.40:5000/predict"); 
      http.addHeader("Content-Type", "application/json");  

      int httpResponseCode = http.POST(jsonPayload);

      if (httpResponseCode > 0) {
        String response = http.getString();
        Serial.print("Server Response: ");
        Serial.println(response);
      } else {
        Serial.print("Error sending POST request: ");
        Serial.println(httpResponseCode);
      }

      http.end(); 
    }
  } else {
    Serial.println("Wi-Fi not connected!");
  }

  delay(10000);
}
