import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

// Datos de ejemplo para 60 minutos en intervalos de 5 minutos
const data = [
  { name: '0 min', promedio: 4.8, faseA: 5.0, faseB: 4.6, faseC: 5.2 },
  { name: '5 min', promedio: 5.1, faseA: 5.3, faseB: 5.0, faseC: 5.4 },
  { name: '10 min', promedio: 5.4, faseA: 5.6, faseB: 5.1, faseC: 5.5 },
  { name: '15 min', promedio: 6.2, faseA: 6.5, faseB: 6.0, faseC: 6.3 },
  { name: '20 min', promedio: 7.1, faseA: 7.5, faseB: 6.8, faseC: 7.0 },
  { name: '25 min', promedio: 6.8, faseA: 7.2, faseB: 6.5, faseC: 6.9 },
  { name: '30 min', promedio: 5.9, faseA: 6.1, faseB: 5.7, faseC: 6.0 },
  { name: '35 min', promedio: 6.4, faseA: 6.7, faseB: 6.0, faseC: 6.6 },
  { name: '40 min', promedio: 7.3, faseA: 7.6, faseB: 7.0, faseC: 7.5 },
  { name: '45 min', promedio: 6.8, faseA: 7.0, faseB: 6.5, faseC: 6.9 },
  { name: '50 min', promedio: 5.6, faseA: 5.8, faseB: 5.3, faseC: 5.9 },
  { name: '55 min', promedio: 5.2, faseA: 5.4, faseB: 5.0, faseC: 5.5 },
  { name: '60 min', promedio: 6.5, faseA: 6.7, faseB: 6.3, faseC: 6.6 }
];

const RealPower = () => {
  return (
    <div>
      <h2 style={{ textAlign: 'center', color: '#69B2A6', marginBottom: '20px' }}>Potencia Real</h2>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={data} margin={{ top: 0, right: 30, left: 30, bottom: 0 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
          <XAxis dataKey="name" tick={{ fill: '#ccc', fontSize: 18 }} reversed={true}/>
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

export default RealPower;
