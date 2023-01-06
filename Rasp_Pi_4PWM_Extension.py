import RPi.GPIO as GPIO
import time
ledPin = 12
dutyControlButton = 11
startStopButton = 13
incrementing = True #state of whether duty cycle is increasing or decreasing
dc = 0 #duty cycle
dcChange = 25 #change in duty cycle

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(dutyControlPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(startStopButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(ledPin, GPIO.LOW)
    p = GPIO.PWM(ledPin, 1000) #frequency of analog wave is 1 kHz
    p.start(0) #set initial PWM duty cycle as 0


#disable PWM and GPIO pins
def destroy():
    p.stop()
    GPIO.output(ledPin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    print("Program is starting...")
    while True:
        GPIO.add_event_detect(startStopButton,GPIO.FALLING,callback=buttonEvent,bouncetime=300)
        if GPIO.event_detected(startStopButton):
            print("Start PWM")
            while True:
                GPIO.add_event_detect(dutyControlButton,GPIO.FALLING,callback=buttonEvent,bouncetime=300)
                if GPIO.event_detected(dutyControlButton):
                    if dc == 100:
                        incrementing = False
                    else if dc == 0:
                        incrementing = True
                    if incrementing:
                        dc = dc + dcChange
                    else:
                        dc = dc - dcChange
                    p.ChangeDutyCycle(dc)
                print("Duty Cycle: " + str(dc) + "%")
                if GPIO.event_detected(startStopButton):
                    print("Stop PWM")
                    break
    destroy()
                    
    
