import RPi.GPIO as GPIO
import time

relayPin = 11 #output high or low signal to relay
buttonPin = 12 #takes input from button
debounceTime = 50 #delay for reading button pressed state

#Initialization
def setup():
    print("Program is starting...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relayPin, GPIO.OUT) #initialize relay pin as output
    GPIO.setup(buttonPin, GPIO.IN) #initialize button pin as input

def loop():
    relayState = False #relay is initially at a low state, motor does not turn
    lastChangeTime = round(time.time()*1000)
    buttonState = GPIO.HIGH
    lastButtonState = GPIO.HIGH
    reading = GPIO.HIGH
    
    while True:
        reading = GPIO.input(buttonPin) #determines if the button is pressed or not
        
        if reading != lastButtonState:
            lastChangeTime = round(time.time()*1000)#determines when the button is pressed

        if((round(time.time()*1000)-lastChangeTime) > debounceTime): #detects when the button is pressed, delaying for 50 milliseconds
            if reading != buttonState:
                buttonState = reading

                if buttonState == GPIO.LOW: 
                    print("Button is pressed!")
                    relayState = not relayState #changes state of relay whenever button is pressed, impacting movement of motor
                    if relayState:
                        print("Turn on relay...")
                    else:
                        print("Turn off relay...")
                else:
                    print("Button is released!")
        GPIO.output(relayPin, relayState) #control relay
        lastButtonState = reading

def destroy(): #disable all ports
    GPIO.output(relayPin, GPIO.LOW)
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
