import React from 'react';
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
  return (
    <div className="content-wrapper">
      {/* Small Tiles Container */}
      <div className="small-tiles-container">
        <Tile 
          title="Demanda Máxima" 
          icon={Activity} 
          content={<TextDisplay display="10 000 kW"/>}
          width="23%"
        />
        <Tile 
          title="Consumo Acumulado" 
          icon={BatteryCharging} 
          content={<TextDisplay display="70 000 kWh"/>} 
          width="23%"
        />
        <Tile 
          title="Factor de Potencia" 
          icon={Gauge} 
          content={<PowerFactor data={data} colors={COLORS}/>} 
          width="23%"
        />
        <Tile 
          title="Tiempo" 
          icon={Clock} 
          content={<TextDisplay display="03 de Agosto de 2024 17:23"/>} 
          width="23%"
        />
      </div>

      {/* Big Tiles Container */}
      <div className="big-tiles-container">
        <Tile 
          title="Perfil de Demanda" 
          icon={Activity} 
          content={<DemandProfile />} 
          width="57%"
        />
        <Tile 
          title="Historial de Consumo" 
          icon={BatteryCharging} 
          content={<ConsumptionHistory />}
          width="43%"
        />
      </div>
    </div>
  );
}

export default Consumo;