/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * Description:
 * This script connects to the PostgreSQL database and fetches the latest 13 values for total_real_power,
 * watts_phase_a, watts_phase_b, and watts_phase_c from the "powertic.measurements" table. It also calculates
 * the average of the three phases for each time interval and returns the data in a JSON format that includes
 * 'name' (time interval) and real power values for each phase and the average.
 * 
 * The returned JSON structure can be used for visualization purposes.
 * 
 * Output:
 * - A JSON array with the time label, average real power, and the real power for each phase.
 * 
 * Test:
 * curl http://localhost:3001/api/historicrealpower
 */

import client from './postgresCredentials.js';

// Helper function to calculate the average of phase values
function calculateAverage(phaseA, phaseB, phaseC) {
  return ((phaseA + phaseB + phaseC) / 3).toFixed(3);
}

// Function to fetch the historic real power data
const fetchHistoricRealPower = async () => {
  try {
    // Query to get the latest 13 real power values from the powertic.measurements table
    const query = `
      SELECT total_real_power, watts_phase_a, watts_phase_b, watts_phase_c
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 13;
    `;

    const result = await client.query(query);

    if (result.rows.length > 0) {
      const data = result.rows.map((row, index) => {
        const average = calculateAverage(row.watts_phase_a, row.watts_phase_b, row.watts_phase_c);
        return {
          name: `${index === 0 ? '0' : `-${index * 5}`} min`, // Label time intervals
          promedio: parseFloat(average), // Average of the three phases
          faseA: parseFloat((row.watts_phase_a / 1000).toFixed(3)), // Convert to kW
          faseB: parseFloat((row.watts_phase_b / 1000).toFixed(3)), // Convert to kW
          faseC: parseFloat((row.watts_phase_c / 1000).toFixed(3))  // Convert to kW
        };
      });

      // Return the formatted data array
      return data;
    } else {
      return { message: 'No records found in the table.' };
    }
  } catch (err) {
    console.error('Error fetching historic real power:', err.stack);
    throw new Error('Failed to fetch historic real power');
  }
};

export default fetchHistoricRealPower;