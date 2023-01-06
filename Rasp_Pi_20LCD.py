from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime

def get_cpu_temp():
    tmp = open(" /sys/class/thermal/thermal_zone0/temp")
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format(float(cpu)/1000)+"C"

def get_time_now():
    return datetime.now().strftime("     %H:%M:%S")

def loop():
    mcp.output(3,1)
    lcd.begin(16,2)
    while(True):
        lcd.setCursor(0,0)
        lcd.message("CPU: "+get_cpu_temp()+"\n")
        lcd.message(get_time_now())
        sleep(1)

def destroy():
    lcd.clear()

PCF8574_address = 0x27
PCF8574A_address = 0x3F

try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print("I2C Address Error")
        exit(1)
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO = mcp)
if __name__ == "__main__":
    print("Program is starting")
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
