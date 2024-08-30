import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Text } from 'recharts';

const data = [
  { name: 'Promedio', value: 133, color: '#69B2A6' },
  { name: 'Fase A', value: 141, color: '#83C5B1' },
  { name: 'Fase B', value: 130, color: '#83C5B1' },
  { name: 'Fase C', value: 128, color: '#83C5B1' },
];

const renderCustomLabel = ({ x, y, width, value }) => (
  <Text x={x + width / 2} y={y} fill="#69B2A6" textAnchor="middle" dy={-10} fontSize={20}>
    {value}
  </Text>
);

const VoltageLN = () => {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <BarChart data={data} margin={{ top: 20, right: 30, left: 30, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
        <XAxis dataKey="name" tick={{ fill: '#ccc', fontSize: 18 }} />
        <YAxis tick={{ fill: '#ccc', fontSize: 18 }} domain={[0, 200]} />
        <Tooltip />
        <Bar dataKey="value" fill="#8884d8">
          {data.map((entry, index) => (
            <Bar key={`bar-${index}`} fill={entry.color} />
          ))}
          {data.map((entry, index) => (
            <text key={`label-${index}`} x={entry.x} y={entry.y} dy={-10} fontSize={18} fill={entry.color}>
              {entry.value}
            </text>
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
};

export default VoltageLN;