#!/usr/bin/env python2 
#type python2 filename to run
import RPi.GPIO as GPIO
import time

ledList = [11,12,13,15,16,18,22,3,5,24]
listLength = len(ledList)

def setup(ledPin):
        GPIO.setmode(GPIO.BOARD) #set pin number by location
        GPIO. setup(ledPin, GPIO.OUT) #sets GPIO as output
        GPIO.output(ledPin, GPIO.LOW) #output value of low
        print ("using pin%d" %ledPin)

def loop():
        while True:
                #turn on led display from left to right, then turn all off
                for k in range (0, listLength + 1):
                        GPIO.output(ledList[k], GPIO.HIGH)
                        time.sleep(0.5)
                        GPIO.output(ledList[k], GPIO.LOW)
                        
                #turn on led display from right to left, then turn all off        
                for m in range (listLength,-1,-1):
                        GPIO.output(ledList[m], GPIO.LOW)
                        time.sleep(0.5)
                        GPIO.output(ledList[m], GPIO.LOW)
        time.sleep(1)

            
def destroy(closeLedPin):
    GPIO.output(closeLedPin, GPIO.low) #output low voltage, turn LED off
    GPIO.cleanup #disable GPIO pins

if __name__ == "__main__":
        
        for i in range (0, listLength + 1)
                setup(ledList[i])
                
#throws try/catch exception where LED continues blinking until Ctrl+C is pressed
    try:
        loop()
    except KeyboardInterrupt:
        for j in range (0, listLength + 1)
                destroy(ledList[j])
     
            
            
