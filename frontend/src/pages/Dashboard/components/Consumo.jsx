import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import Tile from './Tile';
import { Activity, BatteryCharging, Gauge, Clock } from 'lucide-react';
import './Consumo.scss'; 

import ConsumptionHistory from './charts/ConsumptionHistory.jsx'; 
import DemandProfile from './charts/DemandProfile.jsx';
import PowerFactor from './charts/PowerFactor.jsx';
import TextDisplay from './charts/TextDisplay.jsx';

import COLORS from '../../../styles/chartColors.js';
import data from './charts/pieChartData.js';

const socket = io('http://localhost:3001');

const Consumo = () => {
  const [timestamp, setTimestamp] = useState('');

  // Fetch the timestamp initially when the component mounts
  useEffect(() => {
    const fetchInitialTimestamp = async () => {
      const response = await fetch('http://localhost:3001/api/timestamp');
      const data = await response.json();
      setTimestamp(data.timestamp);
    };

    fetchInitialTimestamp();

    // Listen for WebSocket events for real-time updates
    socket.on('newTimestamp', (newTimestamp) => {
      setTimestamp(newTimestamp);
    });

    // Clean up the socket connection on unmount
    return () => {
      socket.off('newTimestamp');
    };
  }, []);

  return (
    <div className="content-wrapper">
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
          content1={<TextDisplay display={timestamp}/>} // Automatically update the timestamp
          width="23%"
        />
      </div>

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