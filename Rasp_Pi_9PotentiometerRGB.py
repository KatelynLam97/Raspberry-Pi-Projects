import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40

#initialize led pin positions
ledRedPin = 11
ledGreenPin = 13
ledBluePin = 15

def analogRead(chn): #read analog data from channel 0,1,2,3 on PCF8591
    bus.write_byte(address,cmd+chn) #sends byte to PCF8591, ensuring connectivity
    value = bus.read_byte(address)
    return value

def analogWrite(value): #output analog value
    bus.write_byte_data(address,cmd,value)

def setup():
    #set LED pins as output
    global p_Red, p_Green, p_Blue
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledRedPin, GPIO.OUT)
    GPIO.setup(ledGreenPin, GPIO.OUT)
    GPIO.setup(ledBluePin, GPIO.OUT)

    #enable PWM for each LED
    p_Red = GPIO.PWM(ledRedPin, 1000)
    p_Red.start(0)
    p_Green = GPIO.PWM(ledGreenPin, 1000)
    p_Green.start(0)
    p_Blue = GPIO.PWM(ledBluePin, 1000)
    p_Blue.start(0)

def loop():
    while True:
        #read resistance from potentiometers, channel A0, A1, A2 on PCF8591
        value_Red = analogRead(0)
        value_Green = analogRead(1)
        value_Blue = analogRead(2)

        #map resistance to corresponding PWM value
        p_Red.ChangeDutyCycle(value_Red*100/255)
        p_Green.ChangeDutyCycle(value_Green*100/255)
        p_Blue.ChangeDutyCycle(value_Blue*100/255)
        print("ADC Value value_Red:%d , \tvalue_Green:%d, \tvalue_Blue: %d" %(value_Red,value_Green,value_Blue))
        time.sleep(0.01)

def destroy(): #disable board and bus that reads analog inputs and writes outputs
    bus.close()
    GPIO.cleanup()

#runs program until Ctrl+C is pressed
if __name__=="__main__":
    print("Program is starting")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
