import express from 'express';
import cors from 'cors';
import { createServer } from 'http'; // Import http to integrate with Socket.IO
import { Server } from 'socket.io'; // Import Socket.IO
import broadcastTimestamp from './broadcastTimestamp.js'; // Import the broadcastTimestamp function
import client from '../tests/dbCredentials.js'; // Import the PostgreSQL client

const app = express();
const port = 3001;

app.use(cors());

// Create an HTTP server and integrate it with Socket.IO
const httpServer = createServer(app);
const io = new Server(httpServer, {
  cors: {
    origin: "*", // Allow all origins for development purposes
    methods: ["GET", "POST"],
  },
});

// Store the ID of the last measurement to compare with the database entries
let lastMeasurementId = null;

// Function to poll the database every minute and check for new entries
async function pollDatabase() {
  try {
    const result = await client.query('SELECT idmeasurements FROM "powertic"."measurements" ORDER BY idmeasurements DESC LIMIT 1;');
    const latestMeasurementId = result.rows[0]?.idmeasurements;

    if (latestMeasurementId !== lastMeasurementId) {
      console.log(`New measurement detected with id: ${latestMeasurementId}`);
      lastMeasurementId = latestMeasurementId;
      
      // Broadcast the latest timestamp to all clients
      broadcastTimestamp(io);
    } else {
      console.log('No new entries found.');
    }
  } catch (error) {
    console.error('Error polling database:', error);
  }
}

// Poll the database every minute (60 seconds)
setInterval(pollDatabase, 60000); // 60 seconds

// Emit the timestamp periodically (every 10 seconds)
setInterval(() => {
  broadcastTimestamp(io); // You can also pass specific time zones if needed
}, 10000); // 10 seconds

// Listen for incoming client connections
io.on('connection', (socket) => {
  console.log('New client connected');

  // Listen for the client's requested timezone
  socket.on('requestTimestamp', (timezone) => {
    // Use the provided timezone or default to 'America/Mexico_City'
    console.log('Timezone requested:', timezone);
    broadcastTimestamp(io, timezone || 'America/Mexico_City');
  });

  // Send the latest timestamp when the client connects
  broadcastTimestamp(io);

  socket.on('disconnect', () => {
    console.log('Client disconnected');
  });
});

// Start the HTTP server instead of the express app
httpServer.listen(port, () => {
  console.log(`Server running on port ${port}`);
});