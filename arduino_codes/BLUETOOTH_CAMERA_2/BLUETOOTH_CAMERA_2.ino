#include "BluetoothSerial.h"
#include "esp32cam.h"

esp32cam::Resolution initialResolution;

BluetoothSerial SerialBT;

void setup() {
    Serial.begin(115200);
    SerialBT.begin("ESP32Camera");
    Serial.println("Bluetooth device is ready to pair");
}

void loop() {
    if (SerialBT.available()) {
        char incoming = SerialBT.read();
        Serial.print("Received: ");
        Serial.println(incoming);

        if (incoming == 'c') {
            takePhoto();
        }
    }
    delay(20);
}

void takePhoto() {
    // Capture a frame using the esp32cam library
    auto frame = esp32cam::capture();
    if (!frame) {
        Serial.println("Camera capture failed");
        SerialBT.println("Camera capture failed");
        return;
    }

    // Get the image size
    size_t frameSize = frame->size();
    SerialBT.printf("Photo taken! Size: %d bytes\n", frameSize);

    // Send the image data over Bluetooth
    SerialBT.write(frame->data(), frameSize);
    Serial.println("Photo data sent over Bluetooth");

    // Release the frame
    frame.reset();
}
