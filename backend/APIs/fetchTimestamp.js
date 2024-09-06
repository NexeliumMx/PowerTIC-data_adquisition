// fetchTimestamp.js
import client from './postgresCredentials.js';

// Function to fetch the latest timestamp from the database
async function fetchTimestamp() {
  try {
    const query = 'SELECT timestamp FROM "powertic"."measurements" ORDER BY idmeasurements DESC LIMIT 1;';
    const result = await client.query(query);

    if (result.rows.length > 0) {
      const originalTimestamp = result.rows[0].timestamp;
      return formatTimestamp(originalTimestamp);
    } else {
      return 'No records found in the table.';
    }
  } catch (error) {
    console.error('Error fetching timestamp:', error.stack);
    throw error;
  }
}

// Helper function to format the timestamp
function formatTimestamp(timestamp) {
  const months = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
  ];

  const date = new Date(timestamp);
  const day = String(date.getDate()).padStart(2, '0');
  const month = months[date.getMonth()];
  const year = date.getFullYear();
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');

  return `${day} de ${month} de ${year} ${hours}:${minutes}`;
}

// Export fetchTimestamp function
export { fetchTimestamp };