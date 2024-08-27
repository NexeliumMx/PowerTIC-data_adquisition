import React, { useState, useEffect } from 'react';
import { Activity, Gauge, Settings } from 'lucide-react';
import './Header.scss';

const Header = ({ setActiveContent }) => {
  const [activeButton, setActiveButton] = useState('consumo');

  const buttons = [
    { id: 'consumo', label: 'Consumo', icon: <Activity /> },
    { id: 'mediciones', label: 'Mediciones', icon: <Gauge /> },
    { id: 'configuracion', label: 'Configuración', icon: <Settings /> },
  ];

  const handleButtonClick = (buttonId) => {
    setActiveButton(buttonId);
    setActiveContent(buttonId);
  };

  useEffect(() => {}, [activeButton]);

  return (
    <div className="header-container">
      <div className="header-titles">
        <h1>Centro de Carga 1</h1>
        <h2>San Ángel</h2>
      </div>
      <div className="header-menu">
        <div className="header-menu-container">
          {buttons.map((button) => (
            <button
              key={button.id}
              className={`header-menu-button ${activeButton === button.id ? 'active' : ''}`}
              onClick={() => handleButtonClick(button.id)}
            >
              {button.icon}
              <span>{button.label}</span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Header;