from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40)

pwm.setPWMFreq(60)

pwm.setPWM(0,0,300)
