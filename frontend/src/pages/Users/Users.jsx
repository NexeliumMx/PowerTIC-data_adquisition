import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import Header from './Components/Header.jsx';
import UserTable from './Components/UsersTable.jsx'; // Importa el componente de la tabla
import './Users.scss';

// Datos de ejemplo para los usuarios
const users = [
  { id: 1, name: 'Jon Snow', phone: '(665)121-5454', email: 'jonsnow@gmail.com', accessLevel: 'admin' },
  { id: 2, name: 'Cersei Lannister', phone: '(421)314-2288', email: 'cerseilannister@gmail.com', accessLevel: 'manager' },
  { id: 3, name: 'Jaime Lannister', phone: '(422)982-6739', email: 'jaimelannister@gmail.com', accessLevel: 'user' },
  { id: 4, name: 'Arya Stark', phone: '(921)425-6742', email: 'aryastark@gmail.com', accessLevel: 'user' },
  // Añade más usuarios según sea necesario
];

export default function Users() {
  return (
    <div className="page-container">
      <Sidebar />
      <div className="page-content">
        <Navbar title="Users" />
        <Header />
        <UserTable users={users} /> {/* Aquí integras la tabla de usuarios */}
      </div>
    </div>
  );
}
