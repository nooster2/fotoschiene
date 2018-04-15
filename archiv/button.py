import run
import time
import RPi.GPIO as GPIO
import lcddriver


lcd = lcddriver.lcd()
lcd.lcd_clear()
run.starten()
schritte = run.schritte()

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Endanschlag
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) # +
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # -
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Modus

# anzahl Bilder, Stunden, Minuten, Sekunden, Richtung
minimalwerte = [2, 0, 0, 10, 0]
maximalwerte = [9999, 99, 59, 59, 1]
praefix = [">"," ", "h", "m", "s"]
praefixstandard = [" "," ", "h", "m", "s"]
i = 0
einstellungen = minimalwerte
status = ["bejonet-studio","Fotoschiene     "]
while True:
    try:
        input_anschlag = GPIO.input(19)
        input_plus = GPIO.input(15)
        input_minus = GPIO.input(21)
        input_modus = GPIO.input(23)
        # Unterscheidung der Buttons die gedrueckt sind
        if input_plus == False and input_minus == False:
            print("zwei gedrueckt")
        elif input_plus == False:
            einstellungen[i] = einstellungen[i] + 1  
        elif input_minus == False:
            einstellungen[i] = einstellungen[i] - 1
        
        ##dieser Block funktioniert nicht!!!
        # if einstellungen[i] < minimalwerte[i]:
            # einstellungen[i] = maximalwerte[i]
        # elif einstellungen[i] > maximalwerte[i]:
            # einstellungen[i] = minimalwerte[i]

        elif input_modus == False:
            i = i+1
        # Menuefuehrung    
        if i < len(einstellungen)-1:
            praefix[i] = ">"
            praefix[i-1] = praefixstandard[i-1] 
            status[0] = "Einstellen:  "+ str(i)
            status[1] = praefix[0] + str(einstellungen[0]).zfill(4) + praefix[1] + str(einstellungen[1]).zfill(2) + praefix[2] + str(einstellungen[2]).zfill(2) + praefix[3] + str(einstellungen[3]).zfill(2) + praefix[4]
        elif i == len(einstellungen)-1:
            status[0] = "Drehrichtung?   "
            status[1] = str(einstellungen[i]) + "     0=cw 1=ccw"
        ##### Alle Einstellungen sind getroffen!!!
        
        elif i == len(einstellungen):
            status[0] = "Starten? Push M!"
            status[1] = praefix[0] + str(einstellungen[0]).zfill(4) + praefix[1] + str(einstellungen[1]).zfill(2) + praefix[2] + str(einstellungen[2]).zfill(2) + praefix[3] + str(einstellungen[3]).zfill(2) + praefix[4]
            # Einstellungen sind getan, los gehts!
        elif i == len(einstellungen)+1:
            print("Letzte Pause")
        elif i == len(einstellungen) + 2:
            # anzahl, dauer, richtung=0
            dauer = einstellungen[1]*3600 + einstellungen[2]*60 + einstellungen[3]
            schritte.run(einstellungen[0], dauer, einstellungen[4])
            status[0] = "Running"
            break
        
        # Einstellungen sind abgeschlossen, Fragen ob gestaretet werden soll?
        
        
        lcd.lcd_display_string(status[0], 1)
        lcd.lcd_display_string(status[1], 2)
        time.sleep(0.1)
    except KeyboardInterrupt:
        text = "abgebrochen"
        lcd.lcd_clear()
        lcd.lcd_display_string("Button:", 1)
        lcd.lcd_display_string(text, 2)
        break