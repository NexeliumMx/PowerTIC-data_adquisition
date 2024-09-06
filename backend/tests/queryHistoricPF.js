/**
 * Author: Arturo Vargas Cuevas & Rogelio Akin Leon Garcia
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and fetches the latest 14 values
 * of the 'power_factor' field from the "powertic.measurements" table.
 * 
 * It normalizes the power factor values from -1000 to +1000 to -1 to 1, and prints them
 * to the terminal along with a labeled time interval for each value.
 * 
 *  Output Order:
 * - The values are printed with a time label in descending order, with the most recent 'power_factor' printed first.
 * - It includes the '-60 min' interval.
 */

import client from './dbCredentials.js';

// Helper function to normalize the power factor value from -1000 to +1000 to -1 to 1
function normalizeHistoricPF(HistoricPF) {
  return HistoricPF / 1000;
}

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest 14 power factor values from the powertic.measurements table
    const query = `
      SELECT power_factor
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 14;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      console.log("Historic Power Factor / Factor de Potencia Historico:");
      // Loop through the results, normalize each power_factor value, and print it with a time label
      result.rows.forEach((row, index) => {
        const normalizedPowerFactor = normalizeHistoricPF(row.power_factor);  // Normalize the value
        console.log(`-${index * 5} min: ${normalizedPowerFactor.toFixed(3)}`);
      });
      console.log("-60 min: 1.000");  // Default value for -60 min if needed
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