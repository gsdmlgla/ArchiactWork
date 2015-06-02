from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)
pwm.setPWMFreq(60)

while True:
    for i in reversed(range(450)):
        pwm.setPWM(1,0,i)
        pwm.setPWM(2,0,i)
    #for j in reversed(range(340)):
     #   pwm.setPWM(2,0,j)
    for i in range(450):
        pwm.setPWM(2,0,i)
        pwm.setPWM(1,0,i)
   # for j in range(340):
    #    pwm.setPWM(2,0,i)
    pwm.setPWM(1,0,450)
    
