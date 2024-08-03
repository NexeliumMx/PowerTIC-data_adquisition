/**
 * This script writes the contents of examplePowerMeterReading.js to Firestore.
 * The script prompts the user to choose between writing to a default path or 
 * providing a custom path. The document ID is generated based on the current timestamp.
 * The path used is either the default path or the user-provided path, 
 * both ending with /E3T150600001/readings.
 */

// Import the Firebase app and other required functions from firebaseSDK.mjs
import app from '../firebaseSDK.mjs';
import { getFirestore, collection, doc, setDoc, serverTimestamp } from 'firebase/firestore';
import examplePowerMeterReading from '../constants/examplePowerMeterReading.js';
import readline from 'readline';

// Initialize Firestore
const db = getFirestore(app);

// Import Power Meter Reading
const powerMeterReading = examplePowerMeterReading;

// Default PowerMeter Path
const defaultPath = "power_meters_readings/E3T150600001/readings";

// Create an interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Function to prompt the user
function promptUser(query) {
  return new Promise((resolve) => rl.question(query, resolve));
}

// Function to determine the write path
async function determineWritePath() {
  const userInput = await promptUser("Write in default path? 'power_meters_readings' (Y/N): ");

  if (["y", "Y", "yes", "Yes"].includes(userInput)) {
    return defaultPath;
  } else if (["n", "N", "no", "No"].includes(userInput)) {
    const userPath = await promptUser("Please input the desired path (e.g., 'power_readings'): ");
    return `${userPath}/E3T150600001/readings`;
  } else {
    console.log("Invalid input. Please enter 'Y' or 'N'.");
    return determineWritePath(); // Recursive call for invalid input
  }
}

// Write to DataBase
async function writePowerMeterReadings() {
  try {
    const writePowerMeterPath = await determineWritePath();

    // Generate a timestamp-based document ID
    const now = new Date();
    const docId = now.toISOString().replace(/[:.]/g, '-'); // e.g., "2024-08-03T10-17-52-123Z"

    // Reference the sub-collection
    const readingsCollection = collection(db, writePowerMeterPath);

    // Add server timestamp to the reading
    powerMeterReading.timestamp_server = serverTimestamp();

    // Write the powerMeterReading object to the sub-collection with the generated ID
    await setDoc(doc(readingsCollection, docId), powerMeterReading);

    console.log(`Power meter reading written successfully in ${writePowerMeterPath}\n`);
  } catch (error) {
    console.error("Error writing power meter reading: ", error);
  } finally {
    // Close the readline interface and exit the process
    rl.close();
    process.exit();
  }
}

// Call the function to write the power meter readings
writePowerMeterReadings();