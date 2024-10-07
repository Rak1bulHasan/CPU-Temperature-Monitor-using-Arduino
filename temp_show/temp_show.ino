#include <dht.h>
#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>

LiquidCrystal_I2C lcd(0x27,16,2);
void setup()
{
  Serial.begin(115200);
  lcd.init();
  lcd.clear();         
  lcd.backlight();      // Make sure backlight is on
}
void loop() 
{
  String t = Serial.readStringUntil('\r');
  data_print(t);
  delay(2000); // Delays 2 secods
}

void data_print(String t)
{
  // Print a message on both lines of the LCD.
  lcd.setCursor(0,0);   //Set cursor to character 2 on line 0
  lcd.print("TEMP(C):   " +(t));
  //lcd.setCursor(0,1);
  //lcd.print(' '+' '+' '+' '+' '+' '+' ' +String(t));
  Serial.println(t);
}
