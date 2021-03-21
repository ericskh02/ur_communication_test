#Always read
""" 
import asyncio

import aioserial

async def read_and_print(aioserial_instance: aioserial.AioSerial):
    while True:
        print((await aioserial_instance.read_async()).decode(errors='ignore'),end='',flush=True)

asyncio.run(read_and_print(aioserial.AioSerial(port='/dev/ttyS0')))
"""




#Read once
"""
import asyncio
import aioserial

port = '/dev/ttyS0' #for raspberry pi 4
#port = '/dev/ttyUSB0' #for laptop

baudrate = 9600


async def read_and_print(aioserial_instance: aioserial.AioSerial):
    while True:
        data: bytes = await aioserial_instance.read_async()
        print(data.decode(errors='ignore'),end='',flush=True)
        if b'\n' in data:
            aioserial_instance.close()
            break

aioserial_instance = aioserial.AioSerial = aioserial.AioSerial(port=port,baudrate=baudrate)

async def main():
    await asyncio.gather(read_and_print(aioserial_instance),aioserial_instance.write_async(b'Hello, World!\n'))
asyncio.run(main())
"""

import asyncio
import aioserial
import aioconsole

port = '/dev/ttyS0' #for raspberry pi 4
#port = '/dev/ttyUSB0' #for laptop

baudrate = 9600

aioserial_instance = aioserial.AioSerial(port=port,baudrate=baudrate)

loop = asyncio.get_event_loop()

cmd = ""

received = ""

async def receive(aioserial_instance: aioserial.AioSerial):
    while True:
        data: bytes = await aioserial_instance.read_async()
        received += data.decode(errors='ignore)    
        print(data.decode(errors='ignore'),end='',flush=True)
        if len(received) >= 7:
            if cmd != received[:7]:
                print("validation error!")
        received = ""

async def write(aioserial_instance: aioserial.AioSerial):
    while True:
        cmd = await aioconsole.ainput('Input a line for serial communication: ')
        await aioserial_instance.write_async(bytearray(cmd,encoding='ascii'))

loop.create_task(receive(aioserial_instance))
loop.create_task(write(aioserial_instance))
#loop.run_until_complete() #Stop running after completing all tasks in coroutine
try:
    loop.run_forever() #Keep running unless loop.stop()
except KeyboardInterrupt:
    loop.close()
