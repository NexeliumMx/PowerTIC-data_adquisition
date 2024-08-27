import React from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import './Users.scss';

function Users() {
  return (
    <div className="page-container">
      <Sidebar />
      <div className="page-content">
        <Navbar title="Users" />
        {/* The rest of the page will be blank */}
      </div>
    </div>
  );
}

export default Users;