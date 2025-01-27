import React, { useState } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [count, setCount] = useState(0);

  const handleButtonClick = () => {
    fetch('http://localhost:8000/api/random-message')
      .then(response => response.json())
      .then(data => {
        setMessage(data.message);
        setCount(data.count);
      })
      .catch(error => console.error('Error fetching data:', error));
  };

  return (
    <div>
      <h1>Welcome to My React App!</h1>
      <button onClick={handleButtonClick}>Get Random Message</button>
      <p>Message: {message}</p>
      <p>Count: {count}</p>
    </div>
  );
}

export default App;
