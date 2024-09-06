import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend } from 'recharts';

// Nuevo conjunto de datos para 60 minutos en intervalos de 5 minutos
const data = [
  { name: '0 min', promedio: 2.1, faseA: 2.4, faseB: 1.9, faseC: 2.0 },
  { name: '5 min', promedio: 2.6, faseA: 2.9, faseB: 2.3, faseC: 2.5 },
  { name: '10 min', promedio: 2.8, faseA: 3.1, faseB: 2.5, faseC: 2.7 },
  { name: '15 min', promedio: 3.2, faseA: 3.5, faseB: 2.9, faseC: 3.1 },
  { name: '20 min', promedio: 3.8, faseA: 4.0, faseB: 3.5, faseC: 3.7 },
  { name: '25 min', promedio: 4.1, faseA: 4.3, faseB: 3.8, faseC: 4.0 },
  { name: '30 min', promedio: 3.6, faseA: 3.8, faseB: 3.3, faseC: 3.5 },
  { name: '35 min', promedio: 3.9, faseA: 4.1, faseB: 3.6, faseC: 3.8 },
  { name: '40 min', promedio: 4.3, faseA: 4.6, faseB: 4.0, faseC: 4.3 },
  { name: '45 min', promedio: 4.0, faseA: 4.3, faseB: 3.7, faseC: 4.1 },
  { name: '50 min', promedio: 3.5, faseA: 3.7, faseB: 3.2, faseC: 3.6 },
  { name: '55 min', promedio: 3.2, faseA: 3.4, faseB: 2.9, faseC: 3.3 },
  { name: '60 min', promedio: 4.5, faseA: 4.8, faseB: 4.2, faseC: 4.5 }
];

const ReactivePower = () => {
  return (
    <div>
      <h2 style={{ textAlign: 'center', color: '#69B2A6', marginBottom: '20px' }}>Potencia Reactiva</h2>
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

export default ReactivePower;
