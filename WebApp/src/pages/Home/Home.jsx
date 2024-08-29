import { useNavigate } from 'react-router-dom';
import './Home.scss';  // Import the Home-specific styles

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className='home-container'>
      <button onClick={() => navigate('/dashboard')} style={{ margin: '10px', padding: '10px 20px', cursor: 'pointer' }}>
        Go to Dashboard
      </button>
      <button onClick={() => navigate('/downloads')} style={{ margin: '10px', padding: '10px 20px', cursor: 'pointer' }}>
        Go to Downloads
      </button>
      <button onClick={() => navigate('/testpage')} style={{ margin: '10px', padding: '10px 20px', cursor: 'pointer' }}>
        Go to Test Page
      </button>
      <button onClick={() => navigate('/nonexistent')} style={{ margin: '10px', padding: '10px 20px', cursor: 'pointer' }}>
        Go to NotFound
      </button>
    </div>
  );
}