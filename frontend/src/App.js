import React, { useState } from 'react';
import axios from 'axios';
import Modal from './components/Modal';
import './styling/App.css';
import logo from './assets/logo-transparent.png';

function App() {
  const [modalOpen, setModalOpen] = useState(false);
  const [similarityData, setSimilarityData] = useState(null);

  const fetchData = async () => {
    const response = await axios.get("http://127.0.0.1:5000/api/similarity");
    console.log(response);
    setSimilarityData(response.data);
    setModalOpen(true);
  };

  return (
    <div className="App">
      <div className="center">
        <img src={logo} />
        <button onClick={fetchData}>Open Analysis</button>
        {modalOpen && similarityData && (
          <Modal onClose={() => setModalOpen(false)} data={similarityData} />
        )}
      </div>
    </div>
  );
}

export default App;
