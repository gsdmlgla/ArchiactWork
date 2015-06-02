from Adafruit_PWM_Servo_Driver import PWM
from subprocess import call
import time

pwm = PWM(0x40)
pwm.setPWMFreq(60)

while True:
    #call("echo 1=150 > /dev/servoblaster", shell=True)#right front  tip
    #pwm.setPWM(4,0,420) #left front tip
    #pwm.setPWM(1,0,375) #right front mid
    #pwm.setPWM(2,0,390) #left front mid
    #pwm.setPWM(3,0,525) #right front base
    #pwm.setPWM(0,0,300) #left front base
    #pwm.setPWM(5,0,500) #middle right base
    #pwm.setPWM(6,0,350) #middle left base
    #pwm.setPWM(7,0,450) #middle right mid
    #pwm.setPWM(8,0,400) #middle left mid
    #pwm.setPWM(9,0,475) #middle right tip
    #pwm.setPWM(10,0,400) #middle left tip
    #pwm.setPWM(11,0,400) #back right base
    #call("echo 4=90 > /dev/servoblaster", shell=True) #back left base
    #pwm.setPWM(13,0,200) #back right mid
    #pwm.setPWM(14,0,400) #back left mid
    #pwm.setPWM(15,0,450) #back right tip
    #pwm.setPWM(12,0,350) #back left tip

    time.sleep(1)
    
    call("echo 1=200 > /dev/servoblaster", shell=True)#right front  tip
    pwm.setPWM(4,0,325) #left front tip
    pwm.setPWM(1,0,450) #right front mid
    pwm.setPWM(2,0,325) #left front mid
    pwm.setPWM(3,0,525) #right front base
    pwm.setPWM(0,0,300) #left front base
    pwm.setPWM(5,0,500) #middle right base
    pwm.setPWM(6,0,350) #middle left base
    pwm.setPWM(7,0,500) #middle right mid
    pwm.setPWM(8,0,325) #middle left mid
    pwm.setPWM(9,0,500) #middle right tip
    pwm.setPWM(10,0,300) #middle left tip
    pwm.setPWM(11,0,400) #back right base
    call("echo 4=90 > /dev/servoblaster", shell=True) #back left base
    pwm.setPWM(13,0,275) #back right mid
    pwm.setPWM(14,0,325) #back left mid
    pwm.setPWM(15,0,550) #back right tip
    pwm.setPWM(12,0,300) #back left tip

    time.sleep(1)
