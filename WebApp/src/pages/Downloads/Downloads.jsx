import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import './Downloads.scss';

function Downloads() {
  return (
    <div className="downloads-container">
      <Sidebar />
      <div className="downloads-content">
        <Navbar title="Downloads" />
        {/* The rest of the page will be blank */}
      </div>
    </div>
  );
}

export default Downloads;