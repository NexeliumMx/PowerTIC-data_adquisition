import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

const HistoricPowerConsumption = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetch data from the API endpoint
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:3001/api/historicpowerconsumption');
        const result = await response.json();
        setData(result); // Set the fetched data
      } catch (error) {
        console.error('Error fetching historic power consumption:', error);
      }
    };

    fetchData(); // Call the function to fetch data on component mount
  }, []);

  return (
    <ResponsiveContainer width="100%" height={400}>
      <BarChart data={data} margin={{ top: 20, right: 30, left: 30, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
        <XAxis dataKey="name" tick={{ fill: '#ccc', fontSize: 18 }} reversed={true} />
        <YAxis tick={{ fill: '#ccc', fontSize: 18 }} />
        <Tooltip />
        <Legend />
        {/* Bar for KW/h */}
        <Bar dataKey="kw" fill="#69B2A6" name="KW/h" />
        {/* Bar for KVAr/h */}
        <Bar dataKey="kvar" fill="#FFBB28" name="KVAr/h" />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default HistoricPowerConsumption;