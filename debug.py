import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Endanschlag
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) # +
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # -
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Modus

status = [0,0,0,0]
try:
    while True:
        status[0] = GPIO.input(13)
        status[1] = GPIO.input(19)
        status[2] = GPIO.input(21)
        status[3] = GPIO.input(23)
        print(status)
finally:
    GPIO.cleanup()