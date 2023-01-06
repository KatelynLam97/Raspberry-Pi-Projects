#!/usr/bin/env python2
import RPi.GPIO as GPIO

buttonPin = 11 #pin location of switch
ledPin = 12 #pin location of LED

def setup():
    print ("Program is starting...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #initializes buttonPin as input with initial value 3.3V

#disables output pin only
def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

#main body of program
if __name__ == "__main__":
    setup()
    try:
        print("Press button to turn on light")
        while(GPIO.input(buttonPin)== GPIO.LOW):
            GPIO.output(ledPin, GPIO.HIGH)
            print ("LED on...")
        print("LED off...")
    except KeyboardInterrupt:
        destroy()
        
