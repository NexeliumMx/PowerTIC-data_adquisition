import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

// Datos ejemplo para 60 minutos con intervalos de 5 minutos
const data = [
  { name: '0 min', promedio: 0.95 },
  { name: '5 min', promedio: 0.96 },
  { name: '10 min', promedio: 0.97 },
  { name: '15 min', promedio: 0.98 },
  { name: '20 min', promedio: 0.99 },
  { name: '25 min', promedio: 1.00 },
  { name: '30 min', promedio: 0.98 },
  { name: '35 min', promedio: 0.97 },
  { name: '40 min', promedio: 0.96 },
  { name: '45 min', promedio: 0.95 },
  { name: '50 min', promedio: 0.96 },
  { name: '55 min', promedio: 0.97 },
  { name: '60 min', promedio: 0.98 }
];

const TriPowerFactor = () => {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={data} margin={{ top: 20, right: 30, left: 30, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
        <XAxis dataKey="name" tick={{ fill: '#ccc', fontSize: 18 }} reversed={true}/>
        <YAxis 
          tick={{ fill: '#ccc', fontSize: 18 }} 
          domain={[0.90, 1.0]} // Cambiamos el dominio para que comience en 0.85
          ticks={[0.92, 0.94,0.96,0.98, 1.00]} // Ajustamos los ticks para que comiencen en 0.85
        />
        <Tooltip />
        <Legend />
        {/* Línea solo para el promedio */}
        <Line type="monotone" dataKey="promedio" stroke="#69B2A6" name="Promedio" strokeWidth={2} />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default TriPowerFactor;
