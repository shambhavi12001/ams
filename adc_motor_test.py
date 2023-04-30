# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import Adafruit_PCA9685
import time
import board
import busio
import math
import numpy
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)
# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
i2c = busio.I2C(board.SCL,board.SDA)

#pwm1 = Adafruit_PCA9685.PCA9685(address = 0x41)
# Alternatively specify a different address and/or bus:
# pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
    # Configure min and max servo pulse lengths

# Initialise the PCA9685 using the default address (0x40).

# Create the ADC object using the I2C bus
# Helper function to make setting a servo pulse width simpler.
ads = ADS.ADS1015(i2c, address = 0x40)
chan = AnalogIn(ads,ADS.P0)
ads.gain = 1
#ads1 = ADS.ADS1015(i2c, address = 0x41)
#chan1 = AnalogIn(ads1, ADS.P0)
#ads1.gain = 1
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(220)
#pwm1.set_pwm_freq(220)
print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
# Move servo on channel O between extremes.
    '''
    #driver 1 base joints
    pwm.set_pwm(0,0,1400)
    pwm.set_pwm(2,0,1400)
    pwm.set_pwm(4,0,1400)

    #driver 1 hip joints
    pwm.set_pwm(6,0,1900)
    pwm.set_pwm(8,0,1900)
    pwm.set_pwm(10,0,1900)

    #driver 2 base joints
    pwm1.set_pwm(0,0,1400)
    pwm1.set_pwm(2,0,1400)
    pwm1.set_pwm(4,0,1400)

    #driver 2 hip joints
    pwm1.set_pwm(6,0,1900)
    pwm1.set_pwm(8,0,1900)
    pwm1.set_pwm(10,0,1825)
   
    #driver 1 knee joints
    pwm.set_pwm(12,0,1525)
    pwm.set_pwm(14,0,1500)
    pwm.set_pwm(15,0,1500)
    
    #driver 2 knee joints
    pwm1.set_pwm(14,0,1375)
    pwm1.set_pwm(12,0,1350) 
    pwm1.set_pwm(15,0,1450)
    time.sleep(5)
    '''
    c = 17.2 #20.1
    d = 25.5 #20.1
    b = 11 #10.1
    alpha = 0#-21 * 3.1415 / 180
    avec = [-5,0,-0.1]
    avecproj = [-5,0,0]
    cfactor = 0.91428
    for i in range(0, 628):
        
        yt = 5*math.sin(0.01*i);#was 10
        backstep = 200*math.sin(0.01*(i+157));
        rvec = [-25,yt,-40] # The desired neutral position
        rvecproj = [-15,yt,0] # Projection of rvec to normal vector
        lvecproj = numpy.subtract(rvecproj,avecproj)
        nlvec = numpy.linalg.norm(lvecproj)
        nrvec = numpy.linalg.norm(rvecproj)
        th1chk = -avec[0]*yt # Check the sign of theta 1
         
        #solve for theta 1 
        theta1 = math.degrees(math.acos((avecproj[0]**2+nlvec**2-nrvec**2)/(2*math.fabs(avecproj[0])*nlvec))) 
        
        if th1chk > 0:
            theta1 = 180 - theta1
            theta1 = math.fabs(360-theta1)
            signal1 = int((theta1-180)/cfactor)
        else:
            theta1 = theta1 + 180
            theta1 = math.fabs(360-theta1)
            signal1 = int((theta1+180)/cfactor)

        bvec = numpy.add(avec,((numpy.multiply([math.cos(math.radians(180+theta1))*math.cos(alpha),math.sin(math.radians(180+theta1))*math.cos(alpha),math.sin(alpha)],b))))

        #print((numpy.multiply([math.cos(math.radians(180+theta1))*math.cos(alpha),math.sin(math.radians(180+theta1))*math.cos(alpha),math.sin(alpha)],b)))
        #print((c**2 + d**2 - (numpy.linalg.norm(numpy.subtract(bvec,rvec)))**2)/(2*c*d))
        #print(1/(2*c*d))       

        theta3 = math.degrees(math.acos((c**2 + d**2 - (numpy.linalg.norm(numpy.subtract(bvec,rvec)))**2)/(2*c*d))) - 180
        theta2 = math.degrees(math.acos((c**2 + (numpy.linalg.norm(numpy.subtract(bvec, rvec))**2-d**2))/(2*c*numpy.linalg.norm(numpy.subtract(bvec,rvec)))))+math.degrees(math.acos((b**2+(numpy.linalg.norm(numpy.subtract(bvec,rvec)))**2-(numpy.linalg.norm(numpy.subtract(avec,rvec))**2))/(2*b*(numpy.linalg.norm(numpy.subtract(bvec,rvec))))))-180     
        #theta3 = -1*theta3
        theta2 = -1*theta2
        # WORKS print((2*c*numpy.linalg.norm(numpy.subtract(bvec,rvec))))
        signal2 = int(theta2/cfactor*(16/3))
        if backstep < 0:
            set1offset = -30
            set2offset = 0
        else:
            set1offset = 0
            set2offset = -30
        # WORKS print( math.degrees(math.acos((c**2 + (numpy.linalg.norm(numpy.subtract(bvec, rvec))**2-d**2))/(2*c*numpy.linalg.norm(numpy.subtract(bvec,rvec))))))

        #print(numpy.linalg.norm(numpy.subtract(bvec,rvec)))
        #WORKS add () print((c**2 + (numpy.linalg.norm(numpy.subtract(bvec, rvec))**2-d**2)))
        #print(bvec)
        #print(theta2)
        offset = 0 
        signal3 = int(theta3/cfactor*16/3*1.55) # USE
        #pwm.set_pwm(0, 0, int(1400 - 40 * math.sin(0.01 * i)))
        #pwm.set_pwm(2, 0, int(1400 - 40 * math.sin(0.01 * i)))
        pwm.set_pwm(0, 0, 1200+signal1)        # USE
        #pwm.set_pwm(6, 0, 1200+signal1)
        #pwm.set_pwm(6, 0, 1300+signal1)
        #pwm1.set_pwm(0, 0, int(1400 - 40 * math.sin(0.01 * i)))
        #pwm1.set_pwm(2, 0, int(1400 - 40 * math.sin(0.01 * i)))
        #pwm1.set_pwm(2, 0, int(1400 + 40 * math.sin(0.01 * i)))
        
        pwm.set_pwm(2, 0, 1400+ signal2 + set1offset) # USE
        print(1400 + signal2)
        #pwm.set_pwm(8, 0, int(1875 - 125 * math.sin(0.01 * i)))
        #pwm.set_pwm(10, 0, int(1875 - 125 * math.sin(0.01 * i)))
        #pwm1.set_pwm(6, 0, int(1875 - 125 * math.sin(0.01 * i)))
        #pwm1.set_pwm(8, 0, int(1875 - 125 * math.sin(0.01 * i)))
        #pwm1.set_pwm(10, 0, int(1875 -125 * math.sin(0.01 * i)))
        #pwm.set_pwm(2, 0, 1940)
        #pwm.set_pwm(12, 0, int(1525 - 70 * math.sin(0.01 * i)))
        #pwm.set_pwm(14, 0, int(1500 - 70 * math.sin(0.01 * i)))
        pwm.set_pwm(4, 0, 1450- signal3) # USE
        #pwm1.set_pwm(12, 0, int(1350 - 70 * math.sin(0.01 * i)))
        #pwm1.set_pwm(14, 0, int(1375 - 70 * math.sin(0.01 * i)))
        #pwm1.set_pwm(15, 0, int(1450 - 70 * math.sin(0.01 * i)))
        
        #print(signal3 + 1540)
        #print(c**2 + d**2 - (numpy.linalg.norm(numpy.subtract(bvec,rvec)))**2)
        #print((2*c*d))
        #print(signal3)
        
        #print("Theta 1 = ", theta1)
        #print("Theta 2 = ", theta2)
        #print("Theta 3 = ", theta3)
    
        time.sleep(0.02)
    #print("{:>5}\t{:>5.3f}".format(chan.value,chan.voltage),"     ",1000-i)
    #pwm.set_pwm(0,0,500)
    #time.sleep(10)
    #pwm.set_pwm(0,0,2400)
    #time.sleep(10)
    ##pwm.set_p:wm(0,0,500)
