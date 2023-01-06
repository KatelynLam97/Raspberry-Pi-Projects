import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40
z_Pin = 40 #GPIO pin for z-motion
xRange = 128 
yRange = 128
ledPins = {"xHigh":29,"xLow":31,"yHigh":33,"yLow":35,"zOn":37}

def analogRead(chn):
    bus.write_byte(address,cmd+chn)
    value = bus.read_byte(address)
    value = bus.read_byte(address)
    return value

def analogWrite(value):
    bus.write_byte_data(address,cmd,value)

def setup():
    GPIO.setmode(GPIO.BOARD)
    for i in ledPins:
        GPIO.setup(pins[i],GPIO.OUT)
        GPIO.output(pins[i],GPIO.LOW)
    GPIO.setup(Z_Pin,GPIO.IN,GPIO.PUD_UP) #set touch pin to have default active high

def loop():
    while True:
        val_Z = GPIO.input(Z_Pin) #read digital value for push switch
        if val_Z == 1:
            GPIO.output(ledPins["zOn"],GPIO.HIGH)
        else:
            GPIO.output(ledPins["zOn"],GPIO.LOW)
        val_Y = analogRead(0)#read analog value for y-motion
        if val_Y < yRange:
            GPIO.output(ledPins["yHigh"],GPIO.LOW)
            GPIO.output(ledPins["yLow"],GPIO.HIGH)
        else:
            GPIO.output(ledPins["yHigh"],GPIO.HIGH)
            GPIO.output(ledPins["yLow"],GPIO.LOW)
            
        val_X = analogRead(1)#read analog value for x-motion
        if val_X < xRange:
            GPIO.output(ledPins["xHigh"],GPIO.LOW)
            GPIO.output(ledPins["xLow"],GPIO.HIGH)
        else:
            GPIO.output(ledPins["xHigh"],GPIO.HIGH)
            GPIO.output(ledPins["xLow"],GPIO.LOW)
        print("value_X: %d, \tvlue_Y: %d, \tvalue_Z: %d"%(val_X,val_Y,val_Z))
        time.sleep(0.01)

def destroy():
    bus.close()
    for j in ledPins:
        GPIO.output(pins[i],GPIO.LOW)
    GPIO.cleanup()

if __name__=="__main__":
    print("Program is starting....")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
