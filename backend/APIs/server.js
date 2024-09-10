import express from 'express';
import { fetchTimestamp } from './scripts/fetchTimestamp.js';
import fetchMaxDemand from './scripts/fetchMaxDemand.js';
import fetchPowerConsumption from './scripts/fetchPowerConsumption.js';
import fetchLastPF from './scripts/fetchLastPF.js';
import fetchCurrent from './scripts/fetchCurrent.js';
import fetchHistoricPF from './scripts/fetchHistoricPF.js';
import fetchHistoricRealPower from './scripts/fetchHistoricRealPower.js';
import fetchHistoricReactivePower from './scripts/fetchHistoricReactivePower.js';
import fetchHistoricPowerConsumption from './scripts/fetchHistoricPowerConsumption.js'; // Import the new function
import cors from 'cors';
import client from './scripts/postgresCredentials.js';
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
    const maxDemand = await fetchMaxDemand();
    res.status(200).send(maxDemand);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch maximum demand' });
  }
});

// Define the /api/powerconsumption endpoint
app.get('/api/powerconsumption', async (req, res) => {
  try {
    const powerConsumption = await fetchPowerConsumption();
    res.status(200).send(powerConsumption);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch power consumption' });
  }
});

// Define the /api/lastpf endpoint
app.get('/api/lastpf', async (req, res) => {
  try {
    const powerFactor = await fetchLastPF();
    res.status(200).send(powerFactor);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch power factor' });
  }
});

// Define the /api/current endpoint
app.get('/api/current', async (req, res) => {
  try {
    const currentValues = await fetchCurrent();
    res.status(200).send(currentValues);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch current values' });
  }
});

// Define the /api/historicpf endpoint
app.get('/api/historicpf', async (req, res) => {
  try {
    const historicPF = await fetchHistoricPF();
    res.status(200).send(historicPF);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch historic power factor' });
  }
});

// Define the /api/historicrealpower endpoint
app.get('/api/historicrealpower', async (req, res) => {
  try {
    const historicRealPower = await fetchHistoricRealPower();
    res.status(200).send(historicRealPower);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch historic real power' });
  }
});

// Define the /api/historicreactivepower endpoint
app.get('/api/historicreactivepower', async (req, res) => {
  try {
    const historicReactivePower = await fetchHistoricReactivePower();
    res.status(200).send(historicReactivePower);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch historic reactive power' });
  }
});

// Define the /api/historicpowerconsumption endpoint
app.get('/api/historicpowerconsumption', async (req, res) => {
  try {
    const historicPowerConsumption = await fetchHistoricPowerConsumption();
    res.status(200).send(historicPowerConsumption);
  } catch (error) {
    res.status(500).send({ error: 'Failed to fetch historic power consumption' });
  }
});

// Function to listen for notifications
async function listenForNotifications() {
  try {
    await client.query('LISTEN new_measurement');
    console.log('Listening for new measurements...');

    client.on('notification', async (msg) => {
      if (msg.channel === 'new_measurement') {
        console.log('New measurement received:', msg.payload);
        const latestTimestamp = await fetchTimestamp();
        io.emit('newTimestamp', latestTimestamp);
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