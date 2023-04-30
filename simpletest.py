# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
# Alternatively specify a different address and/or bus:
# pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
    # Configure min and max servo pulse lengths
servo_min = 110  # Min pulse length out of 4096
servo_max = 655  # Max pulse length out of 4096
i2c = busio.I2C(board.SCL, board.SDA)

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c, address=0x48)
ads.gain = 1
# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)
# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

    # Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)

print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
# Move servo on channel O between extremes.
    pwm.set_pwm(0, 0, 120)
    time.sleep(8)
    pwm.set_pwm(0,0,640)
    time.sleep(8)
    pwm.set_pwm(0,0,120)
    print("{:>5}\t{:>5}".format('raw', 'v'))
    print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
