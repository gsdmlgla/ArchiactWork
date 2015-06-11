#improved walking sequences, before being remote controlled
#should I not have these be sequences somehow?

from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)
pwm.setPWMFreq(60)

leftBaseSides = 500
rightBaseSides = 300
leftBaseForward = 450
rightBaseForward = 350
leftBaseBack = 550
rightBaseBack = 250

rightMidSpread = 450
leftMidSpread = 350

rightMidNarrow = 500
leftMidNarrow = 300

rightTipSpread = 400
leftTipSpread = 400
backRightTipSpread = 150
backLeftTipSpread = 150

rightTipNarrow = 500
leftTipNarrow = 300
backRightTipNarrow = 200
backLeftTipNarrow = 100

pwm.setPWM(0,0,leftBaseSides)
pwm.setPWM(1,0,rightBaseSides)
pwm.setPWM(6,0,leftBaseSides)
pwm.setPWM(7,0,rightBaseSides)
pwm.setPWM(12,0,leftBaseSides)
pwm.setPWM(13,0,rightBaseSides)

def spread(): #spread out positions for all legs
    pwm.setPWM(2,0,leftMidSpread)
    pwm.setPWM(3,0,rightMidSpread)
    pwm.setPWM(4,0,leftTipSpread)
    pwm.setPWM(5,0,rightTipSpread)

    pwm.setPWM(8,0,leftMidSpread)
    pwm.setPWM(9,0,rightMidSpread)
    pwm.setPWM(10,0,leftTipSpread)
    pwm.setPWM(11,0,rightTipSpread)

    pwm.setPWM(14,0,leftMidSpread)
    pwm.setPWM(15,0,rightMidSpread)
    call("echo 1=" + str(backLeftTipSpread) + ">/dev/servoblaster", shell=True)
    call("echo 4=" + str(backRightTipSpread) + ">/dev/servoblaster", shell=True)

def narrow(): #narrowed positions for all legs
    pwm.setPWM(2,0,leftMidNarrow)
    pwm.setPWM(3,0,rightMidNarrow)
    pwm.setPWM(4,0,leftTipNarrow)
    pwm.setPWM(5,0,rightTipNarrow)

    pwm.setPWM(8,0,leftMidNarrow)
    pwm.setPWM(9,0,rightMidNarrow)
    pwm.setPWM(10,0,leftTipNarrow)
    pwm.setPWM(11,0,rightTipNarrow)

    pwm.setPWM(14,0,leftMidNarrow)
    pwm.setPWM(15,0,rightMidNarrow)
    call("echo 1=" + str(backLeftTipNarrow) + ">/dev/servoblaster", shell=True)
    call("echo 4=" + str(backRightTipNarrow) + ">/dev/servoblaster", shell=True)

def frontRightSet(): #front right leg standing up
    pwm.setPWM(3,0,rightMidNarrow)
    pwm.setPWM(5,0,rightTipNarrow) 

def frontRightSpread(): #front right leg stretching
    pwm.setPWM(3,0,rightMidSpread)
    pwm.setPWM(5,0,rightTipSpread) 

def frontLeftSet(): #front left leg standing up
    pwm.setPWM(2,0,leftMidNarrow) #left mid
    pwm.setPWM(4,0,leftTipNarrow) #left tip

def frontLeftSpread(): #front left leg spreading
    pwm.setPWM(2,0,leftMidSpread) #left mid
    pwm.setPWM(4,0,leftTipSpread) #left tip

def middleRightSet(): #middle right leg standing up
    pwm.setPWM(9,0,rightMidNarrow)
    pwm.setPWM(11,0,rightTipNarrow)

def middleRightSpread(): #middle right leg stretching
    pwm.setPWM(9,0,rightMidSpread)
    pwm.setPWM(11,0,rightTipSpread)

def middleLeftSet(): #middle left leg standing up
    pwm.setPWM(8,0,leftMidNarrow) #left mid
    pwm.setPWM(10,0,leftTipNarrow) #left tip
	
def middleLeftSpread(): #middle left leg stretching
    pwm.setPWM(8,0,leftMidSpread) #left mid
    pwm.setPWM(10,0,leftTipSpread) #left tip

def backRightSet(): #back right leg standing up
    pwm.setPWM(15,0,rightMidNarrow)
    call("echo 4=" + str(backRightTipNarrow) + ">/dev/servoblaster",shell=True)
	
def backRightSpread(): #back right leg stretching
   pwm.setPWM(9,0,rightMidSpread)
   call("echo 4=" + str(backRightTipSpread) + ">/dev/servoblaster",shell=True)

def backLeftSet(): #back left leg standing up
    pwm.setPWM(14,0,leftMidNarrow)
    call("echo 1=" + str(backLeftTipNarrow) + ">/dev/servoblaster",shell=True)

def backLeftSpread(): #back left leg stretching
    pwm.setPWM(9,0,leftMidSpread)
    call("echo 1=" + str(backLeftTipSpread) + ">/dev/servoblaster",shell=True)

#right set is the front right, middle left and back right legs
#left set is the front left, middle right and back left legs
def rightSetForward(): #right set forward, left set back
    pwm.setPWM(0,0,leftBaseBack)
    pwm.setPWM(7,0,rightBaseBack)
    pwm.setPWM(12,0,leftBaseBack)
    pwm.setPWM(1,0,rightBaseForward)
    pwm.setPWM(6,0,leftBaseForward)
    pwm.setPWM(13,0,rightBaseForward)

def leftSetForward(): #left set forward, right set back
    pwm.setPWM(0,0,leftBaseForward)
    pwm.setPWM(7,0,rightBaseForward)
    pwm.setPWM(12,0,leftBaseForward)
    pwm.setPWM(1,0,rightBaseBack)
    pwm.setPWM(6,0,leftBaseBack)
    pwm.setPWM(13,0,rightBaseBack)

#set and spread for each set
    
def rightSetSpread():
    frontRightSpread()
    backRightSpread()
    middleLeftSpread()

def leftSetSpread():
    frontLeftSpread()
    backLeftSpread()
    middleRightSpread()

def rightSetSet():
    frontRightSet()
    middleLeftSet()
    backRightSet()

def leftSetSet(): #left set standing up
    frontLeftSet()
    middleRightSet()
    backLeftSet()

def walkForward():
    rightSetSpread()
    time.sleep(0/5)
    rightSetForward() 
    time.sleep(0.5)
    rightSetSet()
    time.sleep(0.5)
    leftSetSpread()
    time.sleep(0.5)
    leftSetForward()
    time.sleep(0.5)
    leftSetSet()
    time.sleep(0.5)

def walkBackwards():
    rightSetSpread()
    time.sleep(0.5)
    leftSetForward() #again kind of counter-intuitive
    time.sleep(0.5)
    rightSetSet()
    time.sleep(0.5)
    leftSetSpread()
    time.sleep(0.5)
    rightSetForward()
    time.sleep(0.5)
    leftSetSet()
    time.sleep(0.5)

def rotateLeft():
    frontRightSpread()
    backLeftSpread()
    pwm.setPWM(1,0,rightBaseForward) #right front forward
    pwm.setPWM(12,0,leftBaseBack)
    time.sleep(0.5)
    frontRightSet()
    backLeftSet()
    time.sleep(0.5)

    frontLeftSpread()
    backRightSpread()
    pwm.setPWM(0,0,leftBaseBack) #left front back
    pwm.setPWM(12,0,leftBaseBack) #right back forward
    time.sleep(0.5)
    frontLeftSet()
    backRightSet()
    time.sleep(0.5)

    middleRightSpread()
    middleLeftSpread()
    pwm.setPWM(0,0,leftBaseForward)#left front forward
    pwm.setPWM(1,0,rightBaseBack)#right front back
    pwm.setPWM(13,0,rightBaseBack) #right back back
    pwm.setPWM(12,0,leftBaseForward)
    time.sleep(0.5)
    middleRightSet()
    middleLeftSet()
    time.sleep(0.5)

def rotateRight():
    frontRightSpread()
    backLeftSpread()
    pwm.setPWM(1,0,rightBaseBack) #right front back
    pwm.setPWM(12,0,leftBaseForward) #back left forward
    time.sleep(0.5)
    frontRightSet()
    backLeftSet()
    time.sleep(0.5)

    frontLeftSpread()
    backRightSpread()
    pwm.setPWM(0,0,leftBaseForward) #left front forward
    pwm.setPWM(13,0,rightBaseBack) #right back backward
    time.sleep(0.5)
    frontLeftSet()
    backRightSet()
    time.sleep(0.5)

    middleRightSpread()
    middleLeftSpread()
    pwm.setPWM(0,0,leftBaseBack)#left front back
    pwm.setPWM(1,0,rightBaseForward)#right front forward
    pwm.setPWM(13,0,rightBaseForward) #right back forward
    pwm.setPWM(12,0,leftBaseBack)
    time.sleep(0.5)
    middleRightSet()
    middleLeftSet()
    time.sleep(0.5)


narrow()
time.sleep(1)
while True:
    rotateRight()
