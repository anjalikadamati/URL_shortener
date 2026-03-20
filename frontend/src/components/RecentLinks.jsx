import { useState } from 'react';

function RecentLinks({ links }) {
  const [toast, setToast] = useState('');

  const showToast = (msg) => {
    setToast(msg);
    setTimeout(() => setToast(''), 2000);
  };

  const copyLink = (url) => {
    navigator.clipboard.writeText(url);
    showToast('Copied!');
  };

  const visitLink = (url) => {
    window.open(url, '_blank');
  };

  if (links.length === 0) {
    return (
      <div className="recent">
        <h2>Recent Links</h2>
        <p>No links yet. Create some!</p>
      </div>
    );
  }

  return (
    <>
      <div className="recent">
        <h2>Recent Links</h2>

        {links.map((item) => (
          <div className="recent-card" key={item.short}>
            <div className="short-url">
              <a href={item.short} target="_blank" rel="noopener noreferrer">
                {item.short}
              </a>
            </div>

            <p className="original" title={item.original}>
              {item.original.length > 60
                ? item.original.slice(0, 60) + '...'
                : item.original}
            </p>

            <span className="clicks">
              {item.clicks || 0} clicks
            </span>

            <div className="buttons">
              <button className='visit-btn' onClick={() => visitLink(item.short)}>
                Visit
              </button>
              <button className='copy-btn' onClick={() => copyLink(item.short)}>
                Copy
              </button>
            </div>
          </div>
        ))}
      </div>

      {toast && <div className="toast show">{toast}</div>}
    </>
  );
}

export default RecentLinks;