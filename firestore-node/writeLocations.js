// Import the Firebase SDK
const { initializeApp } = require("firebase/app");
const { getFirestore, collection, doc, setDoc } = require("firebase/firestore");
const { LOCATIONS_AND_POWERMETERS } = require("./medidores.js");

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

// Function to write locations and power meters to Firestore
async function writeLocationsAndPowerMeters() {
  for (const location of LOCATIONS_AND_POWERMETERS) {
    const locationRef = doc(db, 'Location', location.Location);
    const powerMetersCollectionRef = collection(locationRef, 'PowerMeter');
    
    for (const powerMeter of location.PowerMeters) {
      const powerMeterDocRef = doc(powerMetersCollectionRef, powerMeter);
      await setDoc(powerMeterDocRef, { id: powerMeter });
    }
  }

  console.log('Locations and PowerMeters written to Firestore.');
}

// Run the function
writeLocationsAndPowerMeters()
  .then(() => {
    console.log('Process completed successfully.');
    process.exit(0);
  })
  .catch((error) => {
    console.error('Error writing data:', error);
    process.exit(1);
  });