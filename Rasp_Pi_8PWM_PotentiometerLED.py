import RPi.GPIO as GPIO
import smbus
import time

address = 0x48 #chip address
bus = smbus.SMBus(1)
cmd = 0x40 #analog output address
ledPin = 11 #LED pin (GPIO 17)

def analogRead(chn): #read voltage from input channels 0-3
    value = bus.read_byte_data(address,cmd+chn)
    return value

def analogWrite(value): #write voltage to output port 15
    bus.write_byte_data(address,cmd,value)

def setup():
    global p #duty cycle
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin,GPIO.OUT)
    GPIO.output(ledPin,GPIO.LOW)

    p = GPIO.PWM(ledPin,100) #initialize PWM for LED GPIO 17
    p.start(0) #initialize duty cycle at 0

def loop():
    while True:
        value = analogRead(0)
        p.ChangeDutyCycle(value*100/255) #change duty cycle based on variable resistance 
        voltage = value/255*3.3
        print("ADC Value: %d, Voltage: %.2f"%(value,voltage))
        time.sleep(0.01)

def destroy():
    bus.close()
    GPIO.cleanup()

if __name__ == "__main__":
    print("Program is starting")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        
