int LEDdizi[]={2,3,4,5,6,7};
void setup() {
  for (int i=0; i<6; i++)
  {
    pinMode(LEDdizi[i], OUTPUT);  
  }
}

void loop() {
  for (int i =0; i<6; i++)
  {
    digitalWrite(LEDdizi[i], HIGH);
    delay(150);  
    digitalWrite(LEDdizi[i], LOW);    
  }

 for (int j =6; j>0; j--)
  {
    digitalWrite(LEDdizi[j], HIGH);
    delay(150);  
    digitalWrite(LEDdizi[j], LOW);    
  }

}
