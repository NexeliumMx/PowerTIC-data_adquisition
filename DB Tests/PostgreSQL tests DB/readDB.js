// Import the pg module using the default import syntax
import pkg from 'pg';
const { Client } = pkg;

// Create a new PostgreSQL client
const client = new Client({
  user: "postgres",
  host: "localhost",
  database: "Acurev1313_ModbusAddress",
  password: "Tono2002",
  port: 5432,
});

// Connect to the database
client.connect()
  .then(() => {
    console.log('Connected to the database.');
    return client.query('SELECT parameter_description FROM measurement_address');
  })
  .then(res => {
    // Print all the parameter_description values
    res.rows.forEach(row => {
      console.log(row.parameter_description);
    });
  })
  .catch(err => {
    console.error('Error executing query', err.stack);
  })
  .finally(() => {
    // Close the connection
    client.end();
  });