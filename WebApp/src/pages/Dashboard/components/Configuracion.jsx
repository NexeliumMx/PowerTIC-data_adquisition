// src/pages/Dashboard/components/Configuracion.jsx
import React from 'react';
import Tile from './Tileconfig'; // Import the Tile component
import './Configuración.scss';


const Configuración = () => {
  return (
    <div className="configuración-container">

      <div className="configuración-ID-left">
        <Tile title="ID:"  content='Número ID identificador del sensor' />
      </div>

      <div className="configuración-UBI-right">
        <Tile title="UBICACIÓN:" content='Ubicación del medidor'/>
      </div>

      <div className="configuración-MOD-center">
        <Tile title="MODELO:" content='Número de modelo del medidor'/>
      </div>

      <div className="configuración-FAB-left">
        <Tile title="FABRICANTE:" content='AcuRev'/>
      </div>

      <div className="configuración-VER-right">
        <Tile title="VERSIÓN:" content='Número de la versión de software'/>
      </div>

      <div className="configuración-SER-left">
        <Tile title="SERIAL:" content='Número de serie del medidor'/>
      </div>
      <div className="configuración-REG-right">
        <Tile title="REGISTRO:" content='Fecha de registro del medidor'/>
      </div>

    </div>
  
  );
};

export default Configuración;