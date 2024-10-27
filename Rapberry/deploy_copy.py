from ComsTest import reading_meter
import os
from encript import encript
def rundeploy(SN):
    if  os.path.exists(r'vals/sn.txt'):
        f=open(r"vals/sn.txt","r")
        sn=f.readline(1)
        print('seviene')
        print(sn)
        reading_meter(sn)
    else :
        print('run imprint')
    if os.path.isdir(r"vals/nfail"):
        if not os.listdir(r"vals/nfail"):
            print("Directory is empty")
        else:    
            print("Directory is not empty")
    else:
        print("Given directory doesn't exist")
