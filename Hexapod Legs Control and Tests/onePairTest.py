from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)

pwm.setPWMFreq(60)
#call("echo 0=0 > /dev/servoblaster", shell=True)
pwm.setPWM(0,0,300) #right base
pwm.setPWM(3,0,500) #left base

while True:
	pwm.setPWM(1,0,400) #right mid
	pwm.setPWM(2,0,350) #left mid
#	pwm.setPWM(9,0,400) #right tip
	pwm.setPWM(4,0,300)#left tip
	call("echo 1=200 > /dev/servoblaster", shell=True)
	time.sleep(1)
	pwm.setPWM(1,0,500) #right mid
	pwm.setPWM(2,0,250) #left mid
	pwm.setPWM(4,0,400) #right tip
#	pwm.setPWM(10,0,300)#left tip	
	call("echo 1=170 > /dev/servoblaster", shell=True)
	time.sleep(1)
