#!/usr/bin/env python2
import RPi.GPIO as GPIO
import time

switchPin = 12
numHitTimes = 0
initialTime = 0
elapsedTime = 0
    
if __name__ == "__main__":
    print ("Program is starting")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        GPIO.add_event_detect(switchPin,GPIO.FALLING)
        while True:
            if GPIO.event_detected(switchPin):
                numHitTimes = numHitTimes + 1
            
            if((numHitTimes % 2) == 0):
                elaspedTime = time.time() - initialTime
                print("Elasped time is" + str(elaspedTime))

            else:
                initialTime = time.time()

    except KeyboardInterrupt:
        GPIO.cleanup()
