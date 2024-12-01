import os
from ComsTest import meter_param,reading_meter,timestamp_adquisition,info_backup
from deploy_copy import rundeploy
import subprocess
import time
from setupnode import initialize
import requests
import json
version='0.0.3'
if not os.path.isdir(r'vals'):
    print(subprocess.run(["mkdir", "vals"], 
                     capture_output=True))
    print(subprocess.run(["mkdir", "vals/nfail"], 
                     capture_output=True))
    print(subprocess.run(["mkdir", "vals/apifail"], 
                     capture_output=True))
    print(subprocess.run(["mkdir", "vals/success"], 
                     capture_output=True))
subprocess.run(["curl","-O -J \"https://powertick-api-py.azurewebsites.net/api/downloadModbusRTUcsv\""],capture_output=True)
print(os.path.exists(r"vals/suported_models.json"))
if not os.path.exists(r"vals/suported_models.json"):
    r = requests.get('https://supportedmodels-test-api.azurewebsites.net/api/supportedModels')
    f=open(r"vals/supported_models.json","x")
    json.dump(r,f)
else:
    r = requests.get('https://supportedmodels-test-api.azurewebsites.net/api/supportedModels')
    f=open(r"vals/supported_models.json","w")
    json.dump(r.json(),f)
if not os.path.exists(r'vals/set_up.txt'):
    initialize()
else:    
    y=open(r"vals/sn.txt")
    SN = y.read()
    rundeploy(SN)