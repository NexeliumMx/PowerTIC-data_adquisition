import React from 'react';
import './LCTile.scss';

const UsersTile = ({ title, number, icon }) => {
  return (
    <div className="LC-tile">
      <div className="LC-tile-section">
        <p className="LC-tile-label">Centro de carga:</p>
        <p className="LC-tile-value">{title}</p>
      </div>
      <div className="LC-tile-section">
        <p className="LC-tile-label">#Medidores</p>
        <p className="LC-tile-value">{number}</p>
      </div>
    </div>
  );
};

export default UsersTile;