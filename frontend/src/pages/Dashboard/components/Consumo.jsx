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

const socket = io('http://localhost:3001');

const Consumo = () => {
  const [timestamp, setTimestamp] = useState('');
  const [maxDemand, setMaxDemand] = useState({
    max_total_real_power: '0.000',
    max_reactive_power_var: '0.000'
  });

  const [powerConsumption, setPowerConsumption] = useState({
    total_real_energy_imported: '0.000',
    total_var_hours_imported_q1: '0.000',
    total_var_hours_imported_q2: '0.000'
  });

  const [powerFactorData, setPowerFactorData] = useState([
    { name: 'Filled', value: 75 },
    { name: 'Unfilled', value: 25 }
  ]);

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

  // Fetch the max demand values when the component mounts
  useEffect(() => {
    const fetchMaxDemand = async () => {
      const response = await fetch('http://localhost:3001/api/maxdemand');
      const data = await response.json();
      setMaxDemand(data); // Set max demand data to state
    };

    fetchMaxDemand(); // Call fetchMaxDemand when the component mounts
  }, []);

  // Fetch the power consumption values when the component mounts
  useEffect(() => {
    const fetchPowerConsumption = async () => {
      const response = await fetch('http://localhost:3001/api/powerconsumption');
      const data = await response.json();
      setPowerConsumption(data); // Set power consumption data to state
    };

    fetchPowerConsumption(); // Call fetchPowerConsumption when the component mounts
  }, []);

  // Fetch the power factor value and update the donut chart data
  useEffect(() => {
    const fetchPowerFactor = async () => {
      const response = await fetch('http://localhost:3001/api/lastpf');
      const data = await response.json();
      const filled = (data.power_factor * 100).toFixed(1); // Normalize to percentage
      const unfilled = (100 - filled).toFixed(1); // Remaining percentage

      // Update the donut chart data based on power factor
      setPowerFactorData([
        { name: 'Filled', value: parseFloat(filled) },
        { name: 'Unfilled', value: parseFloat(unfilled) }
      ]);
    };

    fetchPowerFactor(); // Call fetchPowerFactor when the component mounts
  }, []);

  return (
    <div className="content-wrapper">
      <div className="small-tiles-container">
        <Tile 
          title="Demanda Máxima" 
          icon={Activity} 
          content1={<TextDisplay display={`${maxDemand.max_total_real_power} kW`}/>} // Display max total real power
          content2={<TextDisplay display={`${maxDemand.max_reactive_power_var} kVAR`}/>} // Display max reactive power
          width="21%"
        />
        <Tile 
          title="Consumo Acumulado" 
          icon={BatteryCharging} 
          content1={<TextDisplay display={`${powerConsumption.total_real_energy_imported} kWh`}/>} // Display total real energy imported
          content2={<TextDisplay display={`${powerConsumption.total_var_hours_imported_q1} kVArh`}/>} // Display total var hours imported q1
          width="21%"
        />
        <Tile 
          title="Factor de Potencia" 
          icon={Gauge} 
          content1={
            <PowerFactor 
              data={powerFactorData} 
              colors={COLORS} 
              powerFactor={powerFactorData[0]?.value / 100} // Passing the power factor value
            />
          }
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