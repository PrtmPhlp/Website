########################################################################
# EINSCHALTEN EINER LED VIA GPIO UND PYTHON
########################################################################
import RPi.GPIO as GPIO
import time    # Verzögerung

ledPin = 11    # Benutzter Pin

def setup():
    GPIO.setmode(GPIO.BOARD)       # GPIO "einschalten"
    GPIO.setup(ledPin, GPIO.OUT)   # LED ausschalt Sequenz "einschalten"
    GPIO.output(ledPin, GPIO.LOW)  # Die tatsächliche Aktion definieren

def loop():
    while True:
        time.sleep(1)              # 1 Sekunde Verzögerung
        GPIO.output(ledPin, GPIO.HIGH)   # LED ausschalten

def destroy():
    GPIO.cleanup()                      # Strom aller Pins deaktivieren

if __name__ == '__main__':    # Standart Vorgang zum beenden des Programmes
    print ('Program is starting ... \n')   # Start Mitteilung
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # ctrl-c zum stoppen des Programmes
        destroy()

