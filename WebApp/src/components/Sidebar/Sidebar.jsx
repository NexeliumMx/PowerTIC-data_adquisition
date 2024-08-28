import React, { useState } from 'react';
import { Menu } from 'lucide-react';
import './Sidebar.scss'; // Import the Sidebar-specific styles

function Sidebar() {
  const [isCollapsed, setIsCollapsed] = useState(false);

  const toggleSidebar = () => {
    setIsCollapsed(!isCollapsed);
  };

  return (
    <div className={`sidebar-container ${isCollapsed ? 'collapsed' : ''}`}>
      <div className="sidebar-header">
        <h1 className="sidebar-title">PowerTIC</h1>
        <Menu className="menu-icon" onClick={toggleSidebar} />
      </div>
      {!isCollapsed && (
        <>
          <p>Sistema de Medición Profesional</p>
          <h2>San Ángel</h2>
        </>
      )}
      <ul className="sidebar-menu">
        <li>
          <i className="bx bx-building-house"></i> 
          <span>Centros de Carga</span>
        </li>
        <li>
          <i className="bx bx-building-house"></i> 
          <span>Dashboard</span>
        </li>
        <li>
          <i className="bx bx-building-house"></i> 
          <span>Centro de Carga 1</span>
        </li>
        <li>
          <i className="bx bx-building-house"></i> 
          <span>Centro de Carga 2</span>
        </li>
        <li>
          <i className="bx bx-building-house"></i> 
          <span>Centro de Carga 3</span>
        </li>
        <li>
          <i className="bx bx-building-house"></i> 
          <span>Centro de Carga 4</span>
        </li>
        <li>
          <i className="bx bx-building-house"></i> 
          <span>Descargas</span>
        </li>
      </ul>
    </div>
  );
}

export default Sidebar;
