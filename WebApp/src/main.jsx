import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App.jsx';
import './styles/global.scss';

// Find the root element
const rootElement = document.getElementById('root');

// Create the root container using createRoot
const root = createRoot(rootElement);

// Render your application within the root
root.render(
  <Router>
    <App />
  </Router>
);