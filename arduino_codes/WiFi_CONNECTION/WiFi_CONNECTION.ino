#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Redmi";
const char* password = "123456@Abcd";

#define CAMERA_MODEL_AI_THINKER

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

}

void loop() {
  // put your main code here, to run repeatedly:

}
