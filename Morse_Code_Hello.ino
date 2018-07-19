  //all letters are uppercase except for f
void Dot(){
    digitalWrite(12,HIGH);
    delay(500);
    digitalWrite(12,LOW);
    delay(500);
  }
void Flash(){
    digitalWrite(8,HIGH);
    delay(1500);
    digitalWrite(8,LOW);
    delay(500);
  }
void A(){
  Dot();
  Flash();
  delay(1000);
  }
void B(){
  Flash();
  Dot();
  Dot();
  Dot();
  delay(1000);
  }
void C(){
  Flash();
  Dot();
  Flash();
  Dot();
  delay(1000);
  }
void D(){
  Flash();
  Dot();
  Dot();
  delay(1000);
  }
void E(){
  Dot();
  delay(1000);
  }

void G(){
  Flash();
  Flash();
  Dot();
  delay(1000);
  }

 void f(){
  Dot();
  Dot();
  Flash();
  Dot();
  delay(1000);
 }
void H(){
  Dot();
  Dot();
  Dot();
  Dot();
  delay(1000);
  }
void I(){
  Dot();
  Dot();
  delay(1000);
  }
void J(){
  Dot();
  Flash();
  Flash();
  Flash();
  delay(1000);
  }
void K(){
  Flash();
  Dot();
  Flash();
  delay(1000);
  }
void L(){
  Dot();
  Flash();
  Dot();
  Dot();
  delay(1000);
  }
void M(){
  Flash();
  Flash();
  delay(1000);
  }
void N(){
  Flash();
  Dot();
  delay(1000);
  }
void O(){
  Flash();
  Flash();
  Flash();
  delay(1000);
  }
void P(){
  Dot();
  Flash();
  Flash();
  Dot();
  delay(1000);
  }
void Q(){
  Flash();
  Flash();
  Dot();
  Flash();
  delay(1000);
  }
void R(){
  Dot();
  Flash();
  Dot();
  delay(1000);
  }
void S(){
  Dot();
  Dot();
  Dot();
  delay(1000);
  }
void T(){
  Flash();
  delay(1000);
  }
void U(){
  Dot();
  Dot();
  Flash();
  delay(1000);
  }
void V(){
  Dot();
  Dot();
  Dot();
  Flash();
  delay(1000);
  }
void W(){
  Dot();
  Flash();
  Flash();
  delay(1000);
  }
void X(){
  Flash();
  Dot();
  Dot();
  Flash();
  delay(1000);
  }
void Y(){
  Flash();
  Dot();
  Flash();
  Flash();
  delay(1000);
  }
void Z(){
  Flash();
  Flash();
  Dot();
  Dot();
  delay(1000);
  }

void loop() {
  // put your main code here, to run repeatedly:

}


void setup() {
  // put your setup code here, to run once:
    pinMode(12, OUTPUT);
    pinMode(8, OUTPUT);
  while(true){
    G();
    P();
    X();
    }
}
