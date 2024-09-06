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
      // Loop through the results and print each power_factor value
      result.rows.forEach(row => {
        console.log(row.power_factor);  // Print each power_factor value
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