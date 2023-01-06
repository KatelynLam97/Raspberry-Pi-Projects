import RPi.GPIO as GPIO
import time

#define data bit transferred by shift register to latch
LSBFIRST = 1
MSBFIRST = 2

#define pins that connect to 74HC595
dataPin = 11 #DS Pin (14)
latchPin = 13 #ST_CP Pin(12)
clockPin = 15 #SH_CP Pin(11)

def setup():
    GPIO.setmode(GPIO.BOARD);
    GPIO.setup(dataPin, GPIO.OUT)
    GPIO.setup(latchPin, GPIO.OUT)
    GPIO.setup(clockPin, GPIO.OUT)

#enables serial transmission protocol by bit shifting
def shiftOut(dPin,cPin,order,val):
    for i in range(0,8):
        GPIO.output(cPin,GPIO.LOW)
        if(order == LSBFIRST):
            GPIO.output(dPin,(0x01&(val>>i)==0x01) and GPIO.HIGH or GPIO.LOW)
        elif(order == MSBFIRST):
            GPIO.output(dPin,(0x80&(val>>i)==0x80) and GPIO.HIGH or GPIO.LOW)

    GPIO.output(cPin,GPIO.HIGH)

#main
def loop():
    while True:
        x = 0x01 #address for LED output
        for i in range(0,8):
            GPIO.output(latchPin, GPIO.LOW)
            shiftOut(dataPin, clockPin, LSBFIRST,x) #send data to 74HC595
            GPIO.output(latchPin,GPIO.HIGH) #send high level to latch pin to stop reading data and update output
            x<<=1 #performs shift operation to turn on next LED 
            time.sleep(0.1)
            
        x = 0x80
        for i in range(0,8):
            GPIO.output(latchPin, GPIO.LOW)
            shiftOut(dataPin, clockPin, LSBFIRST,x)
            GPIO.output(latchPin,GPIO.HIGH)
            x>>=1
            time.sleep(0.1)

#disable GPIO port
def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
