from Coms import meter_param
import os
from upload import uploadloc,uploadcloud
print("codigo")


if not os.path.exists(r'Rapberry/sn.txt'):
    SN=meter_param()
    f=open(r"Rapberry/sn.txt","x")
    f.write(SN)
    try:
        uploadloc(r'Rapberry/temp.txt')
    except Exception as e: 
    # Save the error message to a file 
        with open(r'Rapberry/error_logloc.txt', 'a') as l: 
            l.write(str(e) + '\n')
        print('not able to upload locally')
    try :
        uploadcloud(r'Rapberry/temp.txt')
    except Exception as e:
        with open(r'Rapberry/error_logcloud.txt', 'a') as l: 
            l.write(str(e) + '\n')
        print('not able to upload to cloud')
    os.remove(r'Rapberry/temp.txt')
else :
    print('already exists')