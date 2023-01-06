import MPU6050
import time

mpu = MPU6050.MPU6050() #instantiate module to read from MPU6050
accel = [0]*3 #array of acceleration in 3 axis
gyro = [0]*3#array of axis of roation in 3 axis

def setup():
    mpu.dmp_initialize()#initialize MPU6050 module

def loop():
    while(True):
        accel = mpu.get_acceleration() #determine acceleration
        gyro = mpu.get_rotation()#determine rotation
        print("a/g:%d\t%d\t%d\t%d\t%d\t%d"
              %(accel[0],accel[1],accel[2],gyro[0],gyro[1],gyro[2])) #display data read from sensor
        print("a/g:%.2f g\t%.2f g\t&.2f g\t%.2f d/s\t%.2f d/s\t%.2fd/s"
              %(accel[0]/16384.0,accel[1]/16384.0,accel[2]/16384.0,
                gyro[0]/131.0,gyro[1]/131.0,gyro[2]/131.0)) #display angular velocity and acceleration due to gravity
        time.sleep(0.1)

if __name__ == "__main__":
    print("Program is starting...")
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        pass
