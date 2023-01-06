import RPi.GPIO as GPIO
import time
ledPin = 12

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    p = GPIO.PWM(ledPin, 1000) #frequency of analog wave is 1 kHz
    p.start(0) #set initial PWM duty cycle as 0

def loop():
    while True:
        #gradually increase duty cycle to 100%
        for dc in range (0, 101, 1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
        #gradually decrease duty cycle to 0%
        for dc in range (100, -1, -1):
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)

#disable PWM and GPIO pins
def destroy():
    p.stop()
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
