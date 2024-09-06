/**
 * Author: Rogelio Akin Leon Garcia & Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and queries the maximum values for
 * 'total_real_power' and 'reactive_power_var' from the "powertic.measurements" table.
 * 
 * The results are printed directly to the terminal in the format:
 * Maximum Demand / Demanda Máxima
 * - Total Real Power (W): <value>
 * - Reactive Power (VAR): <value>
 */

import client from './dbCredentials.js';

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the maximum values for total_real_power and reactive_power_var
    const query = `
      SELECT MAX(total_real_power) AS max_total_real_power, 
             MAX(reactive_power_var) AS max_reactive_power_var
      FROM "powertic"."measurements";
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      const row = result.rows[0];
      const maxTotalRealPower = (row.max_total_real_power / 1000).toFixed(3); // Divide by 1000 and format to 3 decimal places
      const maxReactivePowerVar = (row.max_reactive_power_var / 1000).toFixed(3); // Divide by 1000 and format to 3 decimal places

      // Print the results in the specified format
      console.log("Maximum Demand / Demanda Máxima:");
      console.log(`Total Real Power: ${maxTotalRealPower} kW`);
      console.log(`Reactive Power: ${maxReactivePowerVar} kVAR`);
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