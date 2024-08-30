import React from 'react';
import Tile from './Tile'; // Import the Tile component
import { Activity, BatteryCharging, Gauge, Clock } from 'lucide-react';
import './Consumo.scss'; // Import the styles for Consumo

const Consumo = () => {
  return (
    <div className="content-wrapper">
      {/* Small Tiles Container */}
      <div className="small-tiles-container">
        <Tile 
          title="Demanda Máxima" 
          icon={Activity} 
          content="12,000 kW" 
          width="23%"
        />
        <Tile 
          title="Consumo Acumulado" 
          icon={BatteryCharging} 
          content="70,000 kWh" 
          width="23%"
        />
        <Tile 
          title="Factor de Potencia" 
          icon={Gauge} 
          content="0.75" 
          width="23%"
        />
        <Tile 
          title="Tiempo" 
          icon={Clock} 
          content="03 de Agosto de 2024 17:23" 
          width="23%"
        />
      </div>

      {/* Big Tiles Container */}
      <div className="big-tiles-container">
        <Tile 
          title="Perfil de Demanda" 
          icon={Activity} 
          content={<div>Your custom content here</div>} 
          width="57%"
        />
        <Tile 
          title="Historial de Consumo" 
          icon={BatteryCharging} 
          content={<div>Your custom content here</div>} 
          width="43%"
        />
      </div>
    </div>
  );
}

export default Consumo;