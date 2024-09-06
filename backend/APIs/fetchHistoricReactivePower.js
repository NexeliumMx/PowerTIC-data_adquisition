/**
 * Author: Arturo Vargas Cuevas & Rogelio Akin Leon Garcia
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * Description:
 * This script connects to the PostgreSQL database and fetches the latest 13 values for 
 * reactive_power_var, var_phase_a, var_phase_b, and var_phase_c from the "powertic.measurements" table. 
 * It calculates the average of the three phases and returns the data in a JSON format with labels indicating 
 * the time intervals (e.g., '0 min', '-5 min').
 * 
 * The returned JSON structure can be used for visualization purposes.
 * 
 * Output:
 * - A JSON array with time labels, average reactive power, and the reactive power for each phase.
 * 
 * Test:
 * curl http://localhost:3001/api/historicreactivepower
 */

import client from './postgresCredentials.js';

// Helper function to calculate the average of phase values
function calculateAverage(phaseA, phaseB, phaseC) {
  return ((phaseA + phaseB + phaseC) / 3).toFixed(3);
}

// Function to fetch the historic reactive power data
const fetchHistoricReactivePower = async () => {
  try {
    // Query to get the latest 13 reactive power values from the powertic.measurements table
    const query = `
      SELECT reactive_power_var, var_phase_a, var_phase_b, var_phase_c
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 13;
    `;

    const result = await client.query(query);

    if (result.rows.length > 0) {
      const data = result.rows.map((row, index) => {
        const average = calculateAverage(row.var_phase_a, row.var_phase_b, row.var_phase_c);
        return {
          name: `${index === 0 ? '0' : `-${index * 5}`} min`, // Label time intervals
          promedio: parseFloat(average), // Average of the three phases
          faseA: parseFloat((row.var_phase_a / 1000).toFixed(3)), // Convert to kVAr
          faseB: parseFloat((row.var_phase_b / 1000).toFixed(3)), // Convert to kVAr
          faseC: parseFloat((row.var_phase_c / 1000).toFixed(3))  // Convert to kVAr
        };
      });

      // Return the formatted data array
      return data;
    } else {
      return { message: 'No records found in the table.' };
    }
  } catch (err) {
    console.error('Error fetching historic reactive power:', err.stack);
    throw new Error('Failed to fetch historic reactive power');
  }
};

export default fetchHistoricReactivePower;