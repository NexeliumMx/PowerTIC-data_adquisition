/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * Description:
 * This script connects to the PostgreSQL database and fetches the latest timestamp from the 
 * "powertic.measurements" table, ordered by the timestamp field to ensure the most recent value is returned.
 * 
 * Output:
 * - The raw timestamp from the database.
 * 
 * Test:
 * curl http://localhost:3001/api/timestamp
 */

import client from './postgresCredentials.js';

// Function to fetch the latest timestamp from the database
async function fetchTimestamp() {
  try {
    // Updated query to order by timestamp instead of idmeasurements
    const query = 'SELECT timestamp FROM "powertic"."measurements" ORDER BY timestamp DESC LIMIT 1;';
    const result = await client.query(query);

    if (result.rows.length > 0) {
      console.log('Latest timestamp fetched:', result.rows[0].timestamp);  // Log the fetched timestamp
      return result.rows[0].timestamp;  // Return the raw timestamp
    } else {
      return 'No records found in the table.';
    }
  } catch (error) {
    console.error('Error fetching timestamp:', error.stack);
    throw error;
  }
}

export { fetchTimestamp };