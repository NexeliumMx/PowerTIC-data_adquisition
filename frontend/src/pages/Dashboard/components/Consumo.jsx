import React, { useEffect, useState } from 'react';
import Tile from './Tile'; // Import the Tile component
import { Activity, BatteryCharging, Gauge, Clock } from 'lucide-react';
import './Consumo.scss'; // Import the styles for Consumo

import ConsumptionHistory from './charts/ConsumptionHistory.jsx'; 
import DemandProfile from './charts/DemandProfile.jsx';
import PowerFactor from './charts/PowerFactor.jsx';
import TextDisplay from './charts/TextDisplay.jsx';

import { io } from 'socket.io-client'; // Import Socket.IO client
import COLORS from '../../../styles/chartColors.js';
import data from './charts/pieChartData.js';

const Consumo = () => {
  const [timestamp, setTimestamp] = useState('');

  useEffect(() => {
    // Connect to the WebSocket server
    const socket = io('http://localhost:3001'); // Adjust URL as needed

    // Get the user's time zone from the browser
    const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    console.log('User Time Zone:', timeZone); // Log the time zone to check

    // Request the timestamp in the user's time zone
    socket.emit('requestTimestamp', timeZone);

    // Listen for 'timestamp' events from the server
    socket.on('timestamp', (newTimestamp) => {
      console.log('Received timestamp from server:', newTimestamp); // Log the received timestamp
      setTimestamp(newTimestamp); // Update the timestamp state
    });

    // Cleanup the WebSocket connection when the component unmounts
    return () => {
      socket.disconnect();
    };
  }, []); // Empty dependency array ensures this runs once when the component mounts

  return (
    <div className="content-wrapper">
      {/* Small Tiles Container */}
      <div className="small-tiles-container">
        <Tile 
          title="Demanda Máxima" 
          icon={Activity} 
          content1={<TextDisplay display="10 000 kW"/>}
          content2={<TextDisplay display="10 000 kVar"/>}
          width="21%"
        />
        <Tile 
          title="Consumo Acumulado" 
          icon={BatteryCharging} 
          content1={<TextDisplay display="70 000 kWh"/>} 
          content2={<TextDisplay display="70 000 kWh"/>}
          width="21%"
        />
        <Tile 
          title="Factor de Potencia" 
          icon={Gauge} 
          content1={<PowerFactor data={data} colors={COLORS}/>} 
          width="23%"
        />
        <Tile 
          title="Tiempo" 
          icon={Clock} 
          content1={<TextDisplay display={timestamp}/>} // Display the timestamp received from WebSocket
          width="23%"
        />
      </div>

      {/* Big Tiles Container */}
      <div className="big-tiles-container">
        <Tile 
          title="Perfil de Demanda" 
          icon={Activity} 
          content1={<DemandProfile />} 
          width="57%"
        />
        <Tile 
          title="Historial de Consumo" 
          icon={BatteryCharging} 
          content1={<ConsumptionHistory />}
          width="43%"
        />
      </div>
    </div>
  );
}

export default Consumo;