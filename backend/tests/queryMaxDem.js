import client from './dbCredentials.js';

// Helper function to get the maximum value from an array of values
function getMaxValue(values) {
  return Math.max(...values);
}

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest 12 total real energy imported values from the powertic.measurements table
    const query = `
      SELECT total_real_energy_imported
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 12;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      // Extract all total_real_energy_imported values into an array
      const values = result.rows.map(row => row.total_real_energy_imported);

      // Find the maximum value from the array
      const maxValue = getMaxValue(values);
      console.log('Max value:', maxValue);
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
