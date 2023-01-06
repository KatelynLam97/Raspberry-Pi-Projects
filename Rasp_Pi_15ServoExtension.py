import RPi.GPIO as GPIO
import time
OFFSE_DUTY = 0.5 #pulse offset
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY #minimum angle pulse offset
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY #maximum angle pulse offset
servoPin = 12 #output pin for servo
button0 = 32
button45 = 36
button90 = 38
button180 = 40

def map(value, fromLow, fromHigh, toLow, toHigh):
    return (toHigh-toLow)*(value-fromLow)/(fromHigh-fromLow) + toLow

#initialization
def setup():
    global p

    #set servo pin to output and a low value
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin, GPIO.OUT)
    GPIO.output(servoPin, GPIO.LOW)

    #initialize button pins to input
    GPIO.setup(button0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button45, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button90, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button180, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    #define duty cycle to be 50Hz for servo pin
    p = GPIO.PWM(servoPin, 50)
    p.start(0)

def servoWrite(angle): #rotates servo to a given angle by mapping with duty cycle
    p.ChangeDutyCycle(map(angle,0,100,SERVO_MIN_DUTY,SERVO_MAX_DUTY))
    time.sleep(0.001)

def loop:
    GPIO.add_event_detect(button0,GPIO.FALLING, callback = servoWrite(0), bouncetime = 300)
    GPIO.add_event_detect(button0,GPIO.FALLING, callback = servoWrite(45), bouncetime = 300)
    GPIO.add_event_detect(button0,GPIO.FALLING, callback = servoWrite(90), bouncetime = 300)
    GPIO.add_event_detect(button0,GPIO.FALLING, callback = servoWrite(180), bouncetime = 300)

    while True:
        pass

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
