import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40
motoRPin1 = 13 #pin on GPIO Board connected to motor out1 on L293D
motoRPin2 = 11 #connected to motor out 2
enablePin = 15 #connected to enable1

#reads analog input from a given channel on PCF8591
def analogRead(chn):
    value = bus.read_byte_data(address,cmd+chn)
    return value

#output analog value 
def analogWrite(value):
    bus.write_byte_data(address,cmd,value)

def setup(): #initialize GPIO pins to output, setup PWM
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motoRPin1, GPIO.OUT)
    GPIO.setup(motoRPin2, GPIO.OUT)
    GPIO.setup(enablePin, GPIO.OUT)

    p = GPIO.PWM(enablePin, 1000) #creates PWM
    p.start(0)

#adjusts speed of motor based on resistance from potentiometer
def mapNUM(value,fromLow,fromHigh,toLow,toHigh):
    return(toHigh-toLow)*(value-fromLow)/(fromHigh-fromLow)#ranges from 0-128, value is a percentage of that cycle

def motor(ADC): #controls speed and direction of motor based on potentiometer
    value = ADC - 128
    if(value > 0): #spins motor clockwise if potentiometer turns to the left
        GPIO.output(motoRPin1, GPIO.HIGH)
        GPIO.output(motoRPin2, GPIO.LOW)
        print("Turn Forward...")
    elif (value < 0): #spins motor counterclockwise if potentiometer turns to the right
        GPIO.output(motoRPin1, GPIO.LOW)
        GPIO.output(motoRPin2, GPIO.HIGH)
        print("Turn Backward...")
    else:#stationary at middle position
        GPIO.output(motoRPin1, GPIO.LOW)
        GPIO.output(motoRPin2, GPIO.LOW)
        print("Motor stop...")

    #outputs voltage that corresponds to potentiometer circuit to change speed of motor
    p.start(mapNUM(abs(value),0,128,0,100)) 
    print("The PWM duty cycle is %d%%\n"%(abs(value)*100/127))

#main function
def loop():
    while True:
        value = analogRead(0)
        print("ADC Value: %d"%(value))
        motor(value)
        time.sleep(0.01)

#disables ports
def destroy():
    bus.close()
    GPIO.cleanup()

if __name__== "__main__":
    print("Program is starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        
