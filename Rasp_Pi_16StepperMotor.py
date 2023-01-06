import RPi.GPIO as GPIO
import time

motorPins = (12,16,18,22) #ABCD pins of stepper motor
CCWStep = (0x01, 0x02, 0x04, 0x08) #address for counter clockwise step
CWStep = (0x08, 0x04, 0x02, 0x01) #address for clockwise step

#initialization
def setup():
    print("Program is starting...")
    GPIO.setmode(GPIO.BOARD)
    for pin in motorPins:
        GPIO.setup(pin, GPIO.OUT)

#takes four steps either to move clockwise or anticlockwise
def moveOnePeriod(direction, ms):
    for j in range(0,4,1):
        for i in range(0,4,1):
            if(direction == 1): #turn motor clockwise
                GPIO.output(motorPins[i], ((CWStep[j]==1<<i) and GPIO.HIGH or GPIO.LOW))
            else:
                GPIO.output(motorPins[i], ((CCWStep[j]==1<<i) and GPIO.HIGH or GPIO.LOW))
            if(ms < 3): #max motor speed
                ms = 3
            time.sleep(ms*0.001) 

#moves given number of steps
def moveSteps(direction, ms, steps):
    for i in range(steps):
        moveOnePeriod(direction, ms)

#stops motor
def motorStop():
    for i in range(0,4,1):
        GPIO.output(motorPins[i], GPIO.LOW)

#turns motor 360 degrees clockwise and counter clockwise
def loop():
    while True:
        moveSteps(1,3,512)
        time.sleep(0.5)
        moveSteps(0,3,512)
        time.sleep(0.5)

#disable pins
def destroy:
    GPIO.cleanup()

#main
#program terminates when Ctrl+C is pressed
if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
