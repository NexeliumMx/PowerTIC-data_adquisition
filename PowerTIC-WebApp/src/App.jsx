import { useState } from 'react';
import reactLogo from './assets/react.svg';
import './App.css';
import HandleLogoDarkLightMode from './components/handleLogoDarkLightMode.jsx';
import Locations from './components/locations/Locations.jsx';

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div>
        <HandleLogoDarkLightMode />
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>PowerTIC</h1>
      <div className="card">
        <p>
          This WebApp is created with React!
        </p>
      </div>
      <section>
        <Locations />
      </section>
    </>
  );
}

export default App;