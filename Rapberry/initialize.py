from Coms import meter_param
import os
from upload import uploadloc,uploadcloud
print("start")

print('Connected to the database.')

if not os.path.exists(r'/Rapberry/sn.txt'):
    SN=meter_param()
    f=open(r"Rapberry/sn.txt","x")
    f.write(SN)
    try:
        uploadloc(r'Rapberry/tempquery.txt')
    except Exception as e: 
    # Save the error message to a file 
        with open(r'Rapberry/error_logloc.txt', 'a') as l: 
            l.write(str(e) + '\n')
        print('not able to upload locally')
    try :
        with open(r'Rapberry/error_logcloud.txt', 'a') as l: 
            l.write(str(e) + '\n')
        uploadcloud(r'Rapberry/tempquery.txt')
    except:
        print('not able to upload to cloud')
    os.remove(r'Rapberry/tempquery.txt')
else :
    print('already exists')