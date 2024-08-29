from Coms import meter_param
import os
from upload import uploadloc,uploadcloud
from deploy import rundeploy
import subprocess
import time
# From Python3.7 you can add 
# keyword argument capture_output
if not os.path.isdir(r'vals'):
    print(subprocess.run(["mkdir", "vals"], 
                     capture_output=True))
a=0
while(1):
    
    if not os.path.exists(r'vals/sn.txt'):
        SN=meter_param()
        f=open(r"vals/sn.txt","x")
        print(SN)
        f.write(SN)
        try:
            uploadloc(r'vals/temp.txt')
        except Exception as e: 
        # Save the error message to a file 
            with open(r'vals/error_logloc.txt', 'a') as l: 
                l.write(str(e) + '\n')
            print('not able to upload locally')
        try :
            uploadcloud(r'vals/temp.txt')
        except Exception as e:
            with open(r'vals/error_logcloud.txt', 'a') as l: 
                l.write(str(e) + '\n')
            print('not able to upload to cloud')
        os.remove(r'vals/temp.txt')
        rundeploy(SN)
        
    if (a-time.time())>300:
        rundeploy(SN)
        a=time.time()