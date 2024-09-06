/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * Description:
 * This script connects to the PostgreSQL database and retrieves the latest 13 values of 
 * 'total_real_energy_imported' and 'total_var_hours_imported_q1' from the "powertic.measurements" table. 
 * It calculates the consumption difference in kWh and kVArh for each 5-minute interval and 
 * returns this data in a JSON format suitable for chart visualization.
 * 
 * Output:
 * - The JSON object contains the consumption data for 'total_real_energy_imported' (kWh) and 
 *   'total_var_hours_imported_q1' (kVArh) over 13 intervals of 5 minutes each.
 * 
 * Example Format:
 * const data = [
 *   { name: '0 min', kw: 10, kvar: 8 },
 *   { name: '5 min', kw: 20, kvar: 18 },
 *   ...
 * ];
 * 
 *  Test:
 * curl http://localhost:3001/api/historicpowerconsumption
 */

import client from './postgresCredentials.js';

// Function to fetch historic power consumption
const fetchHistoricPowerConsumption = async () => {
  try {
    // Query to get the latest 13 readings for total_real_energy_imported and total_var_hours_imported_q1
    const query = `
      SELECT total_real_energy_imported, total_var_hours_imported_q1
      FROM "powertic"."measurements"
      ORDER BY timestamp DESC
      LIMIT 14;
    `;

    const result = await client.query(query);

    if (result.rows.length === 14) {
      const data = [];
      let previousKWhReading = result.rows[0].total_real_energy_imported;
      let previousKVarhReading = result.rows[0].total_var_hours_imported_q1;

      // Loop through the rows to compute consumption differences
      for (let i = 1; i < result.rows.length; i++) {
        const currentKWhReading = result.rows[i].total_real_energy_imported;
        const currentKVarhReading = result.rows[i].total_var_hours_imported_q1;

        const kw = ((previousKWhReading - currentKWhReading) / 1000).toFixed(3); // Convert Wh to kWh
        const kvar = ((previousKVarhReading - currentKVarhReading) / 1000).toFixed(3); // Convert VAh to kVArh

        data.push({
          name: `${i === 1 ? '0' : `-${(i - 1) * 5}`} min`,
          kw: parseFloat(kw),
          kvar: parseFloat(kvar)
        });

        previousKWhReading = currentKWhReading;
        previousKVarhReading = currentKVarhReading;
      }

      return data;
    } else {
      return { message: 'Not enough data points found in the table.' };
    }
  } catch (err) {
    console.error('Error fetching historic power consumption:', err.stack);
    throw new Error('Failed to fetch historic power consumption');
  }
};

export default fetchHistoricPowerConsumption;