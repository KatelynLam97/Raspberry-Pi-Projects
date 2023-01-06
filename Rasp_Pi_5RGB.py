import RPi.GPIO as GPIO
import time
import random

pins = {"pin_R":11,"pin_G":12,"pin_B":13} #dictionary of pin names and reference number

def setup():
    global p_R, p_G, p_B
    print("Program is starting...")
    GPIO.setmode(GPIO.BOARD)
    for i in pins: #configure each pin as output of 3.3V
        GPIO.setup(pins[i],GPIO.OUT)
        GPIO.output(pins[i], GPIO.HIGH)
        
    #set frequency to 2 kHz
    p_R = GPIO.PWM(pins["pin_R"],2000)
    p_G = GPIO.PWM(pins["pin_G"],2000)
    p_B = GPIO.PWM(pins["pin_B"],2000)

    #initialize duty cycle as 0
    p_R.start(0)
    p_G.start(0)
    p_B.start(0)

#changes duty cycle for each colour
def setColor(r_val,g_val,b_val):
    p_R.ChangeDutyCycle(r_val)
    p_G.ChangeDutyCycle(g_val)
    p_B.ChangeDutyCycle(b_val)

def loop():
    while True: #changes duty cycle for each light to a random integer each iteration
        r = random.randint(0,100)
        g = random.randint(0,100)
        b = random.randint(0,100)
        setColor(r,g,b)
        print("r=%d,g=%d,b=%d" %(r,g,b))
        time.sleep(0.3)

def destroy(): #disables all GPIO ports, turns LEDs off
    p_R.stop()
    p_G.stop()
    p_B.stop()
    GPIO.cleanup()

#continually alternates colours of bulbs until Ctrl+C is pressed
if __name__ =="main":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        
