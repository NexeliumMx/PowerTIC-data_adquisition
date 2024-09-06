import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Text } from 'recharts';

const renderCustomLabel = ({ x, y, width, value }) => (
  <Text x={x + width / 2} y={y} fill={value >= 0.5 ? '#F2A007' : '#69B2A6'} textAnchor="middle" dy={-10} fontSize={18}>
    {value}
  </Text>
);

const Current = () => {
  const [currentData, setCurrentData] = useState([
    { name: 'Promedio por fase', value: 0, color: '#69B2A6' },
    { name: 'Fase A', value: 0, color: '#83C5B1' },
    { name: 'Fase B', value: 0, color: '#83C5B1' },
    { name: 'Fase C', value: 0, color: '#83C5B1' },
    { name: 'Desbalance %', value: 0, color: '#F2A007' },
  ]);

  // Fetch current data from the API when the component mounts
  useEffect(() => {
    const fetchCurrentData = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/current');
        const data = await response.json();

        // Calculate the average phase current
        const averagePhase = ((data.amps_phase_a + data.amps_phase_b + data.amps_phase_c) / 3).toFixed(2);

        // Update the data state with the fetched values
        setCurrentData([
          { name: 'Promedio por fase', value: parseFloat(averagePhase), color: '#69B2A6' },
          { name: 'Fase A', value: data.amps_phase_a, color: '#83C5B1' },
          { name: 'Fase B', value: data.amps_phase_b, color: '#83C5B1' },
          { name: 'Fase C', value: data.amps_phase_c, color: '#83C5B1' },
          { name: 'Desbalance %', value: parseFloat(data.current_imbalance), color: '#F2A007' },
        ]);
      } catch (error) {
        console.error('Error fetching current data:', error);
      }
    };

    fetchCurrentData();
  }, []);

  return (
    <ResponsiveContainer width="100%" height={400}>
      <BarChart data={currentData} margin={{ top: 20, right: 30, left: 30, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
        <XAxis dataKey="name" tick={{ fill: '#ccc', fontSize: 18 }} />
        <YAxis tick={{ fill: '#ccc', fontSize: 18 }} />
        <Tooltip />
        <Bar dataKey="value" fill="#8884d8">
          {currentData.map((entry, index) => (
            <Bar key={`bar-${index}`} dataKey="value" fill={entry.color} label={renderCustomLabel} />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
};

export default Current;