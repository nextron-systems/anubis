#include "BluetoothSerial"

#define LED_PIN 4


BluetoothSerial serialBT;

void setup() {
  // put your setup code here, to run once:

  serialBT.begin("Anubis");

}

void loop() {
  // put your main code here, to run repeatedly:

}
