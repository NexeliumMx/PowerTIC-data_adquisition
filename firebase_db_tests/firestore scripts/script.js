// Import the Firebase app and other required functions from firebaseSDK.js
import app from '../firebaseSDK.js';
import { getFirestore, doc, updateDoc } from 'firebase/firestore';
import fs from 'fs';
import path from 'path';
import csv from 'csv-parser';

// Initialize Firestore
const db = getFirestore(app);

const filePath = path.join(process.cwd(), '../Acurev1313_ModbusAddresses/readings_addresses.csv');
const baseCollectionPath = '/power_meters/power_readings/';

function getCurrentTimestamp() {
    return new Date().toISOString().split('.')[0] + 'Z';
}

// Function to update data in Firestore for a range of power meter IDs
async function updateFirestoreForMeter(meterId, parameterDescriptions) {
    const timestamp = getCurrentTimestamp();
    const value = 0;

    for (const description of parameterDescriptions) {
        try {
            const docRef = doc(db, `${baseCollectionPath}${meterId}`, description);
            // Use updateDoc instead of setDoc to add a new field (timestamp) to the document
            await updateDoc(docRef, {
                [timestamp]: value
            });
            console.log(`Updated ${description} in ${meterId} with timestamp ${timestamp} and value ${value}`);
        } catch (error) {
            console.error(`Error updating ${description} in ${meterId}:`, error);
        }
    }
}

// Function to perform the update process for all meters
async function performUpdates(parameterDescriptions) {
    console.log('Updating Firestore...');
    for (let i = 1; i <= 9; i++) {
        const meterId = `AVC2705000${i}`;
        await updateFirestoreForMeter(meterId, parameterDescriptions);
    }
    console.log('Update completed.');
}

// Function to read parameter descriptions from CSV and initiate update process
function updateParameterDescriptionsInFirestore() {
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
            console.log('Starting Firestore updates...');

            // Perform an immediate update
            await performUpdates(parameterDescriptions);

            // Then set up an interval to update every five minutes
            setInterval(async () => {
                await performUpdates(parameterDescriptions);
            }, 5 * 60 * 1000); // 5 minutes in milliseconds
        });
}

// Execute the function
updateParameterDescriptionsInFirestore();