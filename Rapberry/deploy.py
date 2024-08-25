from Coms import reading_meter
import os
from upload import uploadcloud,uploadloc
fil = open(r"Rapberry/sn.txt", "r")
sn= fil.read()
if  os.path.exists(r'Rapberry/sn.txt'):
    f=open(r"Rapberry/sn.txt","r")
    sn=f.read()
    reading_meter(sn)
    try:
        uploadloc(r'Rapberry/temp.txt')
    except Exception as e: 
    # Save the error message to a file 
        with open(r'Rapberry/error_logloc.txt', 'a') as l: 
            l.write(str(e) + '\n')
        print('not able to upload locally')
    try :
        uploadcloud(r'Rapberry/temp.txt')
    except:
        with open(r'Rapberry/error_logcloud.txt', 'a') as l: 
            l.write(str(e) + '\n')
        print('not able to upload to cloud')
    #os.remove(r'Rapberry/temp.txt')
else :
    print('run imprint')


