#!/usr/bin/env python2 
#type python2 filename to run
import RPi.GPIO as GPIO

buttonPin = 40
index = 0
ledList = [11,13,15,12,16,18,19,21,23]
lettersList[[11,13,15,12,16,18,21],[11,19,12,13,21,15,23,18],[11,13,15,23,18],[11,13,15,23,18],[11,19,12,13,15,23,18,16]]
listLength = len(hList)

def setup(ledPin):
        GPIO.setmode(GPIO.BOARD) #set pin number by location
        GPIO. setup(ledPin, GPIO.OUT) #sets GPIO as output
        GPIO.output(ledPin, GPIO.LOW) #output value of low
        print ("using pin%d" %ledPin)

def turnSequenceOn(sequenceList):
        for i in range(listLength):
                if(sequenceList[i]):
                        GPIO.output(ledList[i],GPIO.HIGH)
                else:
                        GPIO.output(ledList[i],GPIO.LOW)
        if(index == 5):
                index = 0

        else:
                index++

def destroy(closeLedPin):
    GPIO.output(closeLedPin, GPIO.low) #output low voltage, turn LED off
    GPIO.cleanup #disable GPIO pins

if __name__ == "__main__":
        for i in range (0, listLength + 1):
                setup(ledList[i])

        try:
                GPIO.add_event_detect(buttonPin,GPIO.RISING,callback=turnSequenceOn(lettersList[index]),bouncetime = 300)
                
                
        except KeyboardInterrupt:
                for j in range (0, listLength + 1):
                        destroy(ledList[j])
     
            
            
