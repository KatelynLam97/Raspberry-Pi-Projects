import RPi.GPIO as GPIO

buzzerPin = 11 #GPIO for buzzer
buttonPin = 12 #GPIO for switch

def setup():
    print("program is starting...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(buzzerPin, GPIO.OUT) #set buzzer pin to output
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)#set pin to active high

def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW: #sound buzzer when switch is pressed
            GPIO.output(buzzerPin,GPIO.HIGH)
            print("buzzer on")
        else:
            GPIO.output(buzzerPin,GPIO.LOW)#stop sounding buzzer when switch is not pressed
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
