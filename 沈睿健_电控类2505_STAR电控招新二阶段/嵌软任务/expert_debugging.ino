#include<SoftwareSerial.h>
#include<Servo.h>
Servo s;
int l[7];
int sum =0;
void setup() {
  Serial.begin(9600);
  s.attach(9, 500, 2500);
  s.write(0);
  delay(100);
}

void loop() {
  if (Serial.available() > 0) {
    byte temp = Serial.read();
    l[sum]=temp;
    sum++;
    if (sum == 7){
      sum=0;
      s.write(l[1]);
    }
  }
}

