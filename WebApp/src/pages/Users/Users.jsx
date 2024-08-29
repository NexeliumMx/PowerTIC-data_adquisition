import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';

import UsersTile from './Components/Userstile.jsx'; // Asegúrate de que la ruta sea correcta
import './Users.scss';

export default function Users() {
  return (
    <div className="page-container">
      <Sidebar />
      <div className="page-content">
        <Navbar title="Users" />
        <div className="users-tile-container"> {/* Este es el contenedor grid */}
          <UsersTile title='SAN ÁNGEL' number='1' /> 
          <UsersTile title='CLUB AMÉRICA' number='2' /> 
          <UsersTile title='ESTADIO AZTECA' number='1' /> 
          <UsersTile title='RADIOPOLIS' number='1' /> 
          <UsersTile title='CORP. SANTA FE' number='4' /> 
          <UsersTile title='CENTRO DE CARGA 6' number='#' /> 
        </div>
      </div>
    </div>
  );
}

