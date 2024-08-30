#include "BluetoothSerial"

#define LED_PIN 4


BluetoothSerial serialBT;
char command; 

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN, OUTPUT);
  
  serialBT.begin("Anubis");

}

void loop() {
  // put your main code here, to run repeatedly:
  if(serialBT.available(){
   command = serialBT.read(); 
  }

  if(command == '1'){
    digitalWrite(LED_PIN, HIGH);
  }

  if(command == '0'){
    digitalWrite(LED_PIN, LOW);
  }

}
