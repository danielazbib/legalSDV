import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from 'react-chartjs-2';

// Register necessary Chart.js components
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function Chart({ data }) {
  const chartData = {
    labels: data.documents,
    datasets: [
      {
        label: 'Original Scores',
        backgroundColor: 'rgba(75,192,192,1)',
        data: data.original_scores,
      },
      {
        label: 'Anonymized Scores',
        backgroundColor: 'rgba(192,75,75,1)',
        data: data.anonymized_scores,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Document Similarity Analysis',
      },
    },
  };

  return <Bar data={chartData} options={options} />;
}

export default Chart;
