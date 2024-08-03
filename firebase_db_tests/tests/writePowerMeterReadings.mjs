// Import the Firebase app and other required functions from firebaseSDK.mjs
import app from '../firebaseSDK.mjs';
import { getFirestore, collection, doc, setDoc, serverTimestamp } from 'firebase/firestore';
import powerMeterReading from '../scripts/powerMeterReading.js';
import writePowerMeterPath from '../scripts/writePowerMeterPath.js';

// Initialize Firestore
const db = getFirestore(app);

async function writePowerMeterReadings() {
  try {
    // Generate a timestamp-based document ID
    const now = new Date();
    const docId = now.toISOString().replace(/[:.]/g, '-'); // e.g., "2024-08-03T10-17-52-123Z"

    // Reference the sub-collection
    const readingsCollection = collection(db, writePowerMeterPath);

    // Add server timestamp to the reading
    powerMeterReading.timestamp_server = serverTimestamp();

    // Write the powerMeterReading object to the sub-collection with the generated ID
    await setDoc(doc(readingsCollection, docId), powerMeterReading);

    console.log("Power meter reading written successfully");
  } catch (error) {
    console.error("Error writing power meter reading: ", error);
  } finally {
    // Exit the process
    process.exit();
  }
}

// Call the function to write the power meter readings
writePowerMeterReadings();