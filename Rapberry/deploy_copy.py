from ComsTest import reading_meter
import os
from encript import encript
from uploadback import uploadbackup
def rundeploy(SN):
    if  os.path.exists(r'vals/sn.txt'):
        f=open(r"vals/sn.txt","r")
        sn=f.readline(1)
        print('seviene')
        print(SN)
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
