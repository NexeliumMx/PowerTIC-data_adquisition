import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

const HistoricPF = () => {
  const [data, setData] = useState([]);

  // Fetch data from the /api/historicpf endpoint when the component mounts
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/historicpf');
        const result = await response.json();
        setData(result); // Set the data state with the fetched result
      } catch (error) {
        console.error('Error fetching historic power factor data:', error);
      }
    };

    fetchData(); // Call fetchData on component mount
  }, []);

  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={data} margin={{ top: 20, right: 30, left: 30, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
        <XAxis dataKey="name" tick={{ fill: '#ccc', fontSize: 18 }} reversed={true} />
        <YAxis 
          tick={{ fill: '#ccc', fontSize: 18 }} 
          domain={[0.90, 1.0]} // Set domain to match expected power factor range
          ticks={[0.92, 0.94, 0.96, 0.98, 1.00]} // Customize Y-axis ticks
        />
        <Tooltip />
        <Legend />
        {/* Line for the promedio */}
        <Line type="monotone" dataKey="promedio" stroke="#69B2A6" name="Promedio" strokeWidth={2} />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default HistoricPF;