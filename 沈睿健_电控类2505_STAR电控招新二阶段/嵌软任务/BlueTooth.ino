#include<SoftwareSerial.h>
#include<Servo.h>
Servo s;
int t;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  s.attach(9, 500, 2500);
  s.write(0);
  delay(1000);
}

void loop() {
  while (Serial.available() > 0){
    t = Serial.parseInt();
    if (t!=0) s.write(t);
  }
}

