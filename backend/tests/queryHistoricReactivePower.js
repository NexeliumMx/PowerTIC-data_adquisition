/**
 * Author: Rogelio Akin Leon Garcia & Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and fetches the latest 14 values
 * of the 'reactive_power_var', 'var_phase_a', 'var_phase_b', and 'var_phase_c' fields
 * from the "powertic.measurements" table.
 * 
 * It computes the average of the phase values, divides all values by 1000 to display in kVAr,
 * and prints them to the terminal with a labeled time interval.
 * 
 * Output Order:
 * - It prints the reactive_power_var, var_phase_a, var_phase_b, var_phase_c, and the average
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
    // Query to get the latest 13 reactive power and phase VAR values from the measurements table
    const query = `
      SELECT reactive_power_var, var_phase_a, var_phase_b, var_phase_c
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 13;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      console.log("Reactive Power / Potencia Reactiva:");

      // Loop through the results, calculate the average, and print each value with a time label
      result.rows.forEach((row, index) => {
        const reactivePowerVar = (row.reactive_power_var / 1000).toFixed(3);  // Convert to kVAr
        const varPhaseA = (row.var_phase_a / 1000).toFixed(3);  // Convert to kVAr
        const varPhaseB = (row.var_phase_b / 1000).toFixed(3);  // Convert to kVAr
        const varPhaseC = (row.var_phase_c / 1000).toFixed(3);  // Convert to kVAr
        const average = (calculateAverage(row.var_phase_a, row.var_phase_b, row.var_phase_c) / 1000).toFixed(3);  // Calculate and convert to kVAr

        // Print the values for the current time interval
        console.log(`-${index * 5} min reactive_power_var: ${reactivePowerVar} kVAr`);
        console.log(`-${index * 5} min var_phase_a: ${varPhaseA} kVAr`);
        console.log(`-${index * 5} min var_phase_b: ${varPhaseB} kVAr`);
        console.log(`-${index * 5} min var_phase_c: ${varPhaseC} kVAr`);
        console.log(`-${index * 5} min average: ${average} kVAr`);
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