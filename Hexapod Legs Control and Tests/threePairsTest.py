from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)
pwm.setPWMFreq(60)

#setting base servos
pwm.setPWM(3,0,500) #front right base
pwm.setPWM(0,0,300) #front left servo
pwm.setPWM(5,0,500) #middle right base
pwm.setPWM(6,0,325) #middle left base
pwm.setPWM(11,0,400) #back right base
pwm.setPWM(12,0,250) #back left base

while True:
	#setting initial position
	call("echo 1=170 > /dev/servoblaster", shell=True) #front right tip
	pwm.setPWM(4,0,300) #front left tip
	pwm.setPWM(1,0,400) #front right mid
	pwm.setPWM(2,0,350) #front left mid
	time.sleep(1)
	pwm.setPWM(7,0,500) #middle right mid
	pwm.setPWM(8,0,325) #middle left mid
	pwm.setPWM(9,0,400) #middle right tip
	pwm.setPWM(10,0,400) #middle left tip
	time.sleep(1)
	pwm.setPWM(13,0,250) #back right mid
	pwm.setPWM(14,0,350) #back left mid
	pwm.setPWM(15,0,400) #back right tip
	call("echo 4=200 > /dev/servoblaster", shell=True) #back left tip
	time.sleep(1)
	#setting spread out positions
	call("echo 1=200 > /dev/servoblaster", shell=True) #front right tip
	pwm.setPWM(4,0,300) #front left tip
	pwm.setPWM(1,0,500) #front right mid
	pwm.setPWM(2,0,250) #front left mid
	time.sleep(1)
	pwm.setPWM(7,0,600) #middle right mid
	pwm.setPWM(8,0,225) #middle left mid
	pwm.setPWM(9,0,500) #middle right tip
	pwm.setPWM(10,0,300) #middle left tip
	time.sleep(1)
	pwm.setPWM(13,0,350) #back right mid
	pwm.setPWM(14,0,250) #back left mid
	pwm.setPWM(15,0,500) #back right tip
	call("echo 4=150 > /dev/servoblaster", shell=True) #back left tip	
	time.sleep(1)
