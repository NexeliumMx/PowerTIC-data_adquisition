/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and fetches the latest values
 * for total_real_energy_imported and total_va_hours_imported from the
 * "powertic.measurements" table.
 * 
 * The results are printed directly to the terminal without any surrounding text or labels.
 * 
 *  Output Order:
 * - First, it prints total_real_energy_imported.
 * - Then, it prints total_va_hours_imported.
 */

import client from './dbCredentials.js';

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest power consumption values from the powertic.measurements table
    const query = `
      SELECT total_real_energy_imported, total_va_hours_imported
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 1;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      const row = result.rows[0];
      const totalRealEnergyImported = row.total_real_energy_imported;
      const totalVAHoursImported = row.total_va_hours_imported;

      // Print the values without any strings
      console.log(totalRealEnergyImported);
      console.log(totalVAHoursImported);
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