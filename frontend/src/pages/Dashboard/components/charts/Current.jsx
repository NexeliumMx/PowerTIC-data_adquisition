import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Text } from 'recharts';

const data = [
  { name: 'Promedio', value: 18.0, color: '#69B2A6' },
  { name: 'Fase A', value: 17.7, color: '#83C5B1' },
  { name: 'Fase B', value: 18.2, color: '#83C5B1' },
  { name: 'Fase C', value: 18.0, color: '#83C5B1' },
  { name: 'Desfase', value: 0.5, color: '#F2A007' },
];

const renderCustomLabel = ({ x, y, width, value }) => (
  <Text x={x + width / 2} y={y} fill={value >= 0.5 ? '#F2A007' : '#69B2A6'} textAnchor="middle" dy={-10} fontSize={18}>
    {value}
  </Text>
);

const Current = () => {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <BarChart data={data} margin={{ top: 20, right: 30, left: 30, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
        <XAxis dataKey="name" tick={{ fill: '#ccc', fontSize: 18 }} />
        <YAxis tick={{ fill: '#ccc', fontSize: 18 }} />
        <Tooltip />
        <Bar dataKey="value" fill="#8884d8">
          {data.map((entry, index) => (
            <Bar key={`bar-${index}`} dataKey="value" fill={entry.color} label={renderCustomLabel} />
          ))}
        </Bar>
      </BarChart>
    </ResponsiveContainer>
  );
};

export default Current;
