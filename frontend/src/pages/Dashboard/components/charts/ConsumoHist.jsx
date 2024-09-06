import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

// Datos ejemplo para 60 minutos con intervalos de 5 minutos
const data = [
  { name: '0 min', kw: 10, kvar: 8 },
  { name: '5 min', kw: 20, kvar: 18 },
  { name: '10 min', kw: 30, kvar: 25 },
  { name: '15 min', kw: 22, kvar: 15 },
  { name: '20 min', kw: 28, kvar: 20 },
  { name: '25 min', kw: 35, kvar: 22 },
  { name: '30 min', kw: 40, kvar: 32 },
  { name: '35 min', kw: 50, kvar: 40 },
  { name: '40 min', kw: 42, kvar: 38 },
  { name: '45 min', kw: 48, kvar: 44 },
  { name: '50 min', kw: 55, kvar: 48 },
  { name: '55 min', kw: 52, kvar: 50 },
  { name: '60 min', kw: 60, kvar: 55 }
];

const VoltageLL = () => {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <BarChart data={data} margin={{ top: 20, right: 30, left: 30, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
        {/* Usamos reversed en el XAxis para que el valor más reciente (60 min) aparezca a la derecha */}
        <XAxis dataKey="name" tick={{ fill: '#ccc', fontSize: 18 }} reversed={true} />
        <YAxis tick={{ fill: '#ccc', fontSize: 18 }} />
        <Tooltip />
        <Legend />
        {/* Se agregan dos barras, una para KW/h y otra para KVAr/h con colores diferentes */}
        <Bar dataKey="kw" fill="#69B2A6" name="KW/h" />
        <Bar dataKey="kvar" fill="#FFBB28" name="KVAr/h" />
      </BarChart>
    </ResponsiveContainer>
  );
};

export default VoltageLL;

