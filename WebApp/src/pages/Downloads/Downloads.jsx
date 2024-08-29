import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import Header from './components/Header.jsx';
import Tile from './components/DownloadTile';
import { FileBarChartIcon } from 'lucide-react';
import './Downloads.scss';


function Downloads() {
  return (
    <div className="downloads-container">
      <Sidebar />
      <div className="downloads-content">
        <Navbar title="Descargas"/>
        <Header/>

        <div classname="downloads-tile-container">
          <div classname="downloads-ENE">
             <Tile title= "Enero" year="2024"/>
          </div>

          <div classname="downloads-FEB">
             <Tile title= "Febrero" year="2024"/>
          </div>
          <div classname="downloads-MAR">
             <Tile title= "Marzo" year="2024"/>
          </div>
          <div classname="downloads-ABR">
             <Tile title= "Abril" year="2024"/>
          </div>
          <div classname="downloads-MAY">
             <Tile title= "Mayo" year="2024"/>
          </div>
          <div classname="downloads-JUN">
             <Tile title= "Junio" year="2024"/>
          </div>
          <div classname="downloads-JUL">
             <Tile title= "Julio" year="2024"/>
          </div>
          <div classname="downloads-AGO">
             <Tile title= "Agosto" year="2024"/>
          </div>
          <div classname="downloads-SEPT">
             <Tile title= "Septiembre" year="2023"/>
          </div>
          <div classname="downloads-OCT">
             <Tile title= "Octubre" year="2023"/>
          </div>
          <div classname="downloads-NOV">
             <Tile title= "Noviembre" year="2023"/>
          </div>
          <div classname="downloads-DIC">
             <Tile title= "Diciembre" year="2023"/>
          </div>

        </div>

      </div>
    </div>
  );
}

export default Downloads;