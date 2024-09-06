import React, { useEffect, useState } from 'react';
import Tile from './Tile'; // Import the Tile component
import { Activity, BatteryCharging, Gauge, Clock } from 'lucide-react';
import './Consumo.scss'; // Import the styles for Consumo

import ConsumptionHistory from './charts/ConsumptionHistory.jsx'; 
import DemandProfile from './charts/DemandProfile.jsx';
import PowerFactor from './charts/PowerFactor.jsx';
import TextDisplay from './charts/TextDisplay.jsx';

import COLORS from '../../../styles/chartColors.js';
import data from './charts/pieChartData.js';

const Consumo = () => {
  const [timestamp, setTimestamp] = useState(''); // State to hold the fetched timestamp

  useEffect(() => {
    // Fetch the timestamp from the backend API
    const fetchTimestamp = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/timestamp'); // Adjust URL as needed
        const data = await response.json();
        console.log('Fetched timestamp:', data.timestamp); // Log the fetched timestamp
        setTimestamp(data.timestamp); // Set the fetched timestamp
      } catch (error) {
        console.error('Error fetching timestamp:', error);
      }
    };

    // Call the function to fetch the timestamp
    fetchTimestamp();

    // Optionally, you can set an interval to periodically fetch the timestamp if needed
    const intervalId = setInterval(fetchTimestamp, 60000); // Fetch timestamp every minute

    // Cleanup interval on component unmount
    return () => clearInterval(intervalId);
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
          content1={<TextDisplay display={timestamp}/>} // Display the fetched timestamp
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