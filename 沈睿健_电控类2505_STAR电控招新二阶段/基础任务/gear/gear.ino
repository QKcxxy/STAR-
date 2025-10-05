#include<Servo.h>
Servo s;
int pos[]={0,30,45,90,135};
void setup() {
  // put your setup code here, to run once:
  s.attach(9,500,2500);
  s.write(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i=0;i<5;i++){
    s.write(pos[i]);
    delay(1000);
  }
}
