import os
from ComsTest import meter_param,reading_meter,info_backup
from deploy_copy import rundeploy
import subprocess
import time
from setupnode import initialize
import requests
import json
version='0.0.3'
print(not os.path.isdir(r'vals'))
if not os.path.isdir(r'vals'):
    print(subprocess.run(["mkdir", "vals"], 
                     capture_output=True))
    print(subprocess.run(["mkdir", "vals/nfail"], 
                     capture_output=True))
    print(subprocess.run(["mkdir", "vals/apifail"], 
                     capture_output=True))
    print(subprocess.run(["mkdir", "vals/success"], 
                     capture_output=True))
a=requests.get('https://power-tick-api-js.nexelium.mx/api/testDBconnection')
print(a.json())    

subprocess.run(["curl","-O -J \"https://powertick-api-py.azurewebsites.net/api/downloadModbusRTUcsv\""],capture_output=True)
r = requests.get('https://powertick-api-js.azurewebsites.net/api/supportedModels')
    
a=r.json()

if not os.path.exists(r'vals/set_up.txt'):
    initialize(a)
    rundeploy()
else:    
    rundeploy()