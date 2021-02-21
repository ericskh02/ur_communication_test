import serial

#Get from executing python -m serial.tools.list_ports in console
#port = '/dev/ttyUSB0'

#ser = serial.Serial(port)
#print(ser.name)

#x = ser.read_until(b'\r')

#print(x)


#from serial.tools import list_ports
#list_ports.comports()


from time import sleep

#ser = serial.Serial (port, 9600)    #Open port with baud rate
#while True:
#    received_data = ser.read()              #read serial port
#    sleep(0.03)
#    data_left = ser.inWaiting()             #check for remaining byte
#    received_data += ser.read(data_left)
#    print (received_data)                   #print received data
#    ser.write(received_data)                #transmit data serially 

def read(ser: serial):
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data

