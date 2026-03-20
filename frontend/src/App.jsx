import { useState, useEffect } from 'react';
import ShortenerForm from './components/ShortenerForm';
import RecentLinks from './components/RecentLinks';
import './App.css';

function App() {
  const [recentLinks, setRecentLinks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchLinks = async () => {
    try {
      const res = await fetch('/api/recent');
      if (!res.ok) throw new Error(`Server error: ${res.status}`);
      const data = await res.json();
      setRecentLinks(data);
      setError(null);
    } catch (err) {
      console.error('Fetch error:', err);
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLinks();

    const interval = setInterval(() => {
      fetchLinks();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const handleNewLink = () => {
    fetchLinks();
  };

  const handleRefresh = () => {
    setLoading(true);
    fetchLinks();
  };

  return (
    <>
      <div className="navbar">
        <h1>QuickLink</h1>
      </div>

      <div className="container">
        <h1 className="hero-title">Shorten Your Long URLs Instantly</h1>
        <p className="subtitle">Quick, reliable URL shortening for your links</p>

        <ShortenerForm onShorten={handleNewLink} />

        {loading && (
          <div style={{ color: 'white', textAlign: 'center', marginTop: '2rem' }}>
            <div
              className="loading"
              style={{ margin: '0 auto 1rem', width: '40px', height: '40px' }}
            />
            Loading...
          </div>
        )}

        {error && (
          <div
            style={{
              background: '#fee2e2',
              color: '#991b1b',
              padding: '2rem',
              borderRadius: '16px',
              margin: '2rem auto',
              maxWidth: '500px',
              textAlign: 'center'
            }}
          >
            <h3>Load error</h3>
            <p>{error}</p>
            <button
              onClick={handleRefresh}
              style={{
                background: '#3b82f6',
                color: 'white',
                border: 'none',
                padding: '0.5rem 1rem',
                borderRadius: '8px',
                cursor: 'pointer'
              }}
            >
              Refresh
            </button>
          </div>
        )}

        <RecentLinks links={recentLinks} />
      </div>
    </>
  );
}

export default App;