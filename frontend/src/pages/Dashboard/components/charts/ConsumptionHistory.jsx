import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Ene', value: 0 },
  { name: 'Feb', value: 0 },
  { name: 'Mar', value: 0 },
  { name: 'Abr', value: 0 },
  { name: 'May', value: 0 },
  { name: 'Jun', value: 0 },
  { name: 'Jul', value: 0 },
  { name: 'Ago', value: 0 },
  { name: 'Sept', value: 0 },
  { name: 'Oct', value: 0 },
  { name: 'Nov', value: 0 },
  { name: 'Dic', value: 0 },
];

export default function ConsumptionHistory () {
  return (
    <ResponsiveContainer width="100%" height={500}>
      <BarChart data={data} layout="vertical" margin={{ top: 20, right: 50, left: 50, bottom: 20 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis type="number" />
        <YAxis type="category" dataKey="name" />
        <Tooltip />
        <Bar dataKey="value" fill="#69B2A6" />
      </BarChart>
    </ResponsiveContainer>
  );
};