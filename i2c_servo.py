'''import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=8)

kit.servo[0].angle = 180
kit.continuous_servo[1].throttle = 1
time.sleep(1)
kit.continuous_servo[1].throttle = -1
time.sleep(1)
kit.servo[0].angle = 0
kit.continuous_servo[1].throttle = 0'''




from adafruit_servokit import ServoKit
from time import sleep
kit = ServoKit(channels=8)


def servo1(i):
    for a in range(0,180):
        kit.servo[i].angle = a
        sleep(0.008)
        
    for a in range(179,1,-1):
        kit.servo[i].angle = a
        sleep(0.008)
    '''
def servo2():
    for a in range(0,180):
        kit.servo[1].angle = a
        sleep(0.008)
        
    for a in range(179,1,-1):
        kit.servo[1].angle = a
        sleep(0.008)
        
def servo3():
    for a in range(0,180):
        kit.servo[2].angle = a
        sleep(0.008)
        
    for a in range(179,1,-1):
        kit.servo[2].angle = a
        sleep(0.008)
        
def servo4():
    for a in range(0,180):
        kit.servo[3].angle = a
        sleep(0.008)
        
    for a in range(179,1,-1):
        kit.servo[3].angle = a
        sleep(0.008)
        '''
        
while True:
    servo1(1)
    '''
    servo2(2)
    servo3()
    servo4()'''