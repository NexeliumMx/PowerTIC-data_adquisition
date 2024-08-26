import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import Header from '../../components/Header/Header.jsx';
import HeaderMenu from './components/HeaderMenu'; // Import the specific HeaderMenu for Dashboard
import './Dashboard.scss';  // Import the Dashboard-specific styles

function Dashboard() {
  return (
    <div className="dashboard-container">
      <Sidebar />
      <div className="dashboard-content">
        <Navbar title="Dashboard" />
        <Header headerMenu={HeaderMenu} /> {/* Pass HeaderMenu as a prop */}
        <h1>Dashboard</h1>
        {/* Other content goes here */}
      </div>
    </div>
  );
}

export default Dashboard;