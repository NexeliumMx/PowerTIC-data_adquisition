import { useState } from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.jsx';
import Navbar from '../../components/Navbar/Navbar.jsx';
import Header from './components/Header.jsx';  // Import Header directly
import Consumo from './components/Consumo';
import Mediciones from './components/Mediciones';
import Configuracion from './components/Configuracion';

import CustomPieChart from './components/charts/CustomPieChart.jsx';

export default function Dashboard() {
  const [activeContent, setActiveContent] = useState('consumo');

  let content;
  if (activeContent === 'consumo') {
    content = <Consumo />;
  } else if (activeContent === 'mediciones') {
    content = <Mediciones />;
  } else if (activeContent === 'configuracion') {
    content = <Configuracion />;
  }

  return (
    <div className="page-container">
      <Sidebar />
      <div className="page-content">
        <Navbar title="Dashboard" />
        <Header setActiveContent={setActiveContent} />

        {/* Render the active content */}
        {content}
      </div>
    </div>
  );
}