/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and fetches the latest 12 values
 * of the 'power_factor' field from the "powertic.measurements" table.
 * 
 * The results are printed directly to the terminal without any surrounding text or labels.
 * 
 *  Output Order:
 * - The values are printed in descending order, with the most recent 'power_factor' printed first.
 */

import client from './dbCredentials.js';

// Helper function to normalize the power factor value from -1000 to +1000 to -1 to 1
function normalizeHistoricPF(HistoricPF) {
  return HistoricPF / 1000;
}

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest 12 power factor values from the powertic.measurements table
    const query = `
      SELECT power_factor
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 12;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      // Loop through the results, normalize each power_factor value, and print it
      result.rows.forEach(row => {
        const normalizedPowerFactor = normalizeHistoricPF(row.power_factor);  // Normalize the value
        console.log(normalizedPowerFactor);  // Print the normalized value
      });
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