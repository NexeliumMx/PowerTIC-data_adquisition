import React from 'react';
import Tile from './Tile'; // Import your Tile component
import './Mediciones.scss'; // Import the styles

const Mediciones = () => {
  return (
    <div className="mediciones-container">
      <div className="mediciones-left">
        <Tile title="Corriente" content="Content for Corriente" />
        <Tile title="Voltage Linea - Linea" content="Content for Voltage Linea - Linea" />
      </div>
      <div className="mediciones-center">
        <Tile title="Factor de Potencia" content="Content for Factor de Potencia" />
        <Tile title="Voltage Linea - Neutro" content="Content for Voltage Linea - Neutro" />
      </div>
      <div className="mediciones-right">
        <Tile title="Potencias" content="Content for Potencias" />
      </div>
    </div>
  );
};

export default Mediciones;