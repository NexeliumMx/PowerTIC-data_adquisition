import json
import os
import subprocess
import requests
from ComsTest import meter_param
def initialize():
    direction=[]
    laa=240
    keys=("serialNumber","model","address","cloudConfig","ct","vt")
    print(subprocess.run(["rm", "vals/meters"], 
                     capture_output=True))
    print(subprocess.run(["mkdir", "vals/meters"], 
                     capture_output=True))
    while(1):
        try:
            meternum=int(input('How many meters to install: '))
            break
        except:
            print("Invalid input")
            
    
    r = requests.get('https://supportedmodels-test-api.azurewebsites.net/api/supportedModels')
    models=(r.json())
    for i in range(0,meternum):
        print("Supported models: ")
        for j in range(1,len(models)+1):
            print(" "+ str(models[j-1].get("SERIAL"))+". "+ models[j-1].get("model"))
        temp=dict.fromkeys(keys)
        while(1):
            try:
                model=int(input('Model of the meter (Number in the list): '))
                print(f"selected model {models[model-1]}")
                break
            except: 
                print("invalid model check for support and run again")
        SN=meter_param(models[model-1])
        temp["model"]=models[model-1].get("model")
        tempadd=240-i
        if tempadd not in direction and tempadd>5:
            temp["address"]=tempadd
            direction.append(tempadd)
        else: 
            print('Ran out of available addresses')
            print(direction)
            return None
        temp["ct"]=int(10*float(input("Current Transformer relation \n(Just numbers max 1 decimal place e.g. 100:1=100 2500:5=500 Max 999 Min 1):\n ")))
        temp["vt"]=int(10*float(input("Voltage Transformer relation \n(Just numbers max 1 decimal place e.g. 100:1=100 2500:5=500 Max 999 Min 1):\n ")))
        f=open(fr"vals/meters/{i}data.json","x")
        
        print(SN[0])
        (json.dump(temp,f))
        laa=tempadd-1
    f=open(fr"vals/meters/laa.txt","x")
    f.write(str(laa))
    f=open(fr"vals/meters/directions.json","x")
    json.dump(direction,f)
    print(temp)
initialize()                
