from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)

servoMax1 = 450 #front right  middle
servoMin1 = 350 #front right  middle
servoMax2 = 300 #front left tip
servoMin2 = 200 #front left tip
servoMax3 = 350 #front left middle
servoMin3 = 250 #front left middle

pwm.setPWMFreq(60)
#pwm.setPWM(0,0,500) #this is base servo front right
#pwm.setPWM(8, 0, 300) #front left base

while True:
	#front right tip and left tip
	call("echo 0=0 > /dev/servoblaster", shell=True)
	call("echo 0=225 > /dev/servoblaster", shell=True)
	pwm.setPWM(0, 0, servoMin2)
	time.sleep(1)
	call("echo 0=180 > /dev/servoblaster", shell=True)
	pwm.setPWM(0, 0, servoMax2)
	time.sleep(1)
	#front mid
#	pwm.setPWM(4, 0, servoMin1)
#	pwm.setPWM(6, 0, servoMax3)
#	time.sleep(1)
#	pwm.setPWM(4, 0, servoMax1)
#	pwm.setPWM(6, 0, servoMin3)
#	time.sleep(1)
