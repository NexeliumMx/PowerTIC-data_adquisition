from Coms import reading_meter
import os
from encript import encript
from upload import uploadcloud,uploadloc,uploadcloudback
def rundeploy(SN):
    fil = open(r"vals/sn.txt", "r")
    sn= fil.read()
    if  os.path.exists(r'vals/sn.txt'):
        f=open(r"vals/sn.txt","r")
        sn=f.readline(1)
        print('seviene')
        print(sn)
        reading_meter(SN)
        try:
            uploadloc(r'vals/temp.txt')
        except Exception as e: 
        # Save the error message to a file 
            s=open(r'vals/temp.txt')
            q=str(s.read())
            with open(r'vals/error_logloc.txt', 'a') as l: 
                l.write(str(e) + '\n')
            print('not able to upload locally')
            with open(r'vals/failedlqueries.txt', 'a') as l: 
                l.write(str(encript(q)) + '\n')
        try :
            uploadcloud(r'vals/temp.txt')
        except Exception as e:
            s=open(r'vals/temp.txt')
            q=str(s.read())
            print (q)
            with open(r'vals/error_logcloud.txt', 'a') as l: 
                l.write(str(e) + '\n')
            print('not able to upload to cloud')
            with open(r'vals/failedcqueries.txt', 'a') as l: 
                l.write(str(((q))) + 'mlgsmg')
        os.remove(r'vals/temp.txt')
    else :
        print('run imprint')
    if os.path.exists(r'vals/failedcqueries.txt'):
            t=open(r'vals/failedcqueries.txt')
            text=str(t.read())
            print (text.split('mlgsmg'))
            for a in text.split('mlgsmg'):
                try:
                    print(encript(a))
                    print('sent 1')
                    uploadcloudback(str((a)))
                    text.strip(a)                    
                except Exception as e:
                    with open(r'vals/error_logback.txt', 'a') as l: 
                        l.write(str(e) + '\n')
                    print('not able to upload unuploaded queries')
            os.remove(r'vals/failedcqueries.txt')
            a=open(r'vals/failedcqueries.txt','x')
            a.write(text)

