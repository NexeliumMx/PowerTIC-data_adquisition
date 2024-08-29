import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import Header from './Components/Header.jsx';
import './Users.scss';

export default function Users() {
  return (
    <div className="page-container">
      <Sidebar/>
      <div className="page-content">
        <Navbar title="Users" />
        <Header/>
        {/* The rest of the page will be blank */}
      </div>
    </div>
  );
}