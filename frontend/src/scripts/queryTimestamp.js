import client from './dbCredentials.js';

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
  const hours = String(date.getHours() - 5).padStart(2, '0'); // Adjusting for UTC-5 (Mexico City time)
  const minutes = String(date.getMinutes()).padStart(2, '0');

  return `${day} de ${month} de ${year} ${hours}:${minutes}`;
}

// Function to get the latest timestamp
async function getFormattedTimestamp() {
  await client.connect();

  try {
    const query = 'SELECT timestamp FROM "powertic"."measurements" ORDER BY idmeasurements DESC LIMIT 1;';
    const result = await client.query(query);
    
    if (result.rows.length > 0) {
      const originalTimestamp = result.rows[0].timestamp;
      return formatTimestamp(originalTimestamp);
    } else {
      throw new Error('No records found in the table.');
    }
  } catch (error) {
    console.error('Error executing query', error);
  } finally {
    client.end();
  }
}

// Export the formatted timestamp as a module
export default getFormattedTimestamp;