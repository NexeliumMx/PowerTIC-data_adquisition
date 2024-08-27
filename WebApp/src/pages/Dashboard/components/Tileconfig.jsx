import React from 'react';
import './Tileconfig.scss'; // Create this file for styles

const Tileconfig = ({ title, icon: Icon, content, width }) => {
  return (
    <div className="tileconfig-container" style={{ width: width }}>
      <div className="tileconfig-header">
        {Icon && <Icon className="tileconfig-icon" />}
        <h3 className="tileconfig-title">{title}</h3>
      </div>
      <div className="tileconfig-content">
        {content}
      </div>
    </div>
  );
}

export default Tileconfig;