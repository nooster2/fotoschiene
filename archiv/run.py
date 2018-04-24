import time
import RPi.GPIO as GPIO
import lcddriver
import math

pinstep = 11
pindirection = 18
lcd = lcddriver.lcd()
def starten():
    # display einbinden und reinigen
    global lcd
    lcd.lcd_clear()
    # GPIO einbinden und reinigen 
    GPIO.setwarnings(True)
    # RPi.GPIO Layout verwenden (wie Pin-Nummern)
    GPIO.setmode(GPIO.BOARD)
    # Pin 11 (GPIO 17) auf Output setzen
    GPIO.setup(pinstep, GPIO.OUT)
    # Pin 18 (GPIO 24) auf Output setzen
    GPIO.setup(pindirection, GPIO.OUT)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Endanschlag
    
    
    maxanzahldrehungen = 4800
    mindauer = 0.0015
class schritte:
    def __init__(self):
        print("Jetzt wurde __init__ ausgefuehrt")

    def getbargraph(self, prozent=0):
        zeichen = ""
        anzahlzeichen = 10.0
        anzahlvoll = int(math.floor(prozent/anzahlzeichen))
        for i in range(anzahlvoll):
            zeichen = zeichen + "*"
        anzahlhalb = 0
        if (prozent-anzahlvoll*anzahlzeichen)>=5:
            anzahlhalb = 1
        for i in range(anzahlhalb):
            zeichen = zeichen + "/"
        anzahlleer = int(anzahlzeichen-anzahlvoll-anzahlhalb)
        for i in range(anzahlleer):
            zeichen = zeichen +" "
        return zeichen
        
    def run(self, anzahl, dauer, richtung=0):
        global pindirection
        global pinstep
        global lcd
        zeile=["Fotoschiene","ist cool"]
        # Drehrichtung behandeln
        if richtung == 0:
            richtungtext = "A>B"
        else:
            richtung = 1
            richtungtext = "B>A"
        # Drehrichtung vorgeben
        GPIO.output(pindirection, richtung)
        # Dauer der Schritte
        schrittdauer = float(dauer)/anzahl
        print("Hier passt es noch!")
        try:
            for i in range(anzahl):
                input_anschlag = GPIO.input(19)
                if input_anschlag == True:
                    print("Endanschlag erreicht")
                    zeile[0]=str(richtungtext) + " Endanschlag!"
                    i = anzahl-1
                    #break
                GPIO.output(pinstep, GPIO.HIGH)
                time.sleep(schrittdauer/2) # Einheit ist Sekunden, moegliche Notation: 1.0/100
                GPIO.output(pinstep, GPIO.LOW)
                time.sleep(schrittdauer/2) # Das schnellste: 0.0015
                i = i + 1
                dauer = dauer - schrittdauer
                zeile[0]=str(richtungtext) + "  ETA: " + str(round(dauer,1)).zfill(6)
                
                # Fortschrittsbalken holen
                fortschritt=schritte.getbargraph(self,100*i/float(anzahl))
                zeile[1]=str(i).zfill(4)+"  "+ fortschritt
                lcd.lcd_display_string(zeile[0], 1)
                lcd.lcd_display_string(zeile[1], 2)
        except KeyboardInterrupt:
            print("Unterbrochen")
            lcd.lcd_display_string("abgebrochen", 1)
            lcd.lcd_display_string(str(i), 2)
        finally:
            lcd.lcd_display_string(zeile[0], 1)
            lcd.lcd_display_string(zeile[1], 2)
        print("Schritte gemacht!")
            #lcd.lcd_display_string("Fertig!",1)
            #lcd.lcd_display_string(str(anzahl)+" Schritte",2)