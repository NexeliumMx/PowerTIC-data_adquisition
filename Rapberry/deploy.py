import firebase_admin
from firebase_admin import credentials,db
import os 

import time
from Firestore_subroutine import imprint,upload
#from ModCom2 import reading_meter,meterParam
cred = credentials.Certificate("Rapberry\\power-tic-firebase-adminsdk-9u1tt-ce3f981b49.json")
if os.path.isfile('Rapberry\\meterData.json'):
    while (1):
        SN='meterParam()'
        if not (SN==None):
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://power-tic-default-rtdb.firebaseio.com/'
            })
            imprint(SN)
            ref = db.reference('/Meters').child(SN).set({'status':True})
            
            break
#while (1):  
    #reading_meter()
