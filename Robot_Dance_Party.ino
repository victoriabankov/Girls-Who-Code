
#include <Servo.h>

Servo servoLeft;                             // Declare left servo signal
Servo servoRight;                            // Declare right servo signal

  //all letters are uppercase except for f
void Dot(){
    digitalWrite(12,HIGH);
    delay(500);
    digitalWrite(12,LOW);
    delay(500);
  }
void Flash(){
    digitalWrite(11,HIGH);
    delay(1500);
    digitalWrite(11,LOW);
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

int PIEZOPIN = 5;                            // Declare pin that the piezo is connected to.
// DECLARE LED PINS HERE

// One octave of notes between A4 and A5, for Piezo Greeting
int note_A4 = 440;
int note_As4 = 466; int note_Bb4 = note_As4;
int note_B4 = 494;
int note_C5 = 523;
int note_Cs5 = 554; int note_Db5 = note_Cs5;
int note_D5 = 587;
int note_Ds5 = 622; int note_Eb5 = note_Ds5;
int note_E5 = 659;
int note_F5 = 698;
int note_Fs5 = 740; int note_Gb5 = note_Fs5;
int note_G5 = 784;
int note_Gs5 = 830; int note_Ab5 = note_Gs5;

void setup()
{
  pinMode(PIEZOPIN, OUTPUT);                 // Attach piezo to pin 5. 
  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12
  // Attach LED pins here.
  
}  
  
void loop()
{
  // Code for testing servos. 
  // Tinker with the numbers to see how they work!
  // For help, visit https://learn.parallax.com/tutorials/robot/shield-bot/robotics-board-education-shield-arduino/chapter-2-shield-lights-servo-4. 
  
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(PIEZOPIN, OUTPUT);
   for(int x = 1; x < 2; x += 1){
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_G5,200);
    delay(500);
    tone(PIEZOPIN,note_F5,200);  
    delay(500);
    tone(PIEZOPIN,note_G5,200);
    delay(500);
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_G5,200);
    delay(500);
    tone(PIEZOPIN,note_G5,200);
    delay(500);
    tone(PIEZOPIN,note_G5,200);
    delay(500);
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_C5,200);
    delay(500);
    tone(PIEZOPIN,note_C5,200);
    delay(500);
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_G5,200);
    delay(500);
    tone(PIEZOPIN,note_F5,200);  
    delay(500);
    tone(PIEZOPIN,note_G5,200);
    delay(500);
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_G5,200);
    delay(500);
    tone(PIEZOPIN,note_G5,200);
    delay(500);
    tone(PIEZOPIN,note_A4,200);
    delay(500);
    tone(PIEZOPIN,note_G5,200);
    delay(500);
    tone(PIEZOPIN,note_F5,200);  
    delay(500);
    }
   for(int x = 1; x < 20; x += 1){
    G();
    P();
    X();
    
    servoLeft.writeMicroseconds(1700);
    servoRight.writeMicroseconds(1300);
    delay(50);

    servoLeft.writeMicroseconds(1300);
    servoRight.writeMicroseconds(1700);
    delay(50);
  }
  servoLeft.writeMicroseconds(700);
  delay(400);
}



