import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import Header from './Components/Header.jsx';
import Tile from './Components/Userstile.jsx';
import './Users.scss';

export default function Users() {
  return (
    <div className="page-container">
      <Sidebar/>
      <div className="page-content">
        <Navbar title="Users"/>

        <div className='user-1'>
          <Tile title='SAN ÁNGEL' number='1' /> 
        </div>
        <div className='user-2'>
          <Tile title='CLUB AMÉRICA' number='2' /> 
        </div>
        <div className='user-3'>
          <Tile title='ESTADIO AZTECA' number='1' /> 
        </div>
        <div className='user-4'>
          <Tile title='RADIOPOLIS' number='1' /> 
        </div>
        <div className='user-5'>
          <Tile title='CORP. SANTA FE' number='4' /> 
        </div>
        <div className='user-6'>
          <Tile title='CENTRO DE CARGA 6' number='#' /> 
        </div>
        
      </div>
    </div>
  );
}