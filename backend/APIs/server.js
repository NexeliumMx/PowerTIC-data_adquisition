import express from 'express';
import cors from 'cors';
import fetchTimestamp from './fetchTimestamp.js'; // Import the timestamp fetcher

const app = express();
const port = 3001;

app.use(cors()); // Enable CORS for all origins

// API route to serve the latest timestamp
app.get('/api/timestamp', async (req, res) => {
  try {
    console.log('Received request for timestamp');
    const timestamp = await fetchTimestamp();
    console.log('Sending response:', timestamp);
    res.json({ timestamp });  // Return the timestamp as JSON
  } catch (error) {
    console.error('Error occurred while fetching timestamp:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});