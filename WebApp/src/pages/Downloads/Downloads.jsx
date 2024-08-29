import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import Header from './components/Header.jsx';
import DownloadTile from './components/DownloadTile';
import { FileBarChart } from 'lucide-react';
import './Downloads.scss';


function Downloads() {
   return (
     <div className="page-container">
       <Sidebar />
       <div className="page-content">
         <Navbar title="Descargas" />
         <Header />
         <div className="downloads-tile-container"> {/* Este es el contenedor grid */}
           <DownloadTile title='Enero' year='2024'/> 
           <DownloadTile title='Febrero' year='2024'/> 
           <DownloadTile title='Marzo' year='2024'/> 
           <DownloadTile title='Abril' year='2024'/> 
           <DownloadTile title='Mayo' year='2024'/> 
           <DownloadTile title='Junio' year='2024' /> 
           <DownloadTile title='Julio' year='2024'/> 
           <DownloadTile title='Agosto' year='2024'/> 
           <DownloadTile title='Septiembre' year='2024'  /> 
           <DownloadTile title='Octubre' year='2024'  /> 
           <DownloadTile title='Noviembre' year='2024'  /> 
           <DownloadTile title='Diciembre' year='2024' /> 
         </div>
       </div>
     </div>
   );
 }
 
 export default Downloads;