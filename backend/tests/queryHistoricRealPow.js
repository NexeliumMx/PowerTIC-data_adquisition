import client from './dbCredentials.js';

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest 12 total real power values from the powertic.measurements table
    const query = `
      SELECT total_real_power
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 12;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      // Loop through the results and print each total_real_power value
      result.rows.forEach(row => {
        console.log(row.total_real_power);  // Print each total_real_power value
      });
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
