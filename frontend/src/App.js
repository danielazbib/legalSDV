import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Doughnut } from 'react-chartjs-2';
import Modal from './components/Modal';
import './styling/App.css';
import logo from './assets/logo.png';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
ChartJS.register(ArcElement, Tooltip, Legend);

function App() {
  const [similarityData, setSimilarityData] = useState(null);
  const [selectedDoc, setSelectedDoc] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios.get("http://127.0.0.1:5000/api/similarity");
      setSimilarityData(response.data);
    };
    fetchData();
  }, []);

  const handleDocChange = (event) => {
    setSelectedDoc(event.target.value);
  };

  const avgSimilarityChartData = {
    datasets: [
      {
        data: [similarityData?.avg_similarity * 100, 100 - similarityData?.avg_similarity * 100],
        backgroundColor: ['#36A2EB', '#E5E5E5'],
        borderWidth: 1,
      },
    ],
    labels: ['Semantic Accuracy', ''],
  };

  return (
    <div className="App">
      <div className="header">
        <img src={logo} alt="SimpliSafe Logo" className="logo" />
        <h1>Welcome to SimpliSafe</h1>
        <p>View the application of our software to the <a href="https://github.com/neelguha/legal-ml-datasets?tab=readme-ov-file#cuad-an-expert-annotated-nlp-dataset-for-legal-contract-review" target="_blank" rel="noopener noreferrer">Contract Understanding Atticus Dataset (CUAD)</a>, a <a href="https://github.com/TheAtticusProject/cuad/blob/main/data.zip" target="_blank" rel="noopener noreferrer">dataset on 510 legal contracts</a>. Select a document to view the side-by-side comparison of its original description and our SimpliSafe synthesized description. Check the accuracy for that document with its individual semantic similarity analysis.</p>
      </div>


      <select onChange={handleDocChange} value={selectedDoc} className="dropdown">
            <option value="">Select Document</option>
            {similarityData.documents.map((title, index) => (
              <option key={index} value={index}>{title}</option>
            ))}
          </select>

          {selectedDoc !== null && (
            <Modal 
              title={similarityData.documents[selectedDoc]}
              originalText={similarityData.original_descriptions[selectedDoc]} 
              modifiedText={similarityData.modified_descriptions[selectedDoc]} 
              similarityScore={similarityData.similarity_scores[selectedDoc]}
              onClose={() => setSelectedDoc(null)} 
            />
          )}
      
      {similarityData && (
        <div className="content">
          <div className="chart-container">
            <h2>Overall Semantic Accuracy: {(similarityData.avg_similarity * 100).toFixed(2)}%</h2>
            <Doughnut data={avgSimilarityChartData} className='overall-doughnut' />
          </div>

        </div>
      )}
    </div>
  );
}

export default App;
