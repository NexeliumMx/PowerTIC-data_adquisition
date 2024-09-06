import pkg from 'pg';
const { Client } = pkg;

// PostgreSQL database connection configuration with SSL enabled
const client = new Client({
  user: 'superadmin', // Your PostgreSQL username
  host: 'powerticpgtest1.postgres.database.azure.com',
  database: 'powerticapp', // The correct database name
  password: 'vafja6-hexpem-javdyN', // Your PostgreSQL password
  port: 5432, // PostgreSQL default port
  ssl: {
    rejectUnauthorized: false // Azure uses trusted SSL certificates
  }
});

// Helper function to format the timestamp
function formatTimestamp(timestamp) {
  const months = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
  ];

  const date = new Date(timestamp);
  const day = String(date.getDate()).padStart(2, '0');
  const month = months[date.getMonth()];
  const year = date.getFullYear();
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');

  return `${day} de ${month} de ${year} ${hours}:${minutes}`;
}

// Connect to the PostgreSQL database
client.connect()
  .then(() => {
    console.log('Connected to PostgreSQL database');

    // Query to get the latest timestamp from the powertic.measurements table
    const query = 'SELECT timestamp FROM "powertic"."measurements" ORDER BY idmeasurements DESC LIMIT 1;';

    return client.query(query);
  })
  .then(result => {
    if (result.rows.length > 0) {
      const originalTimestamp = result.rows[0].timestamp;
      console.log(`Latest Timestamp: ${originalTimestamp}`);

      // Convert and format the timestamp
      const formattedTimestamp = formatTimestamp(originalTimestamp);
      console.log(`Converted Timestamp: '${formattedTimestamp}'`);
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