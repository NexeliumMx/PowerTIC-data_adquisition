/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * Description:
 * This script connects to the PostgreSQL database and fetches the latest values
 * for amps_total, amps_phase_a, amps_phase_b, and amps_phase_c from the
 * "powertic.measurements" table.
 * 
 * It also calculates the percentage of current imbalance between the phases,
 * and returns these values along with the imbalance percentage.
 * 
 * Output:
 * - amps_total: Total current across all phases.
 * - amps_phase_a: Current in Phase A.
 * - amps_phase_b: Current in Phase B.
 * - amps_phase_c: Current in Phase C.
 * - current_imbalance: The calculated percentage of current imbalance (range 0 to 100).
 * 
 * The results are returned as a JSON object for use in the API response.
 * 
 * Test:
 * curl http://localhost:3001/api/current
 */

import client from './postgresCredentials.js';

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

// Function to fetch the latest current values and calculate imbalance
const fetchCurrent = async () => {
  try {
    // Query to get the latest amps values from the powertic.measurements table
    const query = `
      SELECT amps_total, amps_phase_a, amps_phase_b, amps_phase_c
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 1;
    `;

    const result = await client.query(query);

    if (result.rows.length > 0) {
      const row = result.rows[0];
      const ampsTotal = row.amps_total || 0;
      const ampsPhaseA = row.amps_phase_a || 0;
      const ampsPhaseB = row.amps_phase_b || 0;
      const ampsPhaseC = row.amps_phase_c || 0;

      // Calculate the current imbalance
      const imbalance = calculateImbalance(ampsPhaseA, ampsPhaseB, ampsPhaseC);

      // Return the results as an object
      return {
        amps_total: ampsTotal,
        amps_phase_a: ampsPhaseA,
        amps_phase_b: ampsPhaseB,
        amps_phase_c: ampsPhaseC,
        current_imbalance: imbalance.toFixed(2)  // Round to 2 decimal places
      };
    } else {
      return {
        amps_total: 'No data',
        amps_phase_a: 'No data',
        amps_phase_b: 'No data',
        amps_phase_c: 'No data',
        current_imbalance: 'No data'
      };
    }
  } catch (err) {
    console.error('Error fetching current values:', err.stack);
    throw new Error('Failed to fetch current values');
  }
};

export default fetchCurrent;