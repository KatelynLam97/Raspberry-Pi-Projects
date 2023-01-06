import RPi.GPIO as GPIO

ledPin = 12 #led pin: GPIO 18
sensorPin = 11 #sensor pin: GPIO 17

def setup():
    print("Program is starting...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT) #initialize LED pin as output
    GPIO.setup(sensorPin, GPIO.IN) #initialize sensor pin as input

def loop():
    #turns on LED if a body is detected, otherwise, turn off LED
    while True:
        if(GPIO.input(sensorPin) == GPIO.HIGH):
            GPIO.output(ledPin,GPIO.HIGH)
            print("LED On...")
        else:
            GPIO.output(ledPin,GPIO.LOW)
            print("LED Off...")

#disable GPIO ports
def destroy():
    GPIO.cleanup()

#main
if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
