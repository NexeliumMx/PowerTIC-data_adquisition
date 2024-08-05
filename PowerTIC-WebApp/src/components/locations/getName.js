// /src/components/locations/getName.js

/**
 * This script connects to the Firebase Firestore database, extracts the "name" field
 * inside the specified document in the "/locations" collection, and returns it.
 *
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-08-03, by Arturo Vargas Cuevas
 */

// Import the Firebase app and other required functions from firebaseSDK.mjs
import app from '../../../firebaseSDK.mjs';
import { getFirestore, doc, getDoc } from 'firebase/firestore';

// Initialize Firestore
const db = getFirestore(app);

// Function to get the name from Firestore
async function getName(location) {
  try {
    // Reference the document
    const locationDoc = doc(db, "locations", location);

    // Get the document
    const locationSnapshot = await getDoc(locationDoc);

    // Extract the "name" field
    if (locationSnapshot.exists()) {
      const name = locationSnapshot.data().name;
      return name;
    } else {
      console.error("No such document!");
      return null;
    }
  } catch (error) {
    console.error("Error getting location name: ", error);
    return null;
  }
}

export default getName;