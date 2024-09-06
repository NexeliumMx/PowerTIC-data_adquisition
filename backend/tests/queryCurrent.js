/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and fetches the latest values
 * for amps_total, amps_phase_a, amps_phase_b, and amps_phase_c from the
 * "powertic.measurements" table.
 * 
 * It also calculates the percentage of current imbalance between the phases, 
 * printing the results in a formatted way to the terminal.
 * 
 * Output:
 * - It prints amps_total.
 * - It prints amps_phase_a, amps_phase_b, and amps_phase_c.
 * - Then, it prints the percentage of current imbalance (range 0 to 100).
 */

import client from './dbCredentials.js';

// Function to calculate the percentage of imbalance between three phases
function calculateImbalance(phaseA, phaseB, phaseC) {
  const avg = (phaseA + phaseB + phaseC) / 3;
  if (avg === 0) {
    return 0;  // Avoid division by zero
  }

  const deviationA = Math.abs(phaseA - avg);
  const deviationB = Math.abs(phaseB - avg);
  const deviationC = Math.abs(phaseC - avg);
  const maxDeviation = Math.max(deviationA, deviationB, deviationC);
  const imbalancePercentage = (maxDeviation / avg) * 100;
  return imbalancePercentage;
}

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest amps values from the powertic.measurements table
    const query = `
      SELECT amps_total, amps_phase_a, amps_phase_b, amps_phase_c
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 1;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      const row = result.rows[0];
      const ampsTotal = row.amps_total || 0;  // Handle null or undefined values
      const ampsPhaseA = row.amps_phase_a || 0;
      const ampsPhaseB = row.amps_phase_b || 0;
      const ampsPhaseC = row.amps_phase_c || 0;

      // Print the amps values with labels and a new header "Current / Corriente"
      console.log("Current / Corriente:");
      console.log(`Total current: ${ampsTotal}`);
      console.log(`Phase A current: ${ampsPhaseA}`);
      console.log(`Phase B current: ${ampsPhaseB}`);
      console.log(`Phase C current: ${ampsPhaseC}`);

      // Calculate and print the imbalance percentage
      const imbalance = calculateImbalance(ampsPhaseA, ampsPhaseB, ampsPhaseC);
      console.log(`Current imbalance: ${imbalance.toFixed(2)}%`);
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