import firebase_admin
from firebase_admin import credentials,db
import os 

import time
from Firestore_subroutine import imprint,upload
from ModCom2 import reading_meter,meterParam
print("start")
#nuevocomentario
cred = credentials.Certificate("/home/power-tic/MICO/PowerTIC/Rapberry/power-tic-firebase-adminsdk-9u1tt-ce3f981b49.json")
if  os.path.isfile('Rapberry\\settingsData.json'):
    print("entre")
    while (1):
        SN=meterParam()
        if not (SN==None):
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://power-tic-default-rtdb.firebaseio.com/'
            })
            imprint(SN)
            ref = db.reference('/Meters').child(SN).set({'status':True})
            
            break
timeRead=0
while (1):  

    if time.time()-timeRead >299:
        upload(reading_meter(),SN)
        timeRead=time.time()
        print("lei")


