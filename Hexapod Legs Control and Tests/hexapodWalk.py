#functions to make the hexapod robot walk backward, forward, rotate left
#and right

from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)
pwm.setPWMFreq(60)

#base positions
frontRightForward = 350
frontLeftForward = 500
middleRightForward = 340
middleLeftForward = 425
backRightForward = 350
backLeftForward = 90

frontRightStraight = 300
frontLeftStraight = 550
middleRightStraight = 300
middleLeftStraight = 450
backRightStraight = 300
backLeftStraight = 110

frontRightBack = 250
frontLeftBack = 575
middleRightBack = 275
middleLeftBack = 475
backRightBack = 250
backLeftBack = 130

def frontRightSet(): #front right leg standing up
    call("echo 1=200 > /dev/servoblaster", shell=True)
    pwm.setPWM(1,0,450) #right mid

def frontRightSpread(): #front right leg stretching
    #call("echo 1=150 > /dev/servoblaster", shell=True)
    pwm.setPWM(1,0,400) #right mid

def frontLeftSet(): #front left leg standing up
    pwm.setPWM(2,0,340) #left mid
    pwm.setPWM(4,0,325) #left tip

def frontLeftSpread(): #front left leg spreading
    pwm.setPWM(2,0,390) #left mid
    #pwm.setPWM(4,0,420) #left tip

def middleRightSet(): #middle right leg standing up
    pwm.setPWM(7,0,500) #mid right
    pwm.setPWM(9,0,500) #right tip

def middleRightSpread(): #middle right leg stretching
    pwm.setPWM(7,0,450) #right mid
    #pwm.setPWM(9,0,425) #right tip

def middleLeftSet(): #middle left leg standing up
    pwm.setPWM(8,0,325) #mid left
    pwm.setPWM(10,0,300) #left tip
	
def middleLeftSpread(): #middle left leg stretching
    pwm.setPWM(8,0,400) #left mid
    #pwm.setPWM(10,0,420) #left tip

def backRightSet(): #back right leg standing up
    pwm.setPWM(13,0,275) #right mid
    pwm.setPWM(15,0,550) #right tip
	
def backRightSpread(): #back right leg stretching
    pwm.setPWM(13,0,200) #right mid
    #pwm.setPWM(15,0,450) #right tip

def backLeftSet(): #back left leg standing up
    pwm.setPWM(14,0,325) #left mid
    pwm.setPWM(12,0,300) #left tip

def backLeftSpread(): #back left leg stretching
    pwm.setPWM(14,0,400) #left mid
    #pwm.setPWM(12,0,350) #left tip

#left set is front left, mid right, back left.
#right set is front right, mid left, back right
    
def basesRightForward(): #right set forward, left set back
    pwm.setPWM(3,0,frontRightForward) #front right leg forward
    pwm.setPWM(6,0,middleLeftForward) #middle left forward
    pwm.setPWM(11,0,backRightForward) #back right forward
    pwm.setPWM(0,0,frontLeftBack) #front left leg back
    pwm.setPWM(5,0,middleRightBack) #middle right leg back
    call("echo 4=" + str(backLeftBack) +  "> /dev/servoblaster", shell=True) #back left

def basesLeftForward(): #left set forward, right set back
    pwm.setPWM(0,0,frontLeftForward) #set front left
    pwm.setPWM(5,0,middleRightForward) #set middle right
    call("echo 4=" + str(backLeftForward) + "> /dev/servoblaster", shell=True) #set back left
    pwm.setPWM(3,0,frontRightBack) #front right leg back
    pwm.setPWM(6,0,middleLeftBack) #middle left leg back
    pwm.setPWM(11,0,backRightBack) #back right leg back

def rightSetSpread(): #right set stretching
    frontRightSpread()
    backRightSpread()
    middleLeftSpread()

def leftSetSpread(): #left set stretching
    frontLeftSpread()
    backLeftSpread()
    middleRightSpread()

def rightSet(): #right set standing up
    frontRightSet()
    middleLeftSet()
    backRightSet()

