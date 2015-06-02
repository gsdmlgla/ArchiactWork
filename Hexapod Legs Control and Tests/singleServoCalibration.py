from Adafruit_PWM_Servo_Driver import PWM
import time

pwm=PWM(0x40)
pwm.setPWMFreq(60)

while True:
#	pwm.setPWM(11,0,300)
	pwm.setPWM(0,0,300)
	time.sleep(1)
	pwm.setPWM(0,0,200)
	time.sleep(1)

