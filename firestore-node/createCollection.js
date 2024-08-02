const { initializeApp } = require("firebase/app");
const { getFirestore, collection, addDoc } = require("firebase/firestore");
const readline = require("readline");

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDrK5vgZxLgU_7MFYCFu3oOIRSAgoc9XiU",
  authDomain: "power-tic.firebaseapp.com",
  projectId: "power-tic",
  storageBucket: "power-tic.appspot.com",
  messagingSenderId: "1076041377760",
  appId: "1:1076041377760:web:b03cd97613eed942a16d85",
  measurementId: "G-QRCSX7C51E"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

// Create readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Function to create a new collection with a sample document
async function createNewCollection(collectionName) {
  try {
    // Create a new document in the specified collection
    const docRef = await addDoc(collection(db, collectionName), {
      sampleField: "This is a sample document."
    });
    console.log(`Collection '${collectionName}' created with document ID: ${docRef.id}`);
  } catch (error) {
    console.error("Error creating collection: ", error);
  }
}

// Ask for the collection name
rl.question("Name of the Collection to create: ", (collectionName) => {
  createNewCollection(collectionName).finally(() => rl.close());
});