import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';

import UsersTile from './Components/Userstile.jsx'; // Asegúrate de que la ruta sea correcta
import './Users.scss';

export default function Users() {
  return (
    <div className="page-container">
      <Sidebar />
      <div className="page-content">
        <Navbar title="Users" />
      </div>
    </div>
  );
}

