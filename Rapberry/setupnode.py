import json
import os
import subprocess
import requests
from ComsTest import meter_param
import random
#from initialwrittenconfig import initialaddres,ctvtsetup
import ast
def initialize(models):
    direction=[]
    laa=240
    keys=("serialNumber","model","address","cloudConfig","ct","vt")
    print(subprocess.run(["mkdir", "vals/meters"], 
                     capture_output=True))
    while(1):
        try:
            meternum=int(input('How many meters to install: '))
            break
        except:
            print("Invalid input")    
    
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
        temp["model"]=models[model-1].get("model")
        autoadd=input("already assigned address (not 1) (y/n): ")
        if autoadd=="y":
            tempadd=int(input("Which address does it have? :"))
            if (((tempadd not in direction) and tempadd!= 1) and tempadd<245):
                temp["address"]=tempadd
                direction.append(tempadd)
                
                
            elif len(direction)==240: 
                print('Ran out of available addresses')
                print(direction)
                return None
            else:
                print("unavailable address please change the adrress to one whis is not present in the following list")
                print(direction)
        elif autoadd=="n":
            
            
            while(1):
                tempadd=random.randint(5,245)
                if tempadd not in direction and tempadd>5:
                    temp["address"]=tempadd
                    direction.append(tempadd)
                    #initialaddres(temp["model"],tempadd)
                    
                    break
                elif len(direction)==240: 
                    print('Ran out of available addresses')
                    print(direction)
                    return None
                
        print("llegue")
        temp["ct"]=int(10*float(input("Current Transformer relation \n(Just numbers max 1 decimal place e.g. 100:1=100 2500:5=500 Max 999 Min 1):\n ")))
        temp["vt"]=int(10*float(input("Voltage Transformer relation \n(Just numbers max 1 decimal place e.g. 100:1=100 2500:5=500 Max 999 Min 1):\n ")))
        #ctvtsetup(temp["model"],temp["address"],temp["ct"],temp["vt"])
        
        SN=meter_param(temp["model"],temp["address"])
        print(SN)
        temp["serialNumber"]=SN[0]
        f=open(fr"vals/meters/{temp['serialNumber']}data.json","w")
        (json.dump(temp,f))
        f.close()
        
    f=open(fr"vals/laa.txt","x")
    f.write(str(laa))
    f=open(fr"vals/directions.json","x")
    json.dump(direction,f)
    print(temp)
    f=open(fr"vals/set_up.txt","x")
    json.dump(direction.append(laa),f)
    print(temp)           
