/**
 * This script writes the contents of acuRev13003P4WEnergyMeterFormat.mjs to Firestore.
 * The document is named using the documentName property from the format object.
 * The path used is /power_meters_formats/{documentName}.
 */

// Import the Firebase app and other required functions from firebaseSDK.mjs
import app from '../firebaseSDK.mjs';
import { getFirestore, doc, setDoc } from 'firebase/firestore';
import { brand, documentName, powerMeterOutputFormat } from '../json data/acuRev13003P4WEnergyMeterFormat.mjs';

// Initialize Firestore
const db = getFirestore(app);

// PowerMeter Format Path
const writePowerMeterFormatPath = `/power_meters_formats/`;

// Write to Database
async function writePowerMeterFormat() {
  try {
    // Reference the document
    const formatDoc = doc(db, writePowerMeterFormatPath, documentName);

    // Write the powerMeterOutputFormat object to the document
    await setDoc(formatDoc, powerMeterOutputFormat);

    console.log(`Power meter format written successfully in ${writePowerMeterFormatPath}/${documentName}\n`);
  } catch (error) {
    console.error("Error writing power meter format: ", error);
  } finally {
    // Exit the process
    process.exit();
  }
}

// Call the function to write the power meter format
writePowerMeterFormat();