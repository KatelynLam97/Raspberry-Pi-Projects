import RPi.GPIO as GPIO
import time
import Freenove_DHT as DHT

DHTPin = 11

def loop():
    dht = DHT.DHT(DHTPin)
    sumCnt = 0
    while(True):
        sumCnt += 1 #counts number of times data is read
        chk = dht.readDHT11() #reads temperature and humidity data from GPIO 17
        print("The sumCnt is %d, \tchk    :%d"%(sumCnt,chk))
        
        if(chk is dht.DHTLIB_OK): #Error check
            print("DHT11, OK!")

        elif(chk is dht.DHTLIB_ERROR_CHECKSUM):
            print("DHTLIB_ERROR_CHECKSUM!!")
        elif(chk is dht.DHTLIB_ERROR_TIMEOUT):
            print("DHTLIB_ERROR_TIMEOUT!")
        else:
            print("Other error!")

        print("Humidity: %.2f, \t Temperature: %.2f \n"%(dht.humidity,dht.temperature)) #print temperature and humidity data
        time.sleep(2)
        
if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()
