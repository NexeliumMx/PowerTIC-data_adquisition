import React from 'react';
import Tile from './Tile'; // Import your Tile component
import './Mediciones.scss'; // Import the styles


import Current from './charts/Current';
import VoltageLL from './charts/VoltageLL';
import TriPowerFactor from './charts/TriPowerFactor';
import RealPower from './charts/RealPower';
import ReactivePower from './charts/ReactivePower';

const Mediciones = () => {
  return (
<div className="mediciones-container">

<div className="CFP-container">
  <Tile className="corriente" title="Corriente" content1={<Current />} />
  <Tile className="factor-potencia" title="Factor de Potencia" content1={<TriPowerFactor />} />
</div>

<div className="potencias-container">
  <Tile className="potencias" title="Potencia Real" content1={<RealPower/>}/>
  <Tile className="potencias" title="Potencia Reactiva" content1={<ReactivePower/>}/>
</div>
<div className="consumo-historico-container">
  <Tile className="consumo-historico" title="Consumo histórico" content1={<VoltageLL />} />
</div>



</div>
  );
};

export default Mediciones;