import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';

import LCTile from './Components/LCTile.jsx'; // Asegúrate de que la ruta sea correcta
import './LoadCenter.scss';

export default function Users() {
  return (
    <div className="page-container">
      <Sidebar />
      <div className="page-content">
        <Navbar title="Centros de Carga" />
        <div className="LC-tile-container"> {/* Este es el contenedor grid */}
          <LCTile title='SAN ÁNGEL' number='1' /> 
          <LCTile title='CLUB AMÉRICA' number='2' /> 
          <LCTile title='ESTADIO AZTECA' number='1' /> 
          <LCTile title='RADIOPOLIS' number='1' /> 
          <LCTile title='CORP. SANTA FE' number='4' /> 
          <LCTile title='CENTRO DE CARGA 6' number='#' /> 
        </div>
      </div>
    </div>
  );
}

