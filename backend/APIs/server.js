import express from 'express';
import { fetchTimestamp } from './fetchTimestamp.js';
import fetchMaxDemand from './fetchMaxDemand.js'; // Import max demand function
import fetchPowerConsumption from './fetchPowerConsumption.js'; // Import power consumption function
import fetchLastPF from './fetchLastPF.js'; // Import last power factor function
import cors from 'cors';
import client from './postgresCredentials.js';
import { Server } from 'socket.io';
import http from 'http';

const app = express();
const PORT = 3001;

const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "*",
    methods: ["GET", "POST"]
  }
});

app.use(cors());

// Connect to the PostgreSQL database once when the server starts
client.connect()
  .then(() => {
    console.log('Connected to PostgreSQL');
  })
  .catch(err => {
    console.error('Failed to connect to PostgreSQL:', err.stack);
  });

// Define the /api/timestamp endpoint
app.get('/api/timestamp', async (req, res) => {
  try {
    const timestamp = await fetchTimestamp();
    res.status(200).send({ timestamp });
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch timestamp' });
  }
});

// Define the /api/maxdemand endpoint
app.get('/api/maxdemand', async (req, res) => {
  try {
    const maxDemand = await fetchMaxDemand(); // Fetch max demand data
    res.status(200).send(maxDemand); // Send the data as a JSON response
  } catch (error) {
    console.error('Error occurred while fetching max demand:', error);
    res.status(500).send({ error: 'Failed to fetch maximum demand' });
  }
});

// Define the /api/powerconsumption endpoint
app.get('/api/powerconsumption', async (req, res) => {
  try {
    const powerConsumption = await fetchPowerConsumption(); // Fetch power consumption data
    res.status(200).send(powerConsumption); // Send the data as a JSON response
  } catch (error) {
    console.error('Error occurred while fetching power consumption:', error);
    res.status(500).send({ error: 'Failed to fetch power consumption' });
  }
});

// Define the /api/lastpf endpoint
app.get('/api/lastpf', async (req, res) => {
  try {
    const powerFactor = await fetchLastPF(); // Fetch last power factor data
    res.status(200).send(powerFactor); // Send the data as a JSON response
  } catch (error) {
    console.error('Error occurred while fetching power factor:', error);
    res.status(500).send({ error: 'Failed to fetch power factor' });
  }
});

// Function to listen for notifications
async function listenForNotifications() {
  try {
    // Listen for 'new_measurement' notifications
    await client.query('LISTEN new_measurement');

    console.log('Listening for new measurements...');

    // When a notification is received
    client.on('notification', async (msg) => {
      if (msg.channel === 'new_measurement') {
        console.log('New measurement received:', msg.payload);

        // Fetch the latest timestamp
        const latestTimestamp = await fetchTimestamp();

        // Send the new timestamp to all connected clients
        io.emit('newTimestamp', latestTimestamp);

        // Log that it's still listening after receiving the new measurement
        console.log('Listening for new measurements...');
      }
    });

  } catch (error) {
    console.error('Error listening for notifications:', error);
  }
}

// Start listening for PostgreSQL notifications
listenForNotifications();

// Start the server with WebSockets
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});