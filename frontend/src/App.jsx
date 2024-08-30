import React from 'react';
import { Routes, Route } from 'react-router-dom';

//Pages Routes
import Dashboard from './pages/Dashboard/Dashboard.jsx';
import Downloads from './pages/Downloads/Downloads.jsx';
import Home from './pages/Home/Home.jsx';
import LoadCenter from './pages/LoadCenter/LoadCenter.jsx';
import NotFound from './pages/NotFound/NotFound.jsx';
import TestPage from './pages/TestPage/TestPage.jsx';
import Users from './pages/Users/Users.jsx';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/downloads" element={<Downloads />} />
      <Route path="/load-center" element={<LoadCenter />} />
      <Route path="*" element={<NotFound />} />
      <Route path="/testpage" element={<TestPage />} />
      <Route path="/users" element={<Users />} />
    </Routes>
  );
};

export default App;