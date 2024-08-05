/**
 * This script connects to the Firebase Firestore database, extracts all the document IDs
 * inside the "/locations" collection, and returns them.
 *
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-08-03, by Arturo Vargas Cuevas
 */

// Import the Firebase app and other required functions from firebaseSDK.mjs
import app from '../../../firebaseSDK.mjs';
import { getFirestore, collection, getDocs } from 'firebase/firestore';

// Initialize Firestore
const db = getFirestore(app);

// Function to get locations from Firestore
async function getLocations() {
  try {
    // Reference the collection
    const locationsRef = collection(db, "locations");

    // Get all documents in the collection
    const locationsSnapshot = await getDocs(locationsRef);

    // Extract document IDs
    const locationIds = locationsSnapshot.docs.map(doc => doc.id);

    // Return document IDs
    return locationIds;
  } catch (error) {
    console.error("Error getting locations: ", error);
    return [];
  }
}

export default getLocations;