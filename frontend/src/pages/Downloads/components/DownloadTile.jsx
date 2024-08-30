import React from 'react';
import './DownloadTile.scss';

const DownloadTile = ({ title, year, Icon }) => {
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
      <p className="download-tile-label">DESCARGAR</p>
      </div>
    </div>
  );
};

export default DownloadTile;
