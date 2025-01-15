import os
from ComsTest import meter_param,reading_meter,info_backup
from deploy_copy import rundeploy
import subprocess
import time
from setupnode import initialize
from version_extraction import call_api, version_check
from download_csv import csv_version
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
    print('initializing.................................\n')
    initialize(a)
    
    rundeploy()
else:    
    rundeploy()
    response, rtu_file, version_file = call_api()
    version_check(version_file=version_file)
    csv_version(rtu_file=rtu_file)

