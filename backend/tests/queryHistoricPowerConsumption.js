/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and retrieves the latest 14 values of
 * 'total_real_energy_imported' and 'total_var_hours_imported_q1' from the "powertic.measurements" table.
 * 
 * It calculates the difference in energy (kWh) and reactive energy (kVArh) consumed
 * between each 5-minute period over the past hour and prints the results to the terminal.
 * 
 * Output:
 * - First, it prints 13 values for total_real_energy_imported in kWh for each 5-minute period.
 * - Then, it prints 13 values for total_var_hours_imported_q1 in kVArh for each 5-minute period.
 * - Both series will have a final value at the -60 minute mark.
 */

import client from './dbCredentials.js';

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest 14 readings for total_real_energy_imported and total_var_hours_imported_q1
    const query = `
      SELECT total_real_energy_imported, total_var_hours_imported_q1, timestamp
      FROM "powertic"."measurements"
      ORDER BY timestamp DESC
      LIMIT 14;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length === 14) {
      // Arrays to store differences for both total_real_energy_imported and total_var_hours_imported_q1
      const kWhConsumptionDifferences = [];
      const kVArhConsumptionDifferences = [];

      // Initial previous readings for both energy and reactive energy
      let previousKWhReading = result.rows[0].total_real_energy_imported;
      let previousKVarhReading = result.rows[0].total_var_hours_imported_q1;

      // Loop through the result set and compute the differences for each 5-minute period
      for (let i = 1; i < result.rows.length; i++) {
        const currentKWhReading = result.rows[i].total_real_energy_imported;
        const currentKVarhReading = result.rows[i].total_var_hours_imported_q1;

        // Calculate consumption for each 5-minute period
        const kWhConsumption = (previousKWhReading - currentKWhReading) / 1000;  // Convert Wh to kWh
        const kVArhConsumption = (previousKVarhReading - currentKVarhReading) / 1000;  // Convert VAh to kVArh

        // Store the computed values
        kWhConsumptionDifferences.push(kWhConsumption.toFixed(3));
        kVArhConsumptionDifferences.push(kVArhConsumption.toFixed(3));

        // Update previous readings for next iteration
        previousKWhReading = currentKWhReading;
        previousKVarhReading = currentKVarhReading;
      }

      // Print the WattHours (kWh) consumption differences
      console.log("Historic Consumption / Consumo histórico");
      console.log("total_real_energy_imported:");
      kWhConsumptionDifferences.forEach((consumption, index) => {
        console.log(`-${index * 5} min: ${consumption} kWh`);
      });

      // Print the -60 min reading for kWh
      console.log("-60 min: 0 kWh");

      // Print the Volt-Ampere hours (kVArh) consumption differences
      console.log("\ntotal_var_hours_imported_q1:");
      kVArhConsumptionDifferences.forEach((consumption, index) => {
        console.log(`-${index * 5} min: ${consumption} kVArh`);
      });

      // Print the -60 min reading for kVArh
      console.log("-60 min: 0 kVArh");
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