def leftSet(): #left set standing up
    frontLeftSet()
    middleRightSet()
    backLeftSet()
    
def setup(): #all legs to the sides
    pwm.setPWM(3,0,frontRightStraight) #front right base
    pwm.setPWM(6,0,middleLeftStraight) #middle left base
    pwm.setPWM(11,0,backRightStraight) #back right base
    frontRightSet()
    middleLeftSet()
    backRightSet()
    pwm.setPWM(0,0,frontLeftStraight) #front left
    pwm.setPWM(5,0,middleRightStraight) #middle right
    call("echo 4=" + str(backLeftStraight) + "> /dev/servoblaster", shell=True) #set back left
    frontLeftSet()
    middleRightSet()
    backLeftSet()
    
#one step forward
def walkForward(): 
    rightSetSpread()
    time.sleep(1)
    basesLeftForward() #kind of counter-intuitive
    time.sleep(1)
    rightSet()
    time.sleep(1)
    leftSetSpread()
    time.sleep(1)
    basesRightForward()
    time.sleep(1)
    leftSet()
    time.sleep(1)

#one step back
def walkBackwards(): 
    rightSetSpread()
    time.sleep(1)
    basesRightForward() #again kind of counter-intuitive
    time.sleep(1)
    rightSet()
    time.sleep(1)
    leftSetSpread()
    time.sleep(1)
    basesLeftForward()
    time.sleep(1)
    leftSet()
    time.sleep(1)
    

#turn right in steps
def rotateRight():
    frontRightSpread()
    backLeftSpread()
    pwm.setPWM(3,0,frontRightForward) #right front forward
    call("echo 4=" + str(backLeftBack) + "> /dev/servoblaster", shell=True) #left back backward
    time.sleep(1)
    frontRightSet()
    backLeftSet()
    time.sleep(1)

    frontLeftSpread()
    backRightSpread()
    pwm.setPWM(0,0,frontLeftBack) #left front back
    pwm.setPWM(11,0,backRightForward) #right back forward
    time.sleep(1)
    frontLeftSet()
    backRightSet()
    time.sleep(1)

    middleRightSpread()
    middleLeftSpread()
    pwm.setPWM(0,0,frontLeftForward)#left front forward
    pwm.setPWM(3,0,frontRightBack)#right front back
    pwm.setPWM(11,0,backRightBack) #right back back
    call("echo 4=" + str(backLeftForward) + ">/dev/servoblaster", shell=True) #left back forward
    time.sleep(1)
    middleRightSet()
    middleLeftSet()
    time.sleep(1)

#turn left in steps
def rotateLeft():
    frontRightSpread()
    backLeftSpread()
    pwm.setPWM(3,0,frontRightBack) #right front back
    call("echo 4=" + str(backLeftForward) + "> /dev/servoblaster", shell=True) #left back forward
    time.sleep(1)
    frontRightSet()
    backLeftSet()
    time.sleep(1)

    frontLeftSpread()
    backRightSpread()
    pwm.setPWM(0,0,frontLeftForward) #left front forward
    pwm.setPWM(11,0,backRightBack) #right back backward
    time.sleep(1)
    frontLeftSet()
    backRightSet()
    time.sleep(1)

    middleRightSpread()
    middleLeftSpread()
    pwm.setPWM(0,0,frontLeftBack)#left front back
    pwm.setPWM(3,0,frontRightForward)#right front forward
    pwm.setPWM(11,0,backRightForward) #right back forward
    call("echo 4=" + str(backLeftBack) + ">/dev/servoblaster", shell=True) #left back back
    time.sleep(1)
    middleRightSet()
    middleLeftSet()
    time.sleep(1)

setup()
time.sleep(3)
rotateRight()
time.sleep(1)
setup()
time.sleep(1)
walkForward()
time.sleep(1)
setup()
time.sleep(1)
walkBackwards()
time.sleep(1)
setup()
time.sleep(1)
rotateLeft()
time.sleep(1)
setup()
time.sleep(1)
