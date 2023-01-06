#!/usr/bin/env python2 
#type python2 filename to run
import RPi.GPIO as GPIO
import time

ledPin = 11; #references pin number on RPi

def setup():
        GPIO.setmode(GPIO.BOARD) #set pin number by location
        GPIO. setup(ledPin, GPIO.OUT) #sets GPIO as output
        GPIO.output(ledPin, GPIO.LOW) #output value of low
        print ("using pin%d" %ledPin)

def loop():
        while True:
            GPIO.output(ledPin, GPIO.HIGH) #output high voltage
            print ("...led on")
            time.sleep(1) #1 second delay
            GPIO.output(ledPin, GPIO.LOW) #output low voltage
            print ("...led off")
            time.sleep(1)

def destroy():
    GPIO.output(ledPin, GPIO.low) #output low voltage, turn LED off
    GPIO.cleanup #disable GPIO pins

if _name_ == "_main_":
    setup()
#throws try/catch exception where LED continues blinking until Ctrl+C is pressed
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
            
            
