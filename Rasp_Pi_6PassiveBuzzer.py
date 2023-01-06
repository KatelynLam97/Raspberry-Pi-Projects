import RPi.GPIO as GPIO
import time
import math

buzzerPin = 11 #GPIO for buzzer
buttonPin = 12 #GPIO for switch

def setup():
    global p
    print("program is starting...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT) #set buzzer pin to output
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)#set pin to active high

    p = GPIO.PWM(buzzerPin, 1) #initialize PWM
    p.start(0)

def alertor():
    p.start(50) #change frequency based on sinewave (analog signal)
    for x in range(0,361):
        sinVal = math.sin(x*(math.pi/180.0))
        toneVal = 2000 + sinVal*500
        p.ChangeFrequency(toneVal)#change the frequency of the sound
        time.sleep(0.001)
        
def stopAlertor():
    p.stop()
    
def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW: #sound buzzer when switch is pressed
            alertor()
            print("buzzer on")
        else:
            stopAlertor()#stop sounding buzzer when switch is not pressed
            print("buzzer off")
            
def destroy(): #disable pins
    GPIO.output(buzzerPin,GPIO.LOW)
    GPIO.cleanup()

#main
#run until Ctrl+C is pressed
if__name__=="__main__":
    setup()
    try:
        loop
    except KeyboardInterrupt:
        destroy()
