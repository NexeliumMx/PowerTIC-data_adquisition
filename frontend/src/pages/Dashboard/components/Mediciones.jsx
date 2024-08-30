import React from 'react';
import Tile from './Tile'; // Import your Tile component
import './Mediciones.scss'; // Import the styles


import Current from './charts/Current';
import VoltageLL from './charts/VoltageLL';
import TriPowerFactor from './charts/TriPowerFactor';
import VoltageLN from './charts/VoltageLN';
import RealPower from './charts/RealPower';
import ApparentPower from './charts/ApparentPower';
import ReactivePower from './charts/ReactivePower';

const Mediciones = () => {
  return (
    <div className="mediciones-container">
      <div className="mediciones-left">
        <Tile title="Corriente" content={<Current/>} />
        <Tile title="Voltage Linea - Linea" content={<VoltageLL/>} />
      </div>
      <div className="mediciones-center">
        <Tile title="Factor de Potencia" content={<TriPowerFactor/>} />
        <Tile title="Voltage Linea - Neutro" content={<VoltageLN/>} />
      </div>
      <div className="mediciones-right">
        <Tile title="Potencias" content={
          <div>
            <RealPower/>
            <ApparentPower/>
            <ReactivePower/>
          </div>
        } />
      </div>
    </div>
  );
};

export default Mediciones;