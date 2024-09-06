import express from 'express';
import { fetchTimestamp } from './fetchTimestamp.js';
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

// Define the /api/timestamp endpoint
app.get('/api/timestamp', async (req, res) => {
  try {
    const timestamp = await fetchTimestamp();
    res.status(200).send({ timestamp });
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch timestamp' });
  }
});

// Function to listen for notifications
async function listenForNotifications() {
  try {
    await client.connect();

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