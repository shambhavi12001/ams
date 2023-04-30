import time
from tfmini import TFmini

# create the sensor and give it a port and (optional) operating mode
tf = TFmini('/dev/tty.usbserial-A506BOT5', mode=TFmini.STD_MODE)

try:
    print('='*25)
    while True:
        d = tf.read()
        if d:
            print(f'Distance: {d:5}')
        else:
            print('No valid response')
        time.sleep(0.1)

except KeyboardInterrupt:
    tf.close()
    print('bye!!')
