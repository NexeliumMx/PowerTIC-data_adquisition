import React from 'react';
import './DownloadTile.scss';

const DownloadTile = ({ title, year, icon }) => {
  return (
    <div className="download-tile">
      <div className="download-tile-section">
        <p className="download-tile-label">MES</p>
        <p className="download-tile-value">{title}</p>
      </div>
      <div className="download-tile-section">
        <p className="download-tile-label">AÑO</p>
        <p className="download-tile-value">{year}</p>
      </div>
      <div className="download-tile-section download-tile-icon">
        <p className="download-tile-label">ARCHIVO</p>
        <p className="download-tile-value">{icon}</p>
      </div>
    </div>
  );
};

export default DownloadTile;
