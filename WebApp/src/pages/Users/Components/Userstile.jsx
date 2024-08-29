import React from 'react';
import './UsersTile.scss';

const UsersTile = ({ title, number, icon }) => {
  return (
    <div className="download-tile">
      <div className="user-tile-section">
        <p className="download-tile-label">Centro de carga:</p>
        <p className="download-tile-value">{title}</p>
      </div>
      <div className="download-tile-section">
        <p className="download-tile-label">#Medidores</p>
        <p className="download-tile-value">{number}</p>
      </div>
    </div>
  );
};

export default UsersTile;