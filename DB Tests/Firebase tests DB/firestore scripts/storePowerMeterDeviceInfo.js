/**
 * This script writes the contents of examplePowerMeterSettings.mjs to Firestore.
 * The document is named using the SN (Serial Number) property from the settings object.
 * The path used is /power_meters_settings/{SN}.
 */

// Import the Firebase app and other required functions from firebaseSDK.mjs
import app from '../firebaseSDK.mjs';
import { getFirestore, doc, setDoc } from 'firebase/firestore';
import examplePowerMeterSettings from '../json data/examplePowerMeterSettings.js';

// Initialize Firestore
const db = getFirestore(app);

// PowerMeter Settings Path
const writePowerMeterSettingsPath = "/power_meters_settings";

// Write to Database
async function writePowerMeterSettings() {
  try {
    // Extract the SN property to use as the document name
    const { SN } = examplePowerMeterSettings;

    // Reference the document
    const settingsDoc = doc(db, writePowerMeterSettingsPath, SN);

    // Write the examplePowerMeterSettings object to the document
    await setDoc(settingsDoc, examplePowerMeterSettings);

    console.log(`Power meter settings written successfully in ${writePowerMeterSettingsPath}/${SN}\n`);
  } catch (error) {
    console.error("Error writing power meter settings: ", error);
  } finally {
    // Exit the process
    process.exit();
  }
}

// Call the function to write the power meter settings
writePowerMeterSettings();