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

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest timestamp from the powertic.measurements table
    const query = 'SELECT timestamp FROM "powertic"."measurements" ORDER BY idmeasurements DESC LIMIT 1;';

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      const originalTimestamp = result.rows[0].timestamp;

      // Convert and format the timestamp
      const formattedTimestamp = formatTimestamp(originalTimestamp);
      console.log(formattedTimestamp);
    } else {
      console.log('No records found in the table.');
    }
  })
  .catch(err => {
    console.error('Error executing query', err.stack);
  })
  .finally(() => {
    // Close the database connection
    client.end();
  });