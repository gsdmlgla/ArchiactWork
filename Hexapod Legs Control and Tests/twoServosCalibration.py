from Adafruit_PWM_Servo_Driver import PWM
#from subprocess import call
import time

pwm = PWM(0x40)

pwm.setPWMFreq(60)
#call("echo 0=0 > /dev/servoblaster", shell=True)

while True:
	pwm.setPWM(9,0,500)
	pwm.setPWM(10,0,300)
#	call("echo 0=180 > /dev/servoblaster", shell=True)
	time.sleep(1)
	pwm.setPWM(9,0,400)
#	call("echo 0=225 > /dev/servoblaster", shell=True)
	pwm.setPWM(10,0,400)
	time.sleep(1)

	
