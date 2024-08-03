const { serverTimestamp } = require("firebase/firestore");
const { RANDOM_DATA_THRESHOLDS } = require("./randomThresholds");

function getRandomValue([min, max]) {
  return (Math.random() * (max - min) + min).toFixed(2);
}

function getRandomDate() {
  const start = new Date(2024, 0, 1);
  const end = new Date(2024, 11, 31);
  return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime())).toISOString().split('T')[0];
}

function getRandomTime() {
  const hours = String(Math.floor(Math.random() * 24)).padStart(2, '0');
  const minutes = String(Math.floor(Math.random() * 60)).padStart(2, '0');
  const seconds = String(Math.floor(Math.random() * 60)).padStart(2, '0');
  return `${hours}:${minutes}:${seconds}`;
}

const data = {
  "Current A": getRandomValue(RANDOM_DATA_THRESHOLDS.Currents),
  "Current B": getRandomValue(RANDOM_DATA_THRESHOLDS.Currents),
  "Current C": getRandomValue(RANDOM_DATA_THRESHOLDS.Currents),
  "Date": getRandomDate(),
  "PF": getRandomValue(RANDOM_DATA_THRESHOLDS.PF),
  "Power": getRandomValue(RANDOM_DATA_THRESHOLDS.Power),
  "Time": getRandomTime(),
  "VAR": getRandomValue(RANDOM_DATA_THRESHOLDS.VAR),
  "Voltage AN": getRandomValue(RANDOM_DATA_THRESHOLDS.Voltages),
  "Voltage BN": getRandomValue(RANDOM_DATA_THRESHOLDS.Voltages),
  "Voltage CN": getRandomValue(RANDOM_DATA_THRESHOLDS.Voltages),
  "timestamp": serverTimestamp()
};

module.exports = { data };