/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * Description:
 * This script connects to the PostgreSQL database and fetches the maximum values for 
 * total_real_power and reactive_power_var from the "powertic.measurements" table.
 * 
 * The values are converted to kilowatts (kW) and kilovolt-amperes reactive (kVAR) 
 * by dividing them by 1000 and are returned as part of a JSON object.
 * 
 * If no records are found, it returns a message indicating no data is available.
 * 
 * Output:
 * - max_total_real_power: The maximum real power value in kW, or 'No data' if no records are found.
 * - max_reactive_power_var: The maximum reactive power value in kVAR, or 'No data' if no records are found.
 * 
 * Test:
 * curl http://localhost:3001/api/maxdemand
 */

import client from './postgresCredentials.js';

// Function to fetch the maximum demand values
const fetchMaxDemand = async () => {
  try {
    // Query to get the maximum values for total_real_power and reactive_power_var
    const query = `
      SELECT MAX(total_real_power) AS max_total_real_power, 
             MAX(reactive_power_var) AS max_reactive_power_var
      FROM "powertic"."measurements";
    `;

    const result = await client.query(query);

    if (result.rows.length > 0) {
      const row = result.rows[0];
      const max_total_real_power = (row.max_total_real_power / 1000).toFixed(3); // Convert to kW
      const max_reactive_power_var = (row.max_reactive_power_var / 1000).toFixed(3); // Convert to kVAR

      // Return the max demand values with the new variable names
      return {
        max_total_real_power,
        max_reactive_power_var
      };
    } else {
      return {
        max_total_real_power: 'No data',
        max_reactive_power_var: 'No data'
      };
    }
  } catch (err) {
    console.error('Error fetching max demand:', err.stack);
    throw new Error('Failed to fetch max demand'); // Throw the error so that the API can handle it
  }
};

export default fetchMaxDemand;