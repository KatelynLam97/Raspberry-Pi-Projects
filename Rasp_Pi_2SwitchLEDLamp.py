#!/usr/bin/env python2
import RPi.GPIO as GPIO
from Logger import Logger

buttonPin = 11 #pin location of switch
ledPin = 12 #pin location of LED
ledState = False #state of LED on or off

def setup():
    print ("Program is starting...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #initializes buttonPin as input with initial value 3.3V

def loop():
def destroy():
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

def buttonEvent():
    Logger.writeLog("Button pressed")
    startTime = time.time()
    global ledState
    ledState = not ledState; #reverses state of LED when buttonEvent is called
    if ledState == True:
        message = "Turn on LED..."
    else:
        message = "Turn off LED..."
    GPIO.output(ledPin,ledState)
    print(message)
    Logger.writeLog(message + " Elapsed time: " + str(time.time()-startTime)

#main body of program
if __name__ == "__main__":
    setup()
    try:
        #detects whether the button is pressed
        GPIO.add_event_detect(buttonPin,GPIO.FALLING, callback = buttonEvent, bouncetime = 300)
        print ("buttonEvent GPIO%d" %channel)
        while True:
        if GPIO.event_detected(buttonPin):
            
                              
    except KeyboardInterrupt:
        destroy()
        
