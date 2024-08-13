/**
 * This script writes the contents of examplePowerMeterReading.js to Firestore.
 * The script prompts the user to choose between writing to a default path or 
 * providing a custom path. The document ID is generated based on the current timestamp.
 * The path used is either the default path or the user-provided path, 
 * both ending with /E3T150600001/readings.
 */


// Import the Firebase app and other required functions from firebaseSDK.js
import app from '../firebaseSDK.js';
import { getFirestore, collection, doc, setDoc } from 'firebase/firestore';
import fs from 'fs';
import path from 'path';
import csv from 'csv-parser';

// Initialize Firestore
const db = getFirestore(app);

const filePath = path.join(process.cwd(), '../Acurev1313_ModbusAddresses/readings_addresses.csv');
const collectionPath = '/power_meters/power_readings/AVC27050001';

// Function to read parameter descriptions from CSV and write to Firestore
function writeParameterDescriptionsToFirestore() {
    const parameterDescriptions = [];

    // Read CSV file
    fs.createReadStream(filePath)
        .pipe(csv())
        .on('data', (row) => {
            const description = row['parameter_description'];
            if (description && description.trim()) {
                parameterDescriptions.push(description);
            }
        })
        .on('end', async () => {
            console.log('Writing to Firestore...');

            // Get the current timestamp without milliseconds
            const timestamp = new Date().toISOString().split('.')[0] + 'Z';
            const value = 0;

            for (const description of parameterDescriptions) {
                try {
                    const docRef = doc(db, collectionPath, description);
                    await setDoc(docRef, {
                        [timestamp]: value
                    });
                    console.log(`Written ${description} with timestamp ${timestamp} and value ${value}`);
                } catch (error) {
                    console.error(`Error writing ${description}:`, error);
                }
            }

            console.log('Writing completed.');
        });
}

// Execute the function
writeParameterDescriptionsToFirestore();