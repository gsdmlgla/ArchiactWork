from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import pygame
import time

#Gamepad settings
axisUpDown = 1
axisUpDownInverted = True #I think this should be true
axisLeftRight = 3
axisLeftRightInverted = False
interval = 0.1

#Setup pygame and states
global hadEvent
global moveForward
global moveBackward
global moveLeft
global moveRight
global previousMove
hadEvent = True
moveForward = False
moveBackward = False
moveLeft = False
moveRight = False
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

#I2C init
pwm = PWM(0x40)
pwm.setPWMFreq(60)

#Constants (servo PWM values). Servo positions:
#FRONT: 0=left base, 1=right base, 2=left mid, 3=right mid, 4=left tip, 5=right tip
#MIDDLE: 6=left base, 7=right base, 8=left mid, 9=right mid, 10=left tip, 11=right tip
#BACK: 12=left base, 13=right base, 14=left mid, 15=right mid, PIN1=left tip, PIN4=right tip
SideFLB=550
SideFRB=250
SideMLB=450
SideMRB=300
SideBLB=400
SideBRB=300

BackFLB=580
BackFRB=220
BackMLB=480
BackMRB=270
BackBLB=430
BackBRB=270

ForwardFLB=520
ForwardFRB=280
ForwardMLB=420
ForwardMRB=330
ForwardBLB=370
ForwardBRB=330

rightMidSpread = 550
leftMidSpread = 250

rightMidNarrow = 500
leftMidNarrow = 300

rightTip = 500
leftTip = 300
backRightTip = 200
backLeftTip = 100

#Spreads out all six legs
def spread():
    pwm.setPWM(0,0,SideFLB)
    pwm.setPWM(1,0,SideFRB)
    pwm.setPWM(6,0,SideMLB)
    pwm.setPWM(7,0,SideMRB)
    pwm.setPWM(12,0,SideBLB)
    pwm.setPWM(13,0,SideBRB)
    
    pwm.setPWM(2,0,leftMidSpread)
    pwm.setPWM(3,0,rightMidSpread)
    pwm.setPWM(4,0,leftTip)
    pwm.setPWM(5,0,rightTip)

    pwm.setPWM(8,0,leftMidSpread)
    pwm.setPWM(9,0,rightMidSpread)
    pwm.setPWM(10,0,leftTip)
    pwm.setPWM(11,0,rightTip)

    pwm.setPWM(14,0,leftMidSpread)
    pwm.setPWM(15,0,rightMidSpread)
    call("echo 1=" + str(backLeftTip) + ">/dev/servoblaster", shell=True)
    call("echo 4=" + str(backRightTip) + ">/dev/servoblaster", shell=True)

#Narrows all six legs. This should be set before it starts walking.
def narrow():
    pwm.setPWM(0,0,SideFLB)
    pwm.setPWM(1,0,SideFRB)
    pwm.setPWM(6,0,SideMLB)
    pwm.setPWM(7,0,SideMRB)
    pwm.setPWM(12,0,SideBLB)
    pwm.setPWM(13,0,SideBRB)

    pwm.setPWM(2,0,leftMidNarrow)
    pwm.setPWM(3,0,rightMidNarrow)
    pwm.setPWM(4,0,leftTip)
    pwm.setPWM(5,0,rightTip)

    pwm.setPWM(8,0,leftMidNarrow)
    pwm.setPWM(9,0,rightMidNarrow)
    pwm.setPWM(10,0,leftTip)
    pwm.setPWM(11,0,rightTip)

    pwm.setPWM(14,0,leftMidNarrow)
    pwm.setPWM(15,0,rightMidNarrow)
    call("echo 1=" + str(backLeftTip) + ">/dev/servoblaster", shell=True)
    call("echo 4=" + str(backRightTip) + ">/dev/servoblaster", shell=True)

def frontRightSet(): #front right leg standing up
    pwm.setPWM(3,0,rightMidNarrow)
    pwm.setPWM(5,0,rightTip) 

def frontRightSpread(): #front right leg stretching
    pwm.setPWM(3,0,rightMidSpread)
    pwm.setPWM(5,0,rightTip) 

def frontLeftSet(): #front left leg standing up
    pwm.setPWM(2,0,leftMidNarrow) #left mid
    pwm.setPWM(4,0,leftTip) #left tip

def frontLeftSpread(): #front left leg spreading
    pwm.setPWM(2,0,leftMidSpread) #left mid
    pwm.setPWM(4,0,leftTip) #left tip

def middleRightSet(): #middle right leg standing up
    pwm.setPWM(9,0,rightMidNarrow)
    pwm.setPWM(11,0,rightTip)

def middleRightSpread(): #middle right leg stretching
    pwm.setPWM(9,0,rightMidSpread)
    pwm.setPWM(11,0,rightTip)

def middleLeftSet(): #middle left leg standing up
    pwm.setPWM(8,0,leftMidNarrow) #left mid
    pwm.setPWM(10,0,leftTip) #left tip
	
def middleLeftSpread(): #middle left leg stretching
    pwm.setPWM(8,0,leftMidSpread) #left mid
    pwm.setPWM(10,0,leftTip) #left tip

def backRightSet(): #back right leg standing up
    pwm.setPWM(15,0,rightMidNarrow)
    call("echo 4=" + str(backRightTip) + ">/dev/servoblaster",shell=True)
	
def backRightSpread(): #back right leg stretching
   pwm.setPWM(15,0,rightMidSpread)
   call("echo 4=" + str(backRightTip) + ">/dev/servoblaster",shell=True)

def backLeftSet(): #back left leg standing up
    pwm.setPWM(14,0,leftMidNarrow)
    call("echo 1=" + str(backLeftTip) + ">/dev/servoblaster",shell=True)

def backLeftSpread(): #back left leg stretching
    pwm.setPWM(14,0,leftMidSpread)
    call("echo 1=" + str(backLeftTip) + ">/dev/servoblaster",shell=True)

#Right set is front right, mid left, back right
#Left set is front left, mid right, back left
    
def rightSetForward(): #right set forward, left set back
    pwm.setPWM(0,0,BackFLB)
    pwm.setPWM(7,0,BackMRB)
    pwm.setPWM(12,0,BackBLB)
    pwm.setPWM(1,0,ForwardFRB)
    pwm.setPWM(6,0,ForwardMLB)
    pwm.setPWM(13,0,ForwardBRB)

def leftSetForward(): #left set forward, right set back
    pwm.setPWM(0,0,ForwardFLB)
    pwm.setPWM(7,0,ForwardMRB)
    pwm.setPWM(12,0,ForwardBLB)
    pwm.setPWM(1,0,BackFRB)
    pwm.setPWM(6,0,BackMLB)
    pwm.setPWM(13,0,BackBRB)

def rightSetSpread(): #Spread legs on right set
    frontRightSpread()
    backRightSpread()
    middleLeftSpread()

def leftSetSpread(): #Spread legs on left set
    frontLeftSpread()
    backLeftSpread()
    middleRightSpread()

def rightSetSet(): #Narrow legs on right set
    frontRightSet()
    middleLeftSet()
    backRightSet()

def leftSetSet(): #Narrow legs on left set
    frontLeftSet()
    middleRightSet()
    backLeftSet()

def walkForwardRightStep(): #Right set moves to walk forward
    rightSetSpread()
    #time.sleep(0.5)
    rightSetForward() 
    time.sleep(0.5)
    rightSetSet()
    #time.sleep(0.5)

def walkForwardLeftStep(): #Left set moves to walk forward
    leftSetSpread()
    #time.sleep(0.5)
    leftSetForward()
    time.sleep(0.5)
    leftSetSet()
    #time.sleep(0.5)

def walkBackwardsRightStep(): #Right set moves to walk backward
    rightSetSpread()
    #time.sleep(0.5)
    leftSetForward()
    time.sleep(0.5)
    rightSetSet()
    #time.sleep(0.5)

def walkBackwardsLeftStep(): #Left set moves to walk backward
    leftSetSpread()
    #time.sleep(0.5)
    rightSetForward()
    time.sleep(0.5)
    leftSetSet()
    #time.sleep(0.5)

def rotateLeft(): #Rotates the spider right in small steps
    frontRightSpread()
    backLeftSpread()
    pwm.setPWM(1,0,ForwardFRB) #right front forward
    pwm.setPWM(12,0,BackBLB)
    time.sleep(0.5)
    frontRightSet()
    backLeftSet()
    time.sleep(0.5)

    frontLeftSpread()
    backRightSpread()
    pwm.setPWM(0,0,BackFLB) #left front back
    pwm.setPWM(13,0,ForwardBRB) #right back forward
    time.sleep(0.5)
    frontLeftSet()
    backRightSet()
    time.sleep(0.5)

    middleRightSpread()
    middleLeftSpread()
    pwm.setPWM(0,0,ForwardFLB)#left front forward
    pwm.setPWM(1,0,BackFRB)#right front back
    pwm.setPWM(13,0,BackBRB) #right back back
    pwm.setPWM(12,0,ForwardBLB)
    time.sleep(0.5)
    middleRightSet()
    middleLeftSet()
    time.sleep(0.5)

