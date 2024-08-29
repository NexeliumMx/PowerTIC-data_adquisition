import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Ene', value: 57000 },
  { name: 'Feb', value: 74779 },
  { name: 'Mar', value: 19027 },
  { name: 'Abr', value: 43887 },
  { name: 'May', value: 22000 },
  { name: 'Jun', value: 67000 },
  { name: 'Jul', value: 78200 },
  { name: 'Ago', value: 51286 },
  { name: 'Sept', value: 40200 },
  { name: 'Oct', value: 58736 },
  { name: 'Nov', value: 68739 },
  { name: 'Dic', value: 62000 },
];

export default function CustomBarChart () {
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