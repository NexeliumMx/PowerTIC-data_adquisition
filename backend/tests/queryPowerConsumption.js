/**
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-09-06, by Arturo Vargas Cuevas
 * 
 * This script connects to the PostgreSQL database and fetches the latest values
 * for total_real_energy_imported, total_var_hours_imported_q1, and total_var_hours_imported_q2
 * from the "powertic.measurements" table.
 * 
 * The results are divided by 1000 and printed in kWh and kvarh with descriptive labels.
 * 
 *  Output Order:
 * - First, it prints total_real_energy_imported in kWh.
 * - Then, it prints total_var_hours_imported_q1 and total_var_hours_imported_q2 in kvarh.
 */

import client from './dbCredentials.js';

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest power consumption values from the powertic.measurements table
    const query = `
      SELECT total_real_energy_imported, total_var_hours_imported_q1, total_var_hours_imported_q2
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 1;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      const row = result.rows[0];
      const totalRealEnergyImported = (row.total_real_energy_imported / 1000).toFixed(3); // Convert to kWh
      const totalVarHoursImportedQ1 = (row.total_var_hours_imported_q1 / 1000).toFixed(3); // Convert to kvarh
      const totalVarHoursImportedQ2 = (row.total_var_hours_imported_q2 / 1000).toFixed(3); // Convert to kvarh

      // Print the values with labels
      console.log("Accumulated Consumption / Consumo Acumulado:");
      console.log(`Total Real Energy Imported: ${totalRealEnergyImported} kWh`);
      console.log(`Total var hours imported q1: ${totalVarHoursImportedQ1} kvarh`);
      console.log(`Total var hours imported q2: ${totalVarHoursImportedQ2} kvarh`);
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