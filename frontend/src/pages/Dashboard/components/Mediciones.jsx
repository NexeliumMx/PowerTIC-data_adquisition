import React from 'react';
import Tile from './Tile'; // Import your Tile component
import './Mediciones.scss'; // Import the styles


import Current from './charts/Current';
import HistoricPowerConsumption from './charts/HistoricPowerConsumption';
import HistoricPF from './charts/HistoricPF';
import HistoricRealPower from './charts/HistoricRealPower';
import HistoricReactivePower from './charts/HistoricReactivePower';

const Mediciones = () => {
  return (
<div className="mediciones-container">

<div className="CFP-container">
  <Tile className="corriente" title="Corriente" content1={<Current />} />
  <Tile className="factor-potencia" title="Factor de Potencia" content1={<HistoricPF />} />
</div>

<div className="potencias-container">
  <Tile className="potencias" title="Potencia Real" content1={<HistoricRealPower/>}/>
  <Tile className="potencias" title="Potencia Reactiva" content1={<HistoricReactivePower/>}/>
</div>
<div className="consumo-historico-container">
  <Tile className="consumo-historico" title="Consumo histórico" content1={<HistoricPowerConsumption />} />
</div>



</div>
  );
};

export default Mediciones;