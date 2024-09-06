import React, { useEffect, useState } from 'react';
import Tile from './Tile'; // Import the Tile component
import { Activity, BatteryCharging, Gauge, Clock } from 'lucide-react';
import './Consumo.scss'; // Import the styles for Consumo

import ConsumptionHistory from './charts/ConsumptionHistory.jsx'; 
import DemandProfile from './charts/DemandProfile.jsx';
import PowerFactor from './charts/PowerFactor.jsx';
import TextDisplay from './charts/TextDisplay.jsx';

import getFormattedTimestamp from '../../../scripts/queryTimestamp.js'; // Import the timestamp function
import COLORS from '../../../styles/chartColors.js';
import data from './charts/pieChartData.js';

const Consumo = () => {
  const [timestamp, setTimestamp] = useState('');

  useEffect(() => {
    const fetchTimestamp = async () => {
      const result = await getFormattedTimestamp();
      setTimestamp(result);
    };
    
    fetchTimestamp();
  }, []);

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
          content1={<TextDisplay display={timestamp}/>} // Use the fetched timestamp here
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