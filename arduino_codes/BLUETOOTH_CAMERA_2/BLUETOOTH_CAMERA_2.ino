#include "BluetoothSerial.h"
#include "esp32cam.h"

BluetoothSerial SerialBT;
char command; 

BluetoothSerial serialBT;

void setup() {

  serialBT.begin("Anubis");
  
}

void loop() {
    
}
