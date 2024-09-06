import client from './postgresCredentials.js';

// Function to fetch the power consumption values
const fetchPowerConsumption = async () => {
  try {
    // Query to get the latest power consumption values from the "powertic.measurements" table
    const query = `
      SELECT total_real_energy_imported, total_var_hours_imported_q1, total_var_hours_imported_q2
      FROM "powertic"."measurements"
      ORDER BY idmeasurements DESC LIMIT 1;
    `;

    const result = await client.query(query);

    if (result.rows.length > 0) {
      const row = result.rows[0];
      const total_real_energy_imported = (row.total_real_energy_imported / 1000).toFixed(3); // Convert to kWh
      const total_var_hours_imported_q1 = (row.total_var_hours_imported_q1 / 1000).toFixed(3); // Convert to kvarh
      const total_var_hours_imported_q2 = (row.total_var_hours_imported_q2 / 1000).toFixed(3); // Convert to kvarh

      // Return the values
      return {
        total_real_energy_imported,
        total_var_hours_imported_q1,
        total_var_hours_imported_q2
      };
    } else {
      return {
        total_real_energy_imported: 'No data',
        total_var_hours_imported_q1: 'No data',
        total_var_hours_imported_q2: 'No data'
      };
    }
  } catch (err) {
    console.error('Error fetching power consumption:', err.stack);
    throw new Error('Failed to fetch power consumption');
  }
};

export default fetchPowerConsumption;