import React from 'react';
import Chart from './Chart';
import '../styling/Modal.css';

function Modal({ onClose, data }) {
  return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={onClose}>&times;</span>
        <h2>Document Similarity Analysis</h2>
        <Chart data={data} />
      </div>
    </div>
  );
}

export default Modal;
