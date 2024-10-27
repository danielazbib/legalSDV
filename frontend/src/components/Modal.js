import React from 'react';
import { Doughnut } from 'react-chartjs-2';
import '../styling/Modal.css';

const Modal = ({ title, originalText, modifiedText, similarityScore, onClose, onCopy }) => {
  const similarityChartData = {
    datasets: [
      {
        data: [similarityScore * 100, 100 - similarityScore * 100],
        backgroundColor: ['#36A2EB', '#E5E5E5'],
        borderWidth: 1,
      },
    ],
    labels: ['Semantic Similarity', ''],
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="close-btn" onClick={onClose}>✕</button>
        <h2 className="modal-title">{title}</h2>

        <div className="text-display">
          <div className="text-container">
            <div>
              <h3 className='original-title'>Original Text</h3>
              <div className="text-box">
                <p>{originalText}</p>
              </div>
            </div>

            <div>
              <div className="modified-copy">
                <h3>Modified Text</h3>
                <button onClick={onCopy} className="copy-btn">Copy</button>
              </div>
              <div className="text-box">
                <p>{modifiedText}</p>
              </div>
            </div>
          </div>
        </div>

        <div>
          <p className="doc-score">The semantics of the two texts are {(similarityScore * 100).toFixed(2)}% similar to eachother.</p>
        </div>
      </div>
    </div>
  );
};

export default Modal;
