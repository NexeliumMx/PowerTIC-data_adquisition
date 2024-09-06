import client from './postgresCredentials.js'; // Import the PostgreSQL client

// Helper function to format the timestamp and adjust it to the local time zone
function formatTimestamp(timestamp) {
  const months = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
  ];

  // Convert the timestamp from UTC to local time zone
  const date = new Date(timestamp);

  const day = String(date.getDate()).padStart(2, '0');
  const month = months[date.getMonth()];
  const year = date.getFullYear();
  const hours = String(date.getHours()).padStart(2, '0'); 
  const minutes = String(date.getMinutes()).padStart(2, '0');

  return `${day} de ${month} de ${year} ${hours}:${minutes}`;
}

async function fetchTimestamp() {
  try {
    // Add log to see if the function is called
    console.log('Fetching timestamp from database...');
    
    // Connect to the PostgreSQL database
    await client.connect();

    // Query to get the latest timestamp from the powertic.measurements table
    const query = 'SELECT timestamp FROM "powertic"."measurements" ORDER BY idmeasurements DESC LIMIT 1;';
    
    const result = await client.query(query);

    if (result.rows.length > 0) {
      const originalTimestamp = result.rows[0].timestamp;
      console.log('Fetched timestamp:', originalTimestamp);
      
      const formattedTimestamp = formatTimestamp(originalTimestamp); // Format the timestamp
      console.log('Formatted timestamp:', formattedTimestamp);
      
      return formattedTimestamp; // Return the formatted timestamp
    } else {
      console.log('No timestamp found');
      return 'No timestamp found'; // Handle case where no rows are found
    }
  } catch (err) {
    console.error('Error fetching timestamp:', err);
    throw new Error('Error fetching timestamp'); // Rethrow the error
  } finally {
    await client.end(); // Close the database connection
    console.log('Database connection closed');
  }
}

export default fetchTimestamp;