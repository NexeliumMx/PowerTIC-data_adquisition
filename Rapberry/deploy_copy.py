from ComsTest import reading_meter
import os
import json
from encript import encript
from uploadback import uploadbackup
def rundeploy(SN):
    if not os.path.isdir(r'vals/meters'):
        if not os.listdir(r"vals/meters"):
            print("Directory is empty")
        else: 
            for i in os.listdir(r"/vals/meters"):  
                with open(rf'vals/meters/{i}') as f:
                    data = json.load(f)
                    SN=data.get("serialNumber")
                    if data.get("cloudConfig")==None:
                     print('missing cloud config')
                    else:
                        if data.get("cloudConfig")=='ready':
                            #script para configuracion de CT y VT
                            print('finishing up details')
                            reading_meter(SN)
                        else:
                            reading_meter(SN)
    else :
        print('run imprint')
    if os.path.isdir(r"vals/nfail"):
        if not os.listdir(r"vals/nfail"):
            print("Directory is empty")
        else:    
            uploadbackup()
    else:
        print("Given directory doesn't exist")
