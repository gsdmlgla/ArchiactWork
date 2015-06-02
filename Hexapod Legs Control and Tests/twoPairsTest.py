from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)

pwm.setPWMFreq(60)

call("echo 0=0 > /dev/servoblaster", shell=True)

pwm.setPWM(0,0,300)#left front base
pwm.setPWM(3,0,500)#right front base
pwm.setPWM(5,0,500)#right mid base
pwm.setPWM(6,0,325)#left mid base

while True:
	call("echo 0=180 > /dev/servoblaster", shell=True)#front right tip
	pwm.setPWM(1,0,400)#front right mid
	pwm.setPWM(2,0,350)#front left mid
	pwm.setPWM(4,0,300)#front left tip
	time.sleep(1)
	pwm.setPWM(7,0,500)#middle right mid
	pwm.setPWM(8,0,325)#middle left mid
	pwm.setPWM(9,0,500)#middle right tip
	pwm.setPWM(10,0,300)#middle left tip
	time.sleep(1)
	call("echo 0=225 > /dev/servoblaster", shell=True)#front right tip
	pwm.setPWM(1,0,500)#front right mid
	pwm.setPWM(2,0,250)#front left mid
	pwm.setPWM(4,0,200)#front left tip
	time.sleep(1)
	pwm.setPWM(7,0,600)#middle right mid
	pwm.setPWM(8,0,225)#middle left mid
	pwm.setPWM(9,0,400)#middle right tip
	pwm.setPWM(10,0,400)#middle left tip
	time.sleep(1)
	
