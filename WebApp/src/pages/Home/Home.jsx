import React from 'react';
import { useNavigate } from 'react-router-dom';

function Home() {
  const navigate = useNavigate();

  return (
    <div style={{ backgroundColor: 'white', height: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
      <h1>Home Page</h1>
      <button onClick={() => navigate('/dashboard')} style={{ margin: '10px', padding: '10px 20px', cursor: 'pointer' }}>
        Go to Dashboard
      </button>
      <button onClick={() => navigate('/nonexistent')} style={{ margin: '10px', padding: '10px 20px', cursor: 'pointer' }}>
        Go to NotFound
      </button>
    </div>
  );
}

export default Home;