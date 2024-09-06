import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

const HistoricReactivePower = () => {
  const [data, setData] = useState([]);

  // Fetch data from the /api/historicreactivepower endpoint when the component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/historicreactivepower');
        const result = await response.json();
        setData(result); // Set the data state with the fetched result
      } catch (error) {
        console.error('Error fetching historic reactive power data:', error);
      }
    };

    fetchData(); // Call fetchData on component mount
  }, []);

  return (
    <div>
      <h2 style={{ textAlign: 'center', color: '#69B2A6', marginBottom: '20px' }}>Potencia Reactiva</h2>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={data} margin={{ top: 0, right: 30, left: 30, bottom: 0 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
          <XAxis dataKey="name" tick={{ fill: '#ccc', fontSize: 18 }} reversed={true} />
          <YAxis tick={{ fill: '#ccc', fontSize: 18 }} domain={[0, 8]} />
          <Tooltip />
          <Legend />
          {/* Líneas de tendencia para el promedio y cada fase */}
          <Line type="monotone" dataKey="promedio" stroke="#69B2A6" name="Promedio" strokeWidth={2} />
          <Line type="monotone" dataKey="faseA" stroke="#83C5B1" name="Fase A" strokeWidth={2} />
          <Line type="monotone" dataKey="faseB" stroke="#FFBB28" name="Fase B" strokeWidth={2} />
          <Line type="monotone" dataKey="faseC" stroke="#FF8042" name="Fase C" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};

export default HistoricReactivePower;