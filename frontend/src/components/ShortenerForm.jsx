import { useState } from 'react';

function ShortenerForm({ onShorten }) {
  const [url, setUrl] = useState('');
  const [shortUrl, setShortUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
    setError('');

    if (!url.trim()) {
      setError('Please enter a URL');
      return;
    }
    try {
      new URL(url);
    } catch {
      setError('Invalid URL');
      return;
    }

    setLoading(true);
    setShortUrl('');

    try {
      const res = await fetch('/shorten', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: url.trim() })
      });

      if (!res.ok) throw new Error('Failed to shorten URL');

      const data = await res.json();

      onShorten({
        original: url,
        short: data.short_url,
        clicks: 0
      });

      setShortUrl(data.short_url);
      setUrl('');

    } catch {
      setError('Server error. Try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <input
        type="url"
        placeholder="Paste a long URL here..."
        value={url}
        onChange={(e) => {
          setUrl(e.target.value);
          setError('');
        }}
        disabled={loading}
      />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? 'Shortening...' : 'Shorten Link'}
      </button>

      {error && <div className="error">{error}</div>}

      {shortUrl && (
        <div className="result">
          <p>Your short link:</p>
          <a href={shortUrl} target="_blank">
            {shortUrl}
          </a>
        </div>
      )}
    </div>
  );
}

export default ShortenerForm;