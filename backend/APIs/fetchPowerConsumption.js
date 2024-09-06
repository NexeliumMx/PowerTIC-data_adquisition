/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * Description:
 * This script connects to the PostgreSQL database and fetches the latest power consumption values
 * from the "powertic.measurements" table, including total_real_energy_imported, 
 * total_var_hours_imported_q1, and total_var_hours_imported_q2.
 * 
 * The values are converted to kilowatt-hours (kWh) and kilovolt-ampere reactive hours (kVARh)
 * by dividing them by 1000 and are returned as part of a JSON object.
 * 
 * If no records are found, it returns a message indicating no data is available.
 * 
 * Output:
 * - total_real_energy_imported: The total real energy imported in kWh, or 'No data' if no records are found.
 * - total_var_hours_imported_q1: The total reactive energy imported in kvarh (Q1), or 'No data'.
 * - total_var_hours_imported_q2: The total reactive energy imported in kvarh (Q2), or 'No data'.
 * 
 * Test:
 * curl http://localhost:3001/api/powerconsumption
 */
import client from './postgresCredentials.js';

// Function to fetch the power consumption values
const fetchPowerConsumption = async () => {
  try {
    // Query to get the latest power consumption values from the "powertic.measurements" table
    const query = `
      SELECT total_real_energy_imported, total_var_hours_imported_q1, total_var_hours_imported_q2
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 1;
    `;

    const result = await client.query(query);

    if (result.rows.length > 0) {
      const row = result.rows[0];
      const total_real_energy_imported = (row.total_real_energy_imported / 1000).toFixed(3); // Convert to kWh
      const total_var_hours_imported_q1 = (row.total_var_hours_imported_q1 / 1000).toFixed(3); // Convert to kvarh
      const total_var_hours_imported_q2 = (row.total_var_hours_imported_q2 / 1000).toFixed(3); // Convert to kvarh

      // Return the values
      return {
        total_real_energy_imported,
        total_var_hours_imported_q1,
        total_var_hours_imported_q2
      };
    } else {
      return {
        total_real_energy_imported: 'No data',
        total_var_hours_imported_q1: 'No data',
        total_var_hours_imported_q2: 'No data'
      };
    }
  } catch (err) {
    console.error('Error fetching power consumption:', err.stack);
    throw new Error('Failed to fetch power consumption');
  }
};

export default fetchPowerConsumption;