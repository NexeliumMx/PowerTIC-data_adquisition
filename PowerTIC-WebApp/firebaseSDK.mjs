// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDrK5vgZxLgU_7MFYCFu3oOIRSAgoc9XiU",
  authDomain: "power-tic.firebaseapp.com",
  projectId: "power-tic",
  storageBucket: "power-tic.appspot.com",
  messagingSenderId: "1076041377760",
  appId: "1:1076041377760:web:b03cd97613eed942a16d85",
  measurementId: "G-QRCSX7C51E"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
//const analytics = getAnalytics(app);

export default app;
//export { analytics };