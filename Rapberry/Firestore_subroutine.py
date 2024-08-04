import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import time
def upload(Json_Path,SerialNumber):
    db = firestore.client()
    doc_ref = db.document('power_meters/power_readings')
    doc_ref = doc_ref.collection(str(SerialNumber))

    f = open(Json_Path)
    data = json.load(f)
    for i in data:
        doc_ref.document(i).set({data["timestamp_power_meter"]: data[i]},merge=True)

    f.close()
    
def imprint(Json_Path,SerialNumber):
    cred = credentials.Certificate('Rapberry/power-tic-firebase-adminsdk-9u1tt-ce3f981b49.json')
    firebase_admin.initialize_app(cred)
    from pathlib import Path
    PROJECT_DIR = Path(__file__).parent
    db = firestore.client()
    doc_ref = db.document('power_meters/power_readings')
    doc_ref = doc_ref.collection(str(SerialNumber))
    doc_ref.document('meter_data').set(json.load(open(PROJECT_DIR/'meterData.json')))
    f = open(Json_Path)
    data = json.load(f)
    for i in data:
        doc_ref.document(i).set({'exists': True})

    f.close()