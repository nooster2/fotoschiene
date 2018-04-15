import run
import time
import RPi.GPIO as GPIO

import lcddriver
lcd = lcddriver.lcd()

run.starten()
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

zahl = 0
while True:
    try:
        input_state = GPIO.input(19)
        if input_state == True:
            text = "gedrueckt"
            zahl=zahl+1
        else:
            text = "offen    "
        lcd.lcd_display_string("Button:" + text, 1)
        lcd.lcd_display_string(str(zahl), 2)
        time.sleep(0.1)
    except KeyboardInterrupt:
        text = "abgebrochen"
        lcd.lcd_clear()
        lcd.lcd_display_string("Button:", 1)
        lcd.lcd_display_string(text, 2)
        break