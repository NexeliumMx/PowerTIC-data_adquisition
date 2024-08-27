import React from 'react';
import './Header.scss'; // Import the Header-specific styles

const Header = ({ headerMenu: HeaderMenu }) => {
  return (
    <div className="header-container">
      <div className="header-titles">
        <h1>Centro de Carga 1</h1>
        <h2>San Ángel</h2>
      </div>
      <div className="header-menu">
        {HeaderMenu && <HeaderMenu />}
      </div>
    </div>
  );
};

export default Header;
