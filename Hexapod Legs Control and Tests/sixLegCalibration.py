from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)
pwm.setPWMFreq(60)


call("echo 1=200 > /dev/servoblaster", shell=True)#right front  tip
pwm.setPWM(4,0,325) #left front tip
pwm.setPWM(1,0,450) #right front mid
pwm.setPWM(2,0,340) #left front mid
pwm.setPWM(3,0,300) #right front base **
pwm.setPWM(0,0,550) #left front base **

pwm.setPWM(5,0,275) #middle right base **
pwm.setPWM(6,0,475) #middle left base **
pwm.setPWM(7,0,500) #middle right mid
pwm.setPWM(8,0,325) #middle left mid
pwm.setPWM(9,0,500) #middle right tip
pwm.setPWM(10,0,300) #middle left tip

pwm.setPWM(11,0,300) #back right base **
call("echo 4=110 > /dev/servoblaster", shell=True) #back left base **
pwm.setPWM(13,0,275) #back right mid
pwm.setPWM(14,0,325) #back left mid
pwm.setPWM(15,0,550) #back right tip
pwm.setPWM(12,0,300) #back left tip
