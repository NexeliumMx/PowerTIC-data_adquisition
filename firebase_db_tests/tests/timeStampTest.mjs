// Import the Firebase app and other required functions from firebaseSDK.mjs
import app from '../firebaseSDK.mjs';
import { getFirestore, doc, setDoc, serverTimestamp } from 'firebase/firestore';

// Initialize Firestore
const db = getFirestore(app);

async function writeTimestamp() {
  try {
    // Reference the document
    const docRef = doc(db, "time_stamp_test", "mMWZMmtcQ833IM5Ov3bW");

    // Write the timestamp
    await setDoc(docRef, {
      timestamp: serverTimestamp(),
    });

    console.log("Timestamp written successfully");
  } catch (error) {
    console.error("Error writing timestamp: ", error);
  } finally {
    // Exit the process
    process.exit();
  }
}

// Call the function to write the timestamp
writeTimestamp();