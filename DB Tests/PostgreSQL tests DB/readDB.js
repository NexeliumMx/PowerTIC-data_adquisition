// Import the pg module using the default import syntax
import pkg from 'pg';
const { Client } = pkg;

// Create a new PostgreSQL client
const client = new Client({
  user: "postgres",
  host: "localhost",
  database: "Acurev1313_ModbusAddress",
  password: "2705", //luis: Tono2002 //Arturo: 2705
  port: 5432,
});

// Function to print parameter descriptions from a specified table
const printParameterDescriptions = (tableName) => {
  return client.query(`SELECT parameter_description FROM ${tableName}`)
    .then(res => {
      console.log(`\nParameter Descriptions from ${tableName}:`);
      res.rows.forEach(row => {
        console.log(row.parameter_description);
      });
    });
};

// Connect to the database and perform the queries
client.connect()
  .then(() => {
    console.log('Connected to the database.');
    // Print parameter descriptions from both tables
    return printParameterDescriptions('readings_addresses')
      .then(() => printParameterDescriptions('device_info_addresses'));
  })
  .catch(err => {
    console.error('Error executing query', err.stack);
  })
  .finally(() => {
    // Close the connection
    client.end();
  });
