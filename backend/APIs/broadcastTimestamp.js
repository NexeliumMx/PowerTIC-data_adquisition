import fetchTimestamp from './fetchTimestamp.js'; // Import the fetchTimestamp function

// Function to broadcast the latest timestamp to all connected clients
async function broadcastTimestamp(io, timezone = 'America/Mexico_City') {
  try {
    // Fetch the latest timestamp using the separated function
    const formattedTimestamp = await fetchTimestamp(timezone);
    
    // Emit the formatted timestamp to all connected clients
    io.emit('timestamp', formattedTimestamp);
  } catch (error) {
    console.error('Error broadcasting timestamp:', error);
  }
}

export default broadcastTimestamp; // Export the broadcastTimestamp function