import RPi.GPIO as GPIO
import time
OFFSE_DUTY = 0.5 #pulse offset
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY #minimum angle pulse offset
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY #maximum angle pulse offset
servoPin = 12 #output pin for servo

def map(value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh-toLow)*(value-fromLow)/(fromHigh-fromLow) + toLow

#initialization
def setup():
    global p

    #set servo pin to output and a low value
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)
    GPIO.output(servoPin, GPIO.LOW)

    #define duty cycle to be 50Hz for servo pin
    p = GPIO.PWM(servoPin, 50)
    p.start(0)

def servoWrite(angle): #rotates servo to a given angle by mapping with duty cycle
    if(angle < 0):
        angle = 0
    elif(angle > 180):
        angle = 180
    p.ChangeDutyCycle(map(angle,0,100,SERVO_MIN_DUTY,SERVO_MAX_DUTY))

def loop():
    while True:
        for dc in range(0,180,1): #rotate servo from 0 to 180 degrees
            servoWrite(dc)
            time.sleep(0.001)
        time.sleep(0.5)

        for dc in range(180,-1,-1): #rotate servo from 180 degrees to 0 
            servoWrite(dc)
            time.sleep(0.001)
        time.sleep(0.5)

#disable GPIO pins
def destroy():
    p.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    print("Program is starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
