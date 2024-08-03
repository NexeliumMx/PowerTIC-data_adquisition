// Import the Firestore instance
const { db } = require("../firebaseSDK.js");
const { collection, doc, setDoc } = require("firebase/firestore");
const { LOCATIONS_AND_POWERMETERS } = require("./assets/medidores.js");

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