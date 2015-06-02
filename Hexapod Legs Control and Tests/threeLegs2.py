from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)
pwm.setPWMFreq(60)

def frontRightSet():
    call("echo 1=200 > /dev/servoblaster", shell=True)
    pwm.setPWM(1,0,450) #right mid

def frontRightSpread():
    call("echo 1=150 > /dev/servoblaster", shell=True)
    pwm.setPWM(1,0,375) #right mid

def frontLeftSet():
    pwm.setPWM(2,0,340) #left mid
    pwm.setPWM(4,0,325) #left tip

def frontLeftSpread():
    pwm.setPWM(2,0,390) #left mid
    pwm.setPWM(4,0,420) #left tip

def middleRightSet():
    pwm.setPWM(7,0,500) #mid right
    pwm.setPWM(9,0,500) #right tip

def middleRightSpread():
    pwm.setPWM(7,0,475) #right mid
    pwm.setPWM(9,0,425) #right tip

def middleLeftSet():
    pwm.setPWM(8,0,325) #mid left
    pwm.setPWM(10,0,300) #left tip
	
def middleLeftSpread():
    pwm.setPWM(8,0,400) #left mid
    pwm.setPWM(10,0,420) #left tip

def backRightSet():
    pwm.setPWM(13,0,275) #right mid
    pwm.setPWM(15,0,550) #right tip
	
def backRightSpread():
    pwm.setPWM(13,0,200) #right mid
    pwm.setPWM(15,0,450) #right tip

def backLeftSet():
    pwm.setPWM(14,0,325) #left mid
    pwm.setPWM(12,0,300) #left tip

def backLeftSpread():
    pwm.setPWM(14,0,400) #left mid
    pwm.setPWM(12,0,350) #left tip

def rightSetStep():
    #move bases forward
    pwm.setPWM(3,0,525)
    pwm.setPWM(6,0,350)
    pwm.setPWM(11,0,400)
    time.sleep(1)
    #move legs
    frontRightSpread()
    backRightSpread()
    middleLeftSpread()
    time.sleep(1)
    frontRightSet()
    middleLeftSet()
    backRightSet()
    time.sleep(1)
#    setup()

def leftSetStep():
    #move bases forward
    pwm.setPWM(0,0,300) #set front left
    pwm.setPWM(5,0,500) #set middle right
    call("echo 4=90 > /dev/servoblaster", shell=True) #set back left
    time.sleep(1)
    #move legs
    frontLeftSpread()
    middleRightSpread()
    backLeftSpread()
    time.sleep(1)
    frontLeftSet()
    middleRightSet()
    backLeftSet()
    time.sleep(1)
#    setup()

def setup():
    pwm.setPWM(3,0,350)
    pwm.setPWM(6,0,450)
    pwm.setPWM(11,0,300)
    frontRightSet()
    middleLeftSet()
    backRightSet()
    pwm.setPWM(0,0,500) #front left
    pwm.setPWM(5,0,400) #middle right
    call("echo 4=130 > /dev/servoblaster", shell=True) #set back left
    frontLeftSet()
    middleRightSet()
    backLeftSet()

setup()
while True:
    time.sleep(1)
    rightSetStep()
    time.sleep(1)
    leftSetStep()
    time.sleep(1)
    
        
