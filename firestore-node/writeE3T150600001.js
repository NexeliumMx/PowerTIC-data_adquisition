// Import the Firebase SDK
const { initializeApp } = require("firebase/app");
const { getFirestore, collection, addDoc, serverTimestamp } = require("firebase/firestore");

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

// Data to be written to Firestore
const data = {
  "Current A": 0,
  "Current B": 0,
  "Current C": 0,
  "Date": "2024-07-26",
  "PF": 1000,
  "Power": 0,
  "Time": "14:23:03",
  "VAR": 0,
  "Voltage AN": 0,
  "Voltage BN": 0,
  "Voltage CN": 0,
  "timestamp": serverTimestamp()
};

// Function to write the data 5 times to Firestore
async function writeData() {
  const collectionRef = collection(db, 'PowerMeters', 'E3T150600001', 'Measures');
  
  for (let i = 0; i < 5; i++) {
    await addDoc(collectionRef, data);
  }

  console.log('Data written 5 times to Firestore with unique IDs.');
}

// Run the function
writeData()
  .then(() => {
    console.log('Process completed successfully.');
    process.exit(0);
  })
  .catch((error) => {
    console.error('Error writing data:', error);
    process.exit(1);
  });