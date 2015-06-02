from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)
pwm.setPWMFreq(60)

def frontRightStep():
	call("echo 1=200 > /dev/servoblaster", shell=True)
	pwm.setPWM(1,0,400) #right mid
	time.sleep(0.25)
	call("echo 1=170 > /dev/servoblaster", shell=True)
	pwm.setPWM(1,0,500) #right mid

def frontLeftStep():
	pwm.setPWM(2,0,350) #left mid
	pwm.setPWM(4,0,400) #left tip
	time.sleep(0.25)
	pwm.setPWM(2,0,250) #left mid
	pwm.setPWM(4,0,300) #left tip

def middleRightStep():
	pwm.setPWM(7,0,500) #mid right
	pwm.setPWM(9,0,400) #right tip
	time.sleep(0.25)
	pwm.setPWM(7,0,600) #right mid
	pwm.setPWM(9,0,500) #right tip

def middleLeftStep():
	pwm.setPWM(8,0,325) #mid left
	pwm.setPWM(10,0,400) #left tip
	time.sleep(0.25)
	pwm.setPWM(8,0,225) #left mid
	pwm.setPWM(10,0,300) #left tip

def backRightStep():
	pwm.setPWM(13,0,250) #right mid
	pwm.setPWM(15,0,400) #right tip
	time.sleep(0.25)
	pwm.setPWM(13,0,350) #right mid
	pwm.setPWM(15,0,500) #right tip

def backLeftStep():
	pwm.setPWM(14,0,350) #left mid
	call("echo 4=200 > /dev/servoblaster", shell=True)
	time.sleep(0.25)
	pwm.setPWM(14,0,250) #left tip
	call("echo 4=150 > /dev/servoblaster", shell=True)

def forwardSteps():
	pwm.setPWM(0,0,500) #front left
	pwm.setPWM(3,0,350) #front right
	pwm.setPWM(5,0,400) #middle right
	pwm.setPWM(6,0,450) #middle left
	pwm.setPWM(11,0,300) #back right
	pwm.setPWM(12,0,300) #back left

	time.sleep(1)
	pwm.setPWM(3,0,500) #set right front
	frontRightStep()
	pwm.setPWM(6,0,325) #set middle left
	middleLeftStep()
	pwm.setPWM(11,0,400) #set back right
	backRightStep()

	time.sleep(1)
	pwm.setPWM(0,0,300) #set front left
	frontLeftStep()
	pwm.setPWM(5,0,500) #set middle right
	middleRightStep()
	pwm.setPWM(12,0,250) #set back left
	backLeftStep()
	time.sleep(1)

while True:
	forwardSteps()

#frontRightStep()
#frontLeftStep()
