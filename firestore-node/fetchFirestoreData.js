const { initializeApp } = require("firebase/app");
const { getFirestore, collection, getDocs } = require("firebase/firestore");
const readline = require("readline");
const fs = require("fs");

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

// Function to get all documents from a collection
async function getAllDocuments(collectionName) {
  try {
    const querySnapshot = await getDocs(collection(db, collectionName));
    const documents = [];
    querySnapshot.forEach((doc) => {
      documents.push({ id: doc.id, data: doc.data() });
    });

    // Write to JSON file
    fs.writeFile(`${collectionName}.json`, JSON.stringify(documents, null, 2), (err) => {
      if (err) {
        console.error("Error writing to file", err);
      } else {
        console.log(`Data successfully written to ${collectionName}.json`);
      }
    });
  } catch (error) {
    console.error("Error getting documents: ", error);
  }
}

// Ask for the collection name
rl.question("Name of the collection to download: ", (collectionName) => {
  getAllDocuments(collectionName).finally(() => rl.close());
});