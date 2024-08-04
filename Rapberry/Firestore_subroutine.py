import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import time

start = time.time()

cred = credentials.Certificate('Rapberry/power-tic-firebase-adminsdk-9u1tt-ce3f981b49.json')
firebase_admin.initialize_app(cred)

db = firestore.client()



doc_ref = db.collection('power_meters/power_readings/E3T150600001')

f = open('Rapberry/examplePowermeterReadings.json')
data = json.load(f)
for i in data:
    doc_ref.document(i).set({data["timestamp_power_meter"]: data[i]},merge=True)

f.close()

end = time.time()
print(end - start)
