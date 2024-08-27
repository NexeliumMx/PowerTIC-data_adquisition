import React from 'react';
import './SmallTile.scss'; // Import the styles for the SmallTile

const SmallTile = ({ title, icon: Icon, content }) => {
  return (
    <div className="small-tile-container">
      <div className="small-tile-header">
        {Icon && <Icon className="small-tile-icon" />}
        <h3>{title}</h3>
      </div>
      <div className="small-tile-content">
        {content}
      </div>
    </div>
  );
};

export default SmallTile;