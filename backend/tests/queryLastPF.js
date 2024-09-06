/**
 * Author: Rogelio Akin Leon Garcia
 * Last Modified: 2024-09-06, by Rogelio Akin Leon Garcia
 * 
 * This script connects to the PostgreSQL database and fetches the latest power factor value
 * from the "powertic.measurements" table.
 * 
 * The result is normalized from -1000 to +1000 to -1 to 1 and printed with a label.
 * 
 *  Output:
 * - The power factor is printed with a descriptive label.
 */

import client from './dbCredentials.js';

// Helper function to normalize the power factor value from -1000 to +1000 to -1 to 1
function normalizePowerFactor(powerFactor) {
  return powerFactor / 1000;
}

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest power_factor from the powertic.measurements table
    const query = 'SELECT power_factor FROM "powertic"."measurements" ORDER BY idmeasurements DESC LIMIT 1;';

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      const powerFactor = result.rows[0].power_factor;

      // Normalize the power factor
      const normalizedPowerFactor = normalizePowerFactor(powerFactor);

      // Print the result with a label
      console.log("Power Factor / Factor de Potencia:");
      console.log(normalizedPowerFactor.toFixed(3)); // Print with 3 decimal places
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