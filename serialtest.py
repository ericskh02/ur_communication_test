import serial
import inputimeout

import serialtest_send
import serialtest_client

#from serial.tools import list_ports
#print(*list_ports.comports())

port = '/dev/ttyUSB0' #for laptop
#port = '/dev/ttyS0' #for raspberry pi 4

ser = serial.Serial(port,timeout=1)

print(ser.name)

while(True):
    try:
        cmd = inputimeout.inputimeout(prompt='>>', timeout=0.5)
    except inputimeout.TimeoutOccurred:
        cmd = None
    if cmd is not None:
        serialtest_send.send(ser,cmd)
    serialtest_client.read(ser)

    
