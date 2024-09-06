/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and fetches the latest timestamp
 * from the "powertic.measurements" table. It then converts and formats the timestamp
 * to display the date in "DD de Month de YYYY HH:MM" format, adjusting for the user's
 * current local time zone based on their computer's settings.
 * 
 * The result is printed directly to the terminal.
 * 
 * Output:
 * - The formatted timestamp is printed in the user's local time zone.
 */

import client from './dbCredentials.js';

// Helper function to format the timestamp and adjust it to the local time zone
function formatTimestamp(timestamp) {
  const months = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
  ];

  // Convert the timestamp from UTC to local time zone
  const date = new Date(timestamp);

  // Get the local time zone offset and adjust the timestamp accordingly
  const localDate = date.toLocaleString('default', {
    timeZoneName: 'short'
  });

  const day = String(date.getDate()).padStart(2, '0');
  const month = months[date.getMonth()];
  const year = date.getFullYear();
  const hours = String(date.getHours()).padStart(2, '0'); // Automatically adjusted to local time
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

      // Convert and format the timestamp using the user's local time zone
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