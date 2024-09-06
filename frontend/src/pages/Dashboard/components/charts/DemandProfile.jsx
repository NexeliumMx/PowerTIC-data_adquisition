import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Enero', value: 0 },
  { name: 'Febrero', value: 0 },
  { name: 'Marzo', value: 0 },
  { name: 'Abril', value: 0 },
  { name: 'Mayo', value: 0 },
  { name: 'Junio', value: 0 },
  { name: 'Julio', value: 0 },
  { name: 'Agosto', value: 0 },
  { name: 'Septiembre', value: 0 },
  { name: 'Octubre', value: 0 },
  { name: 'Noviembre', value: 0 },
  { name: 'Diciembre', value: 0 },
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