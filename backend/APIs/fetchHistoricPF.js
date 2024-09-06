/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * Description:
 * This script connects to the PostgreSQL database and fetches the latest 14 values of the 'power_factor' 
 * field from the "powertic.measurements" table. It normalizes the power factor values from -1000 to +1000 
 * to a range of -1 to 1 and prepares them for use in a JSON object.
 * 
 * The output JSON object consists of an array of objects with 'name' and 'promedio' fields, where 'name' 
 * corresponds to a time label (e.g., '0 min', '-5 min') and 'promedio' is the normalized power factor value.
 * 
 * If no records are found, it returns a message indicating no data is available.
 * 
 * Output:
 * - A JSON array with the time label and the normalized power factor values in descending order.
 * 
 * Test:
 * curl http://localhost:3001/api/historicpf
 */

import client from './postgresCredentials.js';

// Helper function to normalize the power factor value from -1000 to +1000 to -1 to 1
function normalizeHistoricPF(HistoricPF) {
  return HistoricPF / 1000;
}

// Function to fetch historical power factor data
const fetchHistoricPF = async () => {
  try {
    // Query to get the latest 14 power factor values
    const query = `
      SELECT power_factor
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 14;
    `;

    const result = await client.query(query);

    if (result.rows.length > 0) {
      // Build the JSON array of objects for the response
      const data = result.rows.map((row, index) => ({
        name: `-${index * 5} min`,
        promedio: normalizeHistoricPF(row.power_factor).toFixed(3)  // Normalize and round to 3 decimal places
      }));

      // Add the fixed value for the -60 min entry
      data.push({ name: '-60 min', promedio: '1.000' });

      return data;
    } else {
      return [{ name: 'No data', promedio: 0 }];
    }
  } catch (err) {
    console.error('Error fetching historic power factor:', err.stack);
    throw new Error('Failed to fetch historic power factor');
  }
};

export default fetchHistoricPF;