import os
from ComsTest import meter_param,reading_meter,timestamp_adquisition,info_backup
from deploy_copy import rundeploy
import subprocess
import time
# From Python3.7 you can add 
# keyword argument capture_output
if not os.path.isdir(r'vals'):
    print(subprocess.run(["mkdir", "vals"], 
                     capture_output=True))
    print(subprocess.run(["mkdir", "vals/nfail"], 
                     capture_output=True))
    print(subprocess.run(["mkdir", "vals/apifail"], 
                     capture_output=True))
    print(subprocess.run(["mkdir", "vals/success"], 
                     capture_output=True))
if not os.path.exists(r'vals/sn.txt'):
    SN=meter_param()
    f=open(r"vals/sn.txt","x")
    print(SN[1])
    f.write(SN[1])
    rundeploy(SN[1])
else:    
    y=open(r"vals/sn.txt")
    SN = y.read()
    rundeploy(SN)