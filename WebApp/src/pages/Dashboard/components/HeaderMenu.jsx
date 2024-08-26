import React, { useState } from 'react';
import { Activity, Gauge, Settings } from 'lucide-react';
import './HeaderMenu.scss'; // Import the HeaderMenu-specific styles

const HeaderMenu = () => {
  const [activeButton, setActiveButton] = useState('consumo');

  const buttons = [
    { id: 'consumo', label: 'Consumo', icon: <Activity /> },
    { id: 'mediciones', label: 'Mediciones', icon: <Gauge /> },
    { id: 'configuracion', label: 'Configuración', icon: <Settings /> },
  ];

  return (
    <div className="header-menu-container">
      {buttons.map((button) => (
        <button
          key={button.id}
          className={`header-menu-button ${activeButton === button.id ? 'active' : ''}`}
          onClick={() => setActiveButton(button.id)}
        >
          {button.icon}
          <span>{button.label}</span>
        </button>
      ))}
    </div>
  );
};

export default HeaderMenu;
