import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Enero', value: 250 },
  { name: 'Febrero', value: 800 },
  { name: 'Marzo', value: 300 },
  { name: 'Abril', value: 100 },
  { name: 'Mayo', value: 100 },
  { name: 'Junio', value: 500 },
  { name: 'Julio', value: 400 },
  { name: 'Agosto', value: 200 },
  { name: 'Septiembre', value: 950 },
  { name: 'Octubre', value: 100 },
  { name: 'Noviembre', value: 900 },
  { name: 'Diciembre', value: 1000 },
];

const DemandProfile = () => {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={data} margin={{ top: 20, right: 50, left: 50, bottom: 20 }}>
        <CartesianGrid stroke="#ccc" strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="value" stroke="#69B2A6" dot={{ fill: '#69B2A6', strokeWidth: 2, r: 5 }} />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default DemandProfile;