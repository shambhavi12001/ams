import sys
from rplidar import RPLidar
import time

PORT_NAME = '/dev/ttyUSB0'


def run(path):
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    outfile = open(path, 'w')
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for measurement in lidar.iter_measures():
            line = '\t'.join(str(v) for v in measurement)
            print(measurement[3])
            outfile.write(line + '\n')
    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()
    outfile.close()

if __name__ == '__main__':
    run("/home/pi/" + str(time.time()) + ".csv")
