/**
 * This component renders a list of location buttons fetched from the Firebase Firestore database.
 * When a location button is clicked, it displays the name of the location and prints the assigned power meters.
 *
 * Author: Arturo Vargas Cuevas
 * Last Modified: 2024-08-03, by Arturo Vargas Cuevas
 */

import React, { useState, useEffect } from 'react';
import getLocations from './getLocations';
import getName from './getName';
import getAssignedPowerMeters from './getAssignedPowerMeters';

function Locations() {
  const [locations, setLocations] = useState([]);
  const [selectedLocation, setSelectedLocation] = useState(null);
  const [locationName, setLocationName] = useState(null);
  const [assignedPowerMeters, setAssignedPowerMeters] = useState([]);

  useEffect(() => {
    async function fetchLocations() {
      const locationIds = await getLocations();
      setLocations(locationIds);
    }
    
    fetchLocations();
  }, []);

  const handleClick = async (location) => {
    setSelectedLocation(location);
    const name = await getName(location);
    setLocationName(name);
    const powerMeters = await getAssignedPowerMeters(location);
    setAssignedPowerMeters(powerMeters); // Set assigned power meters
  };

  return (
    <div>
      <div>
        {locations.map((location) => (
          <button key={location} onClick={() => handleClick(location)}>
            {location}
          </button>
        ))}
      </div>
      {selectedLocation && (
        <div>
          <h2>{locationName || selectedLocation}</h2>
          <p>You have clicked the {selectedLocation} button</p>
          <div>
            {assignedPowerMeters.map((powerMeter) => (
              <button key={powerMeter}>{powerMeter}</button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default Locations;