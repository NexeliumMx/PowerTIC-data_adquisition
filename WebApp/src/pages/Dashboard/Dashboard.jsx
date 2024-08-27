import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import Header from '../../components/Header/Header.jsx';
import HeaderMenu from './components/HeaderMenu'; // Import the specific HeaderMenu for Dashboard
import SmallTile from './components/SmallTile'; // Import the SmallTile component
import { Activity, BatteryCharging, Gauge, Clock } from 'lucide-react'; // Example icons
import './Dashboard.scss';  // Import the Dashboard-specific styles

function Dashboard() {
  return (
    <div className="dashboard-container">
      <Sidebar />
      <div className="dashboard-content">
        <Navbar title="Dashboard" />
        <Header headerMenu={HeaderMenu} />

        {/* Small Tiles Container */}
        <div className="small-tiles-container" style={{ backgroundColor: 'pink', padding: '1rem' }}>
          <SmallTile title="Demanda Máxima" icon={Activity} content="12,000 kW" />
          <SmallTile title="Consumo Acumulado" icon={BatteryCharging} content="70,000 kWh" />
          <SmallTile title="Factor de Potencia" icon={Gauge} content="0.75" />
          <SmallTile title="Tiempo" icon={Clock} content="03 de Agosto de 2024 17:23" />
        </div>

        <h1>Dashboard</h1>
        {/* Other content goes here */}
      </div>
    </div>
  );
}

export default Dashboard;