import time
import RPi.GPIO as GPIO
import lcddriver

pinstep = 11
pindirection = 18
lcd = lcddriver.lcd()
def starten():
    # display einbinden und reinigen
    global lcd
    lcd.lcd_clear()
    # GPIO einbinden und reinigen 
    GPIO.setwarnings(False)
    GPIO.cleanup()
    # RPi.GPIO Layout verwenden (wie Pin-Nummern)
    GPIO.setmode(GPIO.BOARD)
    # Pin 11 (GPIO 17) auf Output setzen
    GPIO.setup(pinstep, GPIO.OUT)
    # Pin 18 (GPIO 24) auf Output setzen
    GPIO.setup(pindirection, GPIO.OUT)
    
    maxanzahldrehungen = 4800
    mindauer = 0.0015
class schritte:
    def __init__(self):
        print("Jetzt wurde __init__ ausgefuehrt")

        
    def run(self, anzahl, dauer, richtung=0):
        global pindirection
        global pinstep
        global lcd
        zeile=["Fotoschiene","ist cool"]
        # Drehrichtung behandeln
        if richtung == 0:
            richtungtext = "A->B"
        else:
            richtung = 1
            richtungtext = "B->A"
        # Drehrichtung vorgeben
        GPIO.output(pindirection, richtung)
        # Dauer der Schritte
        schrittdauer = float(dauer/anzahl)
        try:
            for i in range(anzahl):
                GPIO.output(pinstep, GPIO.HIGH)
                time.sleep(schrittdauer/2) # Einheit ist Sekunden, moegliche Notation: 1.0/100
                GPIO.output(pinstep, GPIO.LOW)
                time.sleep(schrittdauer/2) # Das schnellste: 0.0015
                i = i + 1
                print i/float(anzahl)
                zeile[0]=str(richtungtext)
                zeile[1]=str(i)+" "+ str(i/float(anzahl)*100.0)+"%"
                lcd.lcd_display_string(zeile[0], 1)
                lcd.lcd_display_string(zeile[1], 2)
        except KeyboardInterrupt:
            print("Unterbrochen")
            lcd.lcd_display_string("abgebrochen", 1)
            lcd.lcd_display_string(str(i), 2)