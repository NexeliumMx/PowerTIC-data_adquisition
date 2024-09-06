import client from '../tests/dbCredentials.js'; // Import the PostgreSQL client
import moment from 'moment-timezone'; // Import moment-timezone

// Function to fetch and format the latest timestamp
async function fetchTimestamp(timezone = 'America/Mexico_City') {
  try {
    // Query the latest timestamp from the 'measurements' table
    const result = await client.query('SELECT timestamp FROM "powertic"."measurements" ORDER BY idmeasurements DESC LIMIT 1;');
    const originalTimestamp = result.rows[0].timestamp;
    
    // Format the timestamp
    return formatTimestamp(originalTimestamp, timezone);
  } catch (error) {
    console.error('Error fetching timestamp:', error);
    throw error; // Throw the error to handle it in the calling function
  }
}

// Helper function to format the timestamp using moment-timezone
function formatTimestamp(timestamp, timezone) {
  const months = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
  ];

  // Convert the UTC timestamp to local time in the provided timezone
  const localDate = moment.utc(timestamp).tz(timezone);

  // Extract day, month, year, hours, and minutes
  const day = localDate.format('DD');
  const month = months[localDate.month()]; // Get the month name from the array
  const year = localDate.format('YYYY');
  const hours = localDate.format('HH');
  const minutes = localDate.format('mm');

  return `${day} de ${month} de ${year} ${hours}:${minutes}`;
}

export default fetchTimestamp; // Export the fetchTimestamp function