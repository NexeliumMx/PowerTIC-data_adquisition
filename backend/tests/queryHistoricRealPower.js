/**
 * Author: Rogelio Akin Leon Garcia & Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and fetches the latest 13 values
 * of the 'total_real_power', 'watts_phase_a', 'watts_phase_b', and 'watts_phase_c' fields
 * from the "powertic.measurements" table.
 * 
 * It computes the average of the phase values, divides all values by 1000 to display in kW, 
 * and prints them to the terminal with a labeled time interval.
 * 
 * Output Order:
 * - It prints the total_real_power, watts_phase_a, watts_phase_b, watts_phase_c, and the average
 *   for each 5-minute interval.
 * - It includes the '-60 min' interval.
 */

import client from './dbCredentials.js';

// Helper function to calculate the average of phase values
function calculateAverage(phaseA, phaseB, phaseC) {
  return (phaseA + phaseB + phaseC) / 3;
}

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest 13 values for total real power and phase wattages from the measurements table
    const query = `
      SELECT total_real_power, watts_phase_a, watts_phase_b, watts_phase_c
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 13;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      console.log("Real Power / Potencia Real:");

      // Loop through the results, calculate the average, and print each value with a time label
      result.rows.forEach((row, index) => {
        const totalRealPower = (row.total_real_power / 1000).toFixed(3);  // Convert to kW
        const wattsPhaseA = (row.watts_phase_a / 1000).toFixed(3);  // Convert to kW
        const wattsPhaseB = (row.watts_phase_b / 1000).toFixed(3);  // Convert to kW
        const wattsPhaseC = (row.watts_phase_c / 1000).toFixed(3);  // Convert to kW
        const average = (calculateAverage(row.watts_phase_a, row.watts_phase_b, row.watts_phase_c) / 1000).toFixed(3);  // Calculate and convert to kW

        // Print the values for the current time interval
        console.log(`-${index * 5} min total_real_power: ${totalRealPower} kW`);
        console.log(`-${index * 5} min watts_phase_a: ${wattsPhaseA} kW`);
        console.log(`-${index * 5} min watts_phase_b: ${wattsPhaseB} kW`);
        console.log(`-${index * 5} min watts_phase_c: ${wattsPhaseC} kW`);
        console.log(`-${index * 5} min average: ${average} kW`);
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