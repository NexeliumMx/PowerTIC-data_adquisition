import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import Header from './components/Header.jsx';
import './Downloads.scss';

function Downloads() {
  return (
    <div className="page-container">
      <Sidebar />
      <div className="page-content">
        <Navbar title="Downloads" />
        {/* The rest of the page will be blank */}
        <Header />
      </div>
    </div>
  );
}

export default Downloads;