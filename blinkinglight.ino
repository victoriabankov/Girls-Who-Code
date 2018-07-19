void setup() {
  // put your setup code here, to run once:
    pinMode(12, OUTPUT);
    for(int i = 0;i<4;i++){
    digitalWrite(12,HIGH);
    delay(500);
    digitalWrite(12,LOW);
    delay(500);
  }
  delay(1000);
    for(int i = 0;i<1;i++){
    digitalWrite(12,HIGH);
    delay(500);
    digitalWrite(12,LOW);
    delay(500);
  }
  delay(1000);
    for(int i = 0;i<2;i++){
    digitalWrite(12,HIGH);
    delay(500);
    digitalWrite(12,LOW);
    delay(500);
    digitalWrite(12,HIGH);
    delay(1500);
    digitalWrite(12,LOW);
    delay(500);
    digitalWrite(12,HIGH);
    delay(500);
    digitalWrite(12,LOW);
    delay(500);
    digitalWrite(12,HIGH);
    delay(500);
    digitalWrite(12,LOW);
    delay(500);
    delay(1000);
  }
    for(int i = 0;i<3;i++){
    digitalWrite(12,HIGH);
    delay(1500);
    digitalWrite(12,LOW);
    delay(500);
}
}

void loop() {
  // put your main code here, to run repeatedly:
 
}