def rotateRight(): #Rotates the spider left in small steps
    frontRightSpread()
    backLeftSpread()
    pwm.setPWM(1,0,BackFRB) #right front back
    pwm.setPWM(12,0,ForwardBLB)
    time.sleep(0.5)
    frontRightSet()
    backLeftSet()
    time.sleep(0.5)

    frontLeftSpread()
    backRightSpread()
    pwm.setPWM(0,0,ForwardFLB) #left front forward
    pwm.setPWM(13,0,BackBRB) #right back backward
    time.sleep(0.5)
    frontLeftSet()
    backRightSet()
    time.sleep(0.5)
    
    middleRightSpread()
    middleLeftSpread()
    pwm.setPWM(0,0,BackFLB)#left front back
    pwm.setPWM(1,0,ForwardFRB)#right front forward
    pwm.setPWM(13,0,ForwardBRB) #right back forward
    pwm.setPWM(12,0,BackBLB)
    time.sleep(0.5)
    middleRightSet()
    middleLeftSet()
    time.sleep(0.5)

def PygameHandler(events): #Gets joystick values and translates it to a movement
    global hadEvent
    global moveForward
    global moveBackward
    global moveLeft
    global moveRight
    global moveQuit
    #handle each event
    for event in events:
        if event.type == pygame.JOYAXISMOTION:
            hadEvent = True
            upDown = joystick.get_axis(axisUpDown)
            leftRight = joystick.get_axis(axisLeftRight)
            print(upDown)
            print(leftRight)
            if axisUpDownInverted:
                upDown = -upDown
            if axisLeftRightInverted:
                leftRight = -leftRight
            if upDown < -0.1:
                moveForward = False
                moveBackward = True
            elif upDown > 0.1:
                moveForward = True
                moveBackward = False
            else:
                moveForward = False
                moveBackward = False
            if leftRight > 0.1:
                moveLeft = False
                moveRight = True
            elif leftRight < -0.1:
                moveLeft = True
                moveRight = False
            else:
                moveLeft = False
                moveRight = False

#Main program. Takes PygameHandler movement and turns it into a real robot movement.
#Eg two forward movements makes the robot walk forward two steps.
try:
    previousMove = False
    narrow()
    while True:
        print(previousMove)
        PygameHandler(pygame.event.get())
        if hadEvent:
            hadEvent = False
            if moveForward:
                if previousMove == moveForward:
                    walkForwardLeftStep()
                    previousMove = False
                else:
                    walkForwardRightStep()
                    previousMove = moveForward
            elif moveBackward:
                if previousMove == moveBackward:
                    walkBackwardsLeftStep()
                    previousMove = False
                else:
                    walkBackwardsRightStep()
                    previousMove = moveBackward
            elif moveLeft:
                rotateLeft()
                previousMove = moveLeft
                #if previousMove == moveLeft:
                 #   rotateLeftPart1()
                  #  previousMove = False
                #else:
                 #   rotateLeftPart2()
                  #  previousMove = moveLeft
            elif moveRight:
                rotateRight()
                previousMove = moveRight
                #if previousMove == moveRight:
                 #   rotateRightPart1()
                  #  previousMove = False
                #else:
                 #   rotateLeftPart2()
                  #  previousMove = moveRight
            #if moveForward:
             #   if previousMove == moveForward:
              #      frontRightSpread()
               #     time.sleep(1)
                #    frontRightSet()
                 #   previousMove = False
                #else:
                 #   frontLeftSpread()
                  #  time.sleep(1)
                   # frontLeftSet()
                    #previousMove = moveForward
            #elif moveBackward:
             #   if previousMove == moveBackward:
              #      middleRightSpread()
               #     time.sleep(1)
                #    middleRightSet()
                 #   previousMove = False
                #else:
                 #   middleLeftSpread()
                  #  time.sleep(1)
                   # middleLeftSet()
                    #previousMove = moveBackward
            #elif moveRight:
             #   backRightSpread()
              #  time.sleep(1)
               # backRightSet()
            #elif moveLeft:
             #   backLeftSpread()
              #  time.sleep(1)
               # backLeftSet()
        time.sleep(interval)

#Narrow position on quitting
except KeyboardInterrupt:
    narrow()
