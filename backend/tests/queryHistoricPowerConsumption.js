/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and retrieves the latest 14 values of
 * 'total_real_energy_imported' and 'total_va_hours_imported' from the "powertic.measurements" table.
 * 
 * It calculates the difference in WattHours (Wh) and Volt-Ampere hours (VAh) consumed
 * between each 5-minute period over the past hour and prints the results to the terminal.
 * 
 *  Output:
 * - First, it prints 14 values for WattHours (Wh) consumed in each 5-minute period.
 * - Then, it prints 14 values for Volt-Ampere hours (VAh) consumed in each 5-minute period.
 */

import client from './dbCredentials.js';

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest 14 readings for total_real_energy_imported and total_va_hours_imported
    const query = `
      SELECT total_real_energy_imported, total_va_hours_imported, timestamp
      FROM "powertic"."measurements"
      ORDER BY timestamp DESC
      LIMIT 14;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length === 14) {
      // Arrays to store differences for both total_real_energy_imported and total_va_hours_imported
      const whConsumptionDifferences = [];
      const vahConsumptionDifferences = [];

      // Initial previous readings for both energy and VA
      let previousWhReading = result.rows[0].total_real_energy_imported;
      let previousVahReading = result.rows[0].total_va_hours_imported;

      // Loop through the result set and compute the differences for each 5-minute period
      for (let i = 1; i < result.rows.length; i++) {
        const currentWhReading = result.rows[i].total_real_energy_imported;
        const currentVahReading = result.rows[i].total_va_hours_imported;

        // Calculate consumption for each 5-minute period
        const whConsumption = previousWhReading - currentWhReading;  // Difference in Wh
        const vahConsumption = previousVahReading - currentVahReading;  // Difference in VAh

        // Store the computed values
        whConsumptionDifferences.push(whConsumption);
        vahConsumptionDifferences.push(vahConsumption);

        // Update previous readings for next iteration
        previousWhReading = currentWhReading;
        previousVahReading = currentVahReading;
      }

      // Print the WattHours (Wh) consumption differences
      console.log("WattHours (Wh) consumption:");
      whConsumptionDifferences.forEach((consumption, index) => {
        console.log(`-${index * 5} min: ${consumption} Wh`);
      });

      // Print the -60 min reading for Wh
      console.log("-60 min: 0 Wh");

      // Print the Volt-Ampere hours (VAh) consumption differences
      console.log("\nVolt-Ampere Hours (VAh) consumption:");
      vahConsumptionDifferences.forEach((consumption, index) => {
        console.log(`-${index * 5} min: ${consumption} VAh`);
      });

      // Print the -60 min reading for VAh
      console.log("-60 min: 0 VAh");
    } else {
      console.log('Not enough data points found in the table.');
    }
  })
  .catch(err => {
    console.error('Error executing query', err.stack);
  })
  .finally(() => {
    // Close the database connection
    client.end();
  });