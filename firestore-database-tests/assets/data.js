const { serverTimestamp } = require("firebase/firestore");

const data = {
  "Current A": 0,
  "Current B": 0,
  "Current C": 0,
  "Date": "2024-07-26",
  "PF": 1000,
  "Power": 0,
  "Time": "14:23:03",
  "VAR": 0,
  "Voltage AN": 0,
  "Voltage BN": 0,
  "Voltage CN": 0,
  "timestamp": serverTimestamp()
};

module.exports = { data };