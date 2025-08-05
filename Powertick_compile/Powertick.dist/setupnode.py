import json
import os
import subprocess
import requests
from ComsTest import meter_param
import random
#from initialwrittenconfig import initialaddres,ctvtsetup
import ast
def initialize(models):
    r = requests.get('https://powertick-api-js.azurewebsites.net/api/supportedTimeZones')
    tz=r.json()
    direction=[]
    laa=240
    keys=("serialNumber","model","address","cloudConfig","ct","vt","dev","tz_identifier")
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
        while(1):
            tib=input("Is it for dev (y/n): ")
            if tib=="y":
                temp["dev"]=True
                break
            elif tib=="n":
                temp["dev"]=False
                break
            print("Invalid input ")
        print("Select your timezone")
        for i in range(0,len(tz)):
            tmp=tz[i]["tz_identifier"]
            print(f"{i+1} : {tmp}")
        while(1):
            try:
                tib=int(input("Input the number of your time zone in the list: "))
                temp["tz_identifier"]=tz[tib-1]["tz_identifier"]
                break
            except:
                print("Invalid input ")    
            
                
            
        SN=meter_param(temp["model"],temp["address"],temp["dev"],temp["tz_identifier"])
        print("Serial Number: ", SN)
        temp["serialNumber"]=SN
        f=open(fr"vals/meters/{temp['serialNumber']}data.json","w")
        (json.dump(temp,f))
        f.close()
        
    f=open(fr"vals/laa.txt","x")
    f.write(str(laa))
    f=open(fr"vals/directions.json","x")
    json.dump(direction,f)
    print("temp: ", temp)
    f=open(fr"vals/set_up.txt","x")
    json.dump(direction.append(laa),f)
    print("temp", temp)           
