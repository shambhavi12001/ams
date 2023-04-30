#!/usr/bin/python
# Filename: text.py
import serial
import time
ser = serial.Serial("/dev/ttyS0",115200)

W_buff = ["AT+CGNSPWR=1\r\n", "AT+CGNSSEQ=\"RMC\"\r\n", "AT+CGNSINF\r\n", "AT+CGNSURC=2\r\n","AT+CGNSTST=1\r\n"]
ser.write(str.encode(W_buff[0]))
ser.flushInput()
data = ""
num = 0

try:
    print("{:>5}\t{:>5}".format('Degrees N', 'Degrees W'))
    while True:
        while ser.inWaiting() > 0:
            #print("ser_Waiting!")
            #print()
            data += str(ser.read(ser.inWaiting()), 'UTF-8')
        if data != "":
            #print("num = %s" % str(num))
            coord = data.split(",")
            if len(coord) >= 4:
                print("{:>5}\t{:>5}".format(coord[3], coord[4]))
                #print("Degrees N: ", coord[4])
                #print("Degrees W: ", coord[5]) 
                #print("this is data", data)
            if  num < 2:	# the string have ok
                #print(num)
                time.sleep(1)
                #print('SENDING TO BOARD %s' % str(W_buff[num+1]))
                #print()
                ser.write(str.encode(W_buff[num+1]))
                num = num + 1
            if num == 2:
                time.sleep(1)
                ser.write(str.encode(W_buff[2]))
                #print('SENDING TO BOARD %s' % str(W_buff[2]))
                #print()
            data = ""

except KeyboardInterrupt:
	if ser != None:
		ser.close()
