import client from './postgresCredentials.js';

// Helper function to normalize the power factor value from -1000 to +1000 to -1 to 1
function normalizePowerFactor(powerFactor) {
  return powerFactor / 1000;
}

// Function to fetch the latest power factor
const fetchLastPF = async () => {
  try {
    // Query to get the latest power_factor from the powertic.measurements table
    const query = 'SELECT power_factor FROM "powertic"."measurements" ORDER BY idmeasurements DESC LIMIT 1;';

    const result = await client.query(query);

    if (result.rows.length > 0) {
      const powerFactor = result.rows[0].power_factor;

      // Normalize the power factor
      const normalizedPowerFactor = normalizePowerFactor(powerFactor);

      // Return the normalized power factor
      return {
        power_factor: normalizedPowerFactor.toFixed(3) // Return with 3 decimal places
      };
    } else {
      return { power_factor: 'No data' };
    }
  } catch (err) {
    console.error('Error fetching power factor:', err.stack);
    throw new Error('Failed to fetch power factor');
  }
};

export default fetchLastPF;