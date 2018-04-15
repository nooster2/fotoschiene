import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.cleanup()
i = 0
pinstep = 11
pindirection = 18
pintaster = 24
# RPi.GPIO Layout verwenden (wie Pin-Nummern)
GPIO.setmode(GPIO.BOARD)
# Pin 11 (GPIO 17) auf Output setzen
GPIO.setup(pinstep, GPIO.OUT)
# Pin 18 (GPIO 24) auf Output setzen
GPIO.setup(pindirection, GPIO.OUT)
# Pin 24 (GPIO 8) auf Input setzen
GPIO.setup(pintaster, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Drehrichtung 1 vorgeben
GPIO.output(pindirection, GPIO.LOW)
# Schleife um den Motor drehen zu lassen
GPIO.add_event_detect(pintaster, GPIO.RISING)
while 1:
	GPIO.output(pinstep, GPIO.HIGH)
	time.sleep(0.01)
	GPIO.output(pinstep, GPIO.LOW)
	time.sleep(0.01)
	if GPIO.event_detected(pintaster):
		print("Andere Richtung!",GPIO.input(pindirection))
		GPIO.output(pindirection, (GPIO.input(pindirection)*(-1)+1))
		time.sleep(0.5)