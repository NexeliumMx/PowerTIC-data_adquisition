import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
from pathlib import Path
def upload(Json_Path,SerialNumber):
    db = firestore.client()
    doc_ref = db.document('power_meters/power_readings')
    doc_ref = doc_ref.collection(str(SerialNumber))

    f = open(Json_Path)
    data = json.load(f)
    for i in data:
        print(i)
        doc_ref.document(i).set({data["timestamp"]: data[i]},merge=True)

    f.close()
    
def imprint(SerialNumber):
    PROJECT_DIR = Path(__file__).parent
    db = firestore.client()
    doc_ref = db.document('power_meters/power_readings')
    doc_ref = doc_ref.collection(str(SerialNumber))
    doc_ref.document('meter_data').set(json.load(open(PROJECT_DIR/'meterData.json')))
    f = open(PROJECT_DIR/'.powerReadingsLocal.json')
    data = json.load(f)
    for i in data:
        doc_ref.document(i).set({'exists': True})

    f.close()