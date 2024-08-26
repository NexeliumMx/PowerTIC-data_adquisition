import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import './Dashboard.scss';  // Import the Dashboard-specific styles

function Dashboard() {
  return (
    <div className="dashboard-container">
      <Sidebar />
      <div className="dashboard-content">
        <h1>Dashboard</h1>
        {/* Other content goes here */}
      </div>
    </div>
  );
}

export default Dashboard;
