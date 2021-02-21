import serial

# can test with echo "Hello" > /dev/ttyS0

#import serial
#ser = serial.Serial('/dev/ttyS0')  # open serial port
#print(ser.name)         # check which port was really used
#ser.write(b'hello')     # write a string
#ser.close()             # close port

def send(ser:serial,cmd:str):
    #ser.write(bytearray(cmd,encoding='ascii'))
    ser.write(bytearray("Hello, world!\n",encoding='ascii'))
