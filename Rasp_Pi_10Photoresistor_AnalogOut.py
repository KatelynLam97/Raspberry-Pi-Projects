import RPi.GPIO as GPIO
import smbus
import time

address = 0x48 #PCF8591 reference address
bus = smbus.SMBus(1) #initialize bus object
cmd = 0x40 #slave address

#read analog value from channel 0-3 PCF8591
def analogRead(chn):
    value = bus.read_byte_data(address,cmd+chn)
    return value

#output analog value
def analogWrite(value):
    bus.write_byte_data(address,cmd,value)


#changes brightness of LED based on light intensity detected by photoresistor
def loop():
    while True:
        value = analogRead(0) #reads voltage input from bridge circuit
        analogWrite(value)
        voltage = value/255.0*3.3
        print("ADC value: %d, Voltage: %.2f"%(value,voltage))
        time.sleep(0.01)

#disable GPIO port, close bus 
def destroy():
    bus.close()

#run program until Ctrl+C is pressed
if "__name__" == "__main__":
    print("Program is starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
