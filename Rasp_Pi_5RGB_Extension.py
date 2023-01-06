import RPi.GPIO as GPIO
import time
import random

pins = {"pin_R":11,"pin_G":12,"pin_B":13} #dictionary of pin names and reference number
ledPins = {"pin_LEDR":16, "pin_LEDG":18, "pin_LEDB":22} #dictionary of LED pins
dutyControlButton = 32
stopButton = 36
incrementing = True #state of whether duty cycle is increasing or decreasing
dc = 0 #duty cycle
dcChange = 25 #change in duty cycle

def setup():
    global p_R, p_G, p_B
    global p_LEDR, p_LEDG, p_LEDB
    print("Program is starting...")
    GPIO.setmode(GPIO.BOARD)
    
    for i in pins: #configure each pin as output of 3.3V
        GPIO.setup(pins[i],GPIO.OUT)
        GPIO.output(pins[i], GPIO.LOW)
        
    for j in ledPins: #configure each LED pin to output, off 
        GPIO.setup(ledPins[j],GPIO.OUT)
        GPIO.output(ledPins[j], GPIO.LOW)
    GPIO.setup(dutyControlButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(stopButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
    #set frequency to 2 kHz
    p_R = GPIO.PWM(pins["pin_R"],2000)
    p_G = GPIO.PWM(pins["pin_G"],2000)
    p_B = GPIO.PWM(pins["pin_B"],2000)
    p_LEDR = GPIO.PWM(ledPins["pin_LEDR"],2000)
    p_LEDG = GPIO.PWM(ledPins["pin_LEDG"],2000)
    p_LEDB = GPIO.PWM(ledPins["pin_LEDB"],2000)

    #initialize duty cycle as 0
    p_R.start(0)
    p_G.start(0)
    p_B.start(0)
    p_LEDR.start(0)
    p_LEDG.start(0)
    p_LEDB.start(0)

#changes duty cycle for each colour
def setColor(dutyCycle):
    p_R.ChangeDutyCycle(dutyCycle)
    p_G.ChangeDutyCycle(dutyCycle)
    p_B.ChangeDutyCycle(dutyCycle)
    p_LEDR.ChangeDutyCycle(dutyCycle)
    p_LEDG.ChangeDutyCycle(dutyCycle)
    p_LEDB.ChangeDutyCycle(dutyCycle)
    
#pwm routine
def pwmProcedure(channel):
    global dc
    global incrementing
    if dc == 100:
        incrementing = False
    elif dc == 0:
        incrementing = True
    if incrementing:
        dc = dc + dcChange
    else:
        dc = dc - dcChange
    setColor(dc)
    print("Duty Cycle: " + str(dc) + "%")



def destroy(): #disables all GPIO ports, turns LEDs off
    p_R.stop()
    p_G.stop()
    p_B.stop()
    GPIO.cleanup()

#changes duty cycle of RGB and three LEDs until stop button is pressed
if __name__ =="__main__":
    setup()
    GPIO.add_event_detect(dutyControlButton,GPIO.FALLING,callback=pwmProcedure,bouncetime=300) #increases duty cycle by 25% each time duty cycle button is pressed
    while GPIO.input(stopButton)==GPIO.HIGH: #ends program when stop button is pressed
        pass
    
    print("End program")
    destroy()
        
