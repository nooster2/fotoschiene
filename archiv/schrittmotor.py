# Raspberry Pi zur Steuerung eines Schrittmotors
# Motor: Nema 17
# Treiber: A4988
# 100/4 = 25 Umdrehungen = 40 cm Vorschlub
# Nutzbarer Weg: 39 cm --> 24 Umdrehungen
# 200 Schritte / Umdrehung 
# Schritte fuer eine Fahrt: 4800

import time
import RPi.GPIO as GPIO
import lcddriver

# display einbinden und reinigen
lcd = lcddriver.lcd()
lcd.lcd_clear()

# GPIO einbinden und reinigen 
GPIO.setwarnings(False)
GPIO.cleanup()

i = 0
pinstep = 11
pindirection = 18
drehrichtung = "cw"
if drehrichtung == "cw":
    drehrichtungstatus = 1
else:
    drehrichtungstatus = 0

# RPi.GPIO Layout verwenden (wie Pin-Nummern)
GPIO.setmode(GPIO.BOARD)
# Pin 11 (GPIO 17) auf Output setzen
GPIO.setup(pinstep, GPIO.OUT)
# Pin 18 (GPIO 24) auf Output setzen
GPIO.setup(pindirection, GPIO.OUT)

# Drehrichtung 1 vorgeben
GPIO.output(pindirection, drehrichtungstatus)
# Schleife um den Motor drehen zu lassen

while i < 10:
    GPIO.output(pinstep, GPIO.HIGH)
    time.sleep(0.0015) # Einheit ist Sekunden, moegliche Notation: 1.0/100
    GPIO.output(pinstep, GPIO.LOW)
    time.sleep(0.0015) # Das schnellste: 0.0015
    i = i + 1
    print i
    lcd.lcd_display_string("Fotoschiene", 1)
    lcd.lcd_display_string(str(i), 2)
# Drehrichtung aendern
print "Richtung 1 fertig"
i = 0
GPIO.output(pindirection, GPIO.HIGH)
time.sleep(1)
#GPIO.output(pindirection, GPIO.LOW)
while i < 4800:
    GPIO.output(pinstep, GPIO.HIGH)
    time.sleep(0.0015)
    GPIO.output(pinstep, GPIO.LOW)
    time.sleep(0.0015)
    i = i + 1
    print i
    lcd.lcd_display_string("Fotoschiene", 1)
    lcd.lcd_display_string(str(i), 2)
print "Richtung 2 fertig, beenden"
