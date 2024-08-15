import firebase_admin
from firebase_admin import credentials,db
import os 
import time
from Firestore_subroutine import imprint,upload
from Coms import reading_meter,meter_param
print("start")

cred = credentials.Certificate("Rapberry/power-tic-firebase-adminsdk-9u1tt-ce3f981b49.json")
if  not os.path.isfile('Rapberry\\settingsData.json'):
    print("entre")
    while (1):
        SN=meter_param('powertic.modbusqueries')
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
        upload(reading_meter('powertic.modbusqueries',SN),SN)
        timeRead=time.time()
        print("lei")


