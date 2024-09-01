#include "BluetoothSerial.h"
#include "esp_camera.h"

BluetoothSerial serialBT;

camera_config_t config = {
    .pin_pwdn = -1,
    .pin_reset = -1,
    .pin_xclk = 0,
    .pin_sccb_sda = 26,
    .pin_sccb_scl = 27,
    .pin_d7 = 35,
    .pin_d6 = 34,
    .pin_d5 = 39,
    .pin_d4 = 36,
    .pin_d3 = 21,
    .pin_d2 = 19,
    .pin_d1 = 18,
    .pin_d0 = 5,
    .pin_vsync = 25,
    .pin_href = 23,
    .pin_pclk = 22,
    .xclk_freq_hz = 20000000,
    .ledc_timer = LEDC_TIMER_0,
    .ledc_channel = LEDC_CHANNEL_0,
    .pixel_format = PIXFORMAT_JPEG,
    .frame_size = FRAMESIZE_SVGA,
    .jpeg_quality = 12,
    .fb_count = 2,
};



void setup() {
  
    Serial.begin(115200); // Start Serial communication
    serialBT.begin("ESP32Camera"); // Bluetooth device name
    Serial.println("Bluetooth device is ready to pair");

    // Initialize the camera
    if (!esp_camera_init(&config)) {
        Serial.println("Camera init failed");
        return;
    }

}

void loop() {
  // put your main code here, to run repeatedly:
  if (serialBT.available()) { // Check if data is available
        char incoming = serialBT.read(); // Read the incoming data
        Serial.print("Received: ");
        Serial.println(incoming);

        if (incoming == 'c') { // If 'c' is received, take a photo
            takePhoto();
        }
    }
    delay(20); // Small delay for stabilityif (serialBT.available()) { // Check if data is available
        char incoming = serialBT.read(); // Read the incoming data
        Serial.print("Received: ");
        Serial.println(incoming);

        if (incoming == 'c') { // If 'c' is received, take a photo
            takePhoto();
        }
    }
    delay(20); // Small delay for stability

}

void takePhoto() {
    // Capture a frame
    camera_fb_t *fb = esp_camera_fb_get();
    if (!fb) {
        Serial.println("Camera capture failed");
        serialBT.println("Camera capture failed");
        return;
    }

    // Send the image size to the Bluetooth terminal
    serialBT.printf("Photo taken! Size: %d bytes\n", fb->len);

    // Optionally, you can send the image data over Bluetooth
    // Uncomment the following lines to send the image data
    
    serialBT.write(fb->buf, fb->len);
    Serial.println("Photo data sent over Bluetooth");
    

    // Return the frame buffer back to the driver
    esp_camera_fb_return(fb);
}
