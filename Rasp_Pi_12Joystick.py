import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40
z_Pin = 12 #GPIO pin for z-motion

def analogRead(chn):
    bus.write_byte(address,cmd+chn)
    value = bus.read_byte(address)
    value = bus.read_byte(address)
    return value

def analogWrite(value):
    bus.write_byte_data(address,cmd,value)

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Z_Pin,GPIO.IN,GPIO.PUD_UP) #set touch pin to have default active high

def loop():
    while True:
        val_Z = GPIO.input(Z_Pin) #read digital value for push switch
        val_Y = analogRead(0)#read analog value for y-motion
        val_X = analogRead(1)#read analog value for x-motion
        print("value_X: %d, \tvlue_Y: %d, \tvalue_Z: %d"%(val_X,val_Y,val_Z))
        time.sleep(0.01)

def destroy():
    bus.close()
    GPIO.cleanup()

if __name__=="__main__":
    print("Program is starting....")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
