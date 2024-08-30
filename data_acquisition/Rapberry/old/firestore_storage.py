import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(r"C:\Users\Luis\OneDrive\Skybox-Smartnet\Projects\PowerTIC\Firebase_PowerTIC\power-tic-firebase-adminsdk-9u1tt-ce3f981b49.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {
    'task': 'Wahs the dishes',
    'status': 'TODO'
}

doc_ref = db.collection('taskCollection').document()
doc_ref.set(data)

print('Document ID', doc_ref.id)