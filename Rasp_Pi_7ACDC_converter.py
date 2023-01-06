import smbus
import time

address = 0x4f #address of chip PCF8591
bus = smbus.SMBus(1)
cmd = 0x40 #chip controls through this address

def analogRead(chn): #reads analog value in chn 0,1,2,3
    value = bus.read_byte_data(address,cmd+chn)
    return value

def analogWrite(value): #outputs Analog value from digital
    bus.write_byte_data(address,cmd,value)

def loop():
    while True:
        value = analogRead(0) #read voltage input from channel 0
        analogWrite(value) #output voltage to LED
        voltage = value/255.0 * 3.3 #voltage value (input)
        print("ADC Value: %d, Voltage: %.2f"%(value, voltage))
        time.sleep(0.01)

def destroy():
    bus.close()

if __name__== "__main__":
    print("Program is starting: ")
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
