// /src/components/locations/getAssignedPowerMeters.js

/**
 * This script connects to the Firebase Firestore database, extracts the assigned power meters
 * inside the specified document in the "/locations/{location}/assigned_power_meters" collection,
 * and returns them.
 *
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-08-03, by Arturo Vargas Cuevas
 */

// Import the Firebase app and other required functions from firebaseSDK.mjs
import app from '../../../firebaseSDK.js';
import { getFirestore, collection, getDocs } from 'firebase/firestore';

// Initialize Firestore
const db = getFirestore(app);

// Function to get assigned power meters from Firestore
async function getAssignedPowerMeters(location) {
  try {
    // Reference the sub-collection
    const powerMetersRef = collection(db, `locations/${location}/assigned_power_meters`);

    // Get all documents in the sub-collection
    const powerMetersSnapshot = await getDocs(powerMetersRef);

    // Extract document IDs
    const powerMeterIds = powerMetersSnapshot.docs.map(doc => doc.id);

    // Return document IDs
    return powerMeterIds;
  } catch (error) {
    console.error(`Error getting assigned power meters for ${location}: `, error);
    return [];
  }
}

export default getAssignedPowerMeters;