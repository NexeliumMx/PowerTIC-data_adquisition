import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Filled', value: 75 },
  { name: 'Unfilled', value: 25 },
];

const COLORS = ['#69B2A6', '#F2A007'];

export default function CustomPieChart() {
  return (
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <ResponsiveContainer width={300} height={200}>
        <PieChart>
          <Pie
            data={data}
            innerRadius={60}
            outerRadius={80}
            paddingAngle={5}
            dataKey="value"
            startAngle={90}
            endAngle={-270}
          >
            {data.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
        </PieChart>
      </ResponsiveContainer>
      <div
        style={{
          marginLeft: '-60px',
          padding: '10px',
          borderRadius: '10px',
          backgroundColor: 'rgba(105, 178, 166, 0.1)',
          border: '2px solid #69B2A6',
          fontSize: '2rem',
          color: 'white',
        }}
      >
        0.75
      </div>
    </div>
  );
}