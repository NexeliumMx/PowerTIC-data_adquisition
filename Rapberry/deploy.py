from Coms import reading_meter
import os
from encript import encript
from upload import uploadcloud,uploadloc,uploadcloudback
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
        s=open(r'Rapberry/temp.txt')
        q=str(s.read())
        with open(r'Rapberry/error_logloc.txt', 'a') as l: 
            l.write(str(e) + '\n')
        print('not able to upload locally')
        with open(r'Rapberry/failedlqueries.txt', 'a') as l: 
            l.write(str(encript(q)) + '/')
    try :
        uploadcloud(r'Rapberry/temp.txt')
    except Exception as e:
        s=open(r'Rapberry/temp.txt')
        q=str(s.read())
        print (q)
        with open(r'Rapberry/error_logcloud.txt', 'a') as l: 
            l.write(str(e) + '\n')
        print('not able to upload to cloud')
        with open(r'Rapberry/failedcqueries.txt', 'a') as l: 
            l.write(str((encript(q))) + '\n')
    os.remove(r'Rapberry/temp.txt')
else :
    print('run imprint')
if os.path.exists(r'Rapberry/failedcqueries.txt'):
    try:
        t=open(r'Rapberry/failedcqueries.txt')
        text=str(t.readlines())
        for a in text:
            print(encript(a))
            print('sent 1')
            uploadcloudback(str(encript(a)))
    except Exception as e:
        with open(r'Rapberry/error_logback.txt', 'a') as l: 
            l.write(str(e) + '\n')
        print('not able to upload unuploaded queries')

