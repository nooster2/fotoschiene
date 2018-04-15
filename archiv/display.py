import lcddriver
from time import *
 
lcd = lcddriver.lcd()
lcd.lcd_clear()
 
lcd.lcd_display_string("Fotoschiene", 1)
lcd.lcd_display_string("100 stps  10m00s", 2)