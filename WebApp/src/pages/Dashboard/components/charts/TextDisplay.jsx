import React from 'react';
import './TextDisplay.scss';

const TextDisplay = ({ display }) => {
  return (
    <div className="text-display-container">
      {display}
    </div>
  );
};

export default TextDisplay;