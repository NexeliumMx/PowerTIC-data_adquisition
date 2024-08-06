from Firestore_subroutine import upload,imprint
import firebase_admin
from firebase_admin import credentials,db
import os 

import time
from Firestore_subroutine import imprint,upload
from ModCom2 import reading_meter,meterParam
cred = credentials.Certificate("/home/guillermo/MICO/PowerTIc/PowerTIC/Rapberry/power-tic-firebase-adminsdk-9u1tt-ce3f981b49.json")
firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://power-tic-default-rtdb.firebaseio.com/'
            })
upload('/home/guillermo/MICO/PowerTIc/PowerTIC/Rapberry/meter_data.json','pruebamesta')