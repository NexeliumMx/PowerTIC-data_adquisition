// Import the Firestore instance
const { db } = require("..firebaseSDK.js");
const { collection, addDoc } = require("firebase/firestore");
const { LOCATIONS_AND_POWERMETERS } = require("./assets/medidores.js");
const { data } = require("./assets/data.js");

// Function to write the data 5 times to Firestore for each PowerMeter
async function writeData() {
  for (const location of LOCATIONS_AND_POWERMETERS) {
    for (const powerMeter of location.PowerMeters) {
      const collectionRef = collection(db, 'PowerMeters', powerMeter, 'Measures');
      for (let i = 0; i < 5; i++) {
        await addDoc(collectionRef, data);
      }
    }
  }

  console.log('Data written 5 times to Firestore for each PowerMeter.');
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