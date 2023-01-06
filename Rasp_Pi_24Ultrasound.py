import RPi.GPIO as GPIO
import time

trigPin = 16
echoPin = 18
MAX_DISTANCE = 220 #maximum measured distance: 220cm
timeOut = MAX_DISTANCE * 60 #throws error if no signal is received beyond expected time for max distance

def pulseIn(pin, level, timeOut):
    t0 = time.time()
    while(GPIO.input(pin) != level): #continue waiting for HIGH signal to denote finish distance measurement
        if((time.time()-t0) < timeOut * 0.000001):
            return();

    t0 = time.time()
    while(GPIO.input(pin) == level): #measure duration of HIGH signal (receiver)
        if((time.time() - t0) > timeOut*0.000001):
            return();
        pulseTime = (time.time() - t0)*0.000001
        return pulseTime #return duration of HIGH signal

def getSonar():
    GPIO.output(trigPin, GPIO.HIGH) #time pulse to start measuring echo
    time.sleep(0.00001)
    GPIO.output(trigPin, GPIO.LOW)
    pingTime = pulseIn(echoPin, GPIO.HIGH, timeOut) #receive duration of sound wave
    distance = pingTime * 340.0/2.0/1000.0 #calculate distance
    return distance;

#initialize pins
def setup():
    print("Program is starting...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trigPin, GPIO.OUT)
    GPIO.setup(echoPin, GPIO.IN)

def loop():
    while True:
        distance = getSonar() #update distance measurement every second
        print("The distance is : %.2f cm"%(distance))
        time.sleep(1)

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup() #disable GPIO pins
