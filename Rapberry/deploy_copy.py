from ComsTest import reading_meter
import serial
import os
import json
from encript import encript
from uploadback import uploadbackup

ser =  serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=19200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=0.1)

def rundeploy():
    if  os.path.isdir(r'vals/meters'):
        
        if not os.listdir(r"vals/meters"):
            print("Directory is empty")
        else: 
            for i in os.listdir(r"vals/meters"):  
                with open(rf'vals/meters/{i}') as f:
                    data = json.load(f)
                    SN=data.get("serialNumber")
                    mbdadd=data.get("address")
                    model=data.get("model")
                    print('finishing up details')
                    if data.get("cloudConfig")==None:
                     print('confirm configuration in cloud as soon as posible')
                    reading_meter(SN,mbdadd,model)

    if os.path.isdir(r"vals/nfail"):
        if not os.listdir(r"vals/nfail"):
            print("Directory is empty")
        else:    
            uploadbackup()
    else:
        print("Given directory doesn't exist")
