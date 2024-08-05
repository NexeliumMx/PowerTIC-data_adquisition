// /src/components/locations/Locations.jsx

/**
 * DESCRIPTION
 * DESCRIPTION
 *
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-08-03, by Arturo Vargas Cuevas
 */

import React, { useState, useEffect } from 'react';
import getLocations from './getLocations.js';

function Locations() {
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    async function fetchLocations() {
      const locationIds = await getLocations();
      setLocations(locationIds);
    }
    
    fetchLocations();
  }, []);

  return (
    <div>
      <h2>Locations</h2>
      {locations.map((location) => (
        <button key={location}>{location}</button>
      ))}
    </div>
  );
}

export default Locations;
