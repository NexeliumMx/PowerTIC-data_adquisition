from Coms import reading_meter
import os
from upload import uploadcloud,uploadloc
fil = open(r"Rapberry/sn.txt", "r")
sn= fil.read()
if  os.isdir(r'/Rapberry/sn.txt'):
    f=open(r"Rapberry/sn.txt","r")
    SN=reading_meter(f.read())
    try:
        uploadloc(r'Rapberry/tempquery.txt')
    except Exception as e: 
    # Save the error message to a file 
        with open('error_logloc.txt', 'a') as l: 
            l.write(str(e) + '\n')
        print('not able to upload locally')
    try :
        with open('error_logcloud.txt', 'a') as l: 
            l.write(str(e) + '\n')
        uploadcloud(r'Rapberry/tempquery.txt')
    except:
        print('not able to upload to cloud')
    os.remove(r'Rapberry/tempquery.txt')
else :
    print('run imprint')


