// /src/components/HandleLogoDarkLightMode.jsx
import { useState, useEffect } from 'react';

function handleLogoDarkLightMode() {
  const [isDarkMode, setIsDarkMode] = useState(false);

  useEffect(() => {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    setIsDarkMode(mediaQuery.matches);

    const handleChange = (e) => setIsDarkMode(e.matches);
    mediaQuery.addListener(handleChange);
    return () => mediaQuery.removeListener(handleChange);
  }, []);

  return (
    <a href="https://vitejs.dev" target="_blank">
      <img
        src={isDarkMode ? '/volt-circle-dark.svg' : '/bolt-circle-light.svg'}
        className="logo"
        alt="PowerTIC logo"
      />
    </a>
  );
}

export default handleLogoDarkLightMode;