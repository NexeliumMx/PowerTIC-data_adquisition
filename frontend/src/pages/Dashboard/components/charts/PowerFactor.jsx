import { PieChart, Pie, Cell } from 'recharts';

export default function PowerFactor({ data, colors, powerFactor }) {
  return (
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <div style={{ width: '300px', height: '200px' }}>
        <PieChart width={300} height={200}>
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
              <Cell key={`cell-${index}`} fill={colors[index % colors.length]} />
            ))}
          </Pie>
        </PieChart>
      </div>

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
        {powerFactor} {/* Dynamically display the power factor */}
      </div>
    </div>
  );
}