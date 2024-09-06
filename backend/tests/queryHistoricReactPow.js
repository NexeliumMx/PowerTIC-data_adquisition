import client from './dbCredentials.js';

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    // Query to get the latest 12 reactive power var values from the powertic.measurements table
    const query = `
      SELECT reactive_power_var
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 12;
    `;

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      // Loop through the results and print each reactive_power_var value
      result.rows.forEach(row => {
        console.log(row.reactive_power_var);  // Print each reactive_power_var value
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