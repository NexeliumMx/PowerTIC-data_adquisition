/**
 * This script writes the contents of examplePowerMeterReading.js to Firestore.
 * The script prompts the user to choose between writing to a default path or 
 * providing a custom path. The document ID is generated based on the current timestamp.
 * The path used is either the default path or the user-provided path, 
 * both ending with /E3T150600001/readings.
 */

// Import the Firebase app and other required functions from firebaseSDK.js
import app from '../firebaseSDK.js';
import { getFirestore, collection, doc, setDoc} from 'firebase/firestore';

// Initialize Firestore
const db = getFirestore(app);


// Call the function to write the power meter readings
writePowerMeterReadings();