/**
 * This is the main application component for the PowerTIC project.
 * It includes the logo, a header, and the Locations component.
 *
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-08-03, by Arturo Vargas Cuevas
 */

import reactLogo from './assets/react.svg';
import './App.css';
import HandleLogoDarkLightMode from './components/handleLogoDarkLightMode.jsx';
import Locations from './components/locations/Locations';


function App() {
  return (
    <>
      <div>
        <HandleLogoDarkLightMode />
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>PowerTIC</h1>
      <Locations />
    </>
  );
}

export default App;