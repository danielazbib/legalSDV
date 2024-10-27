// Notification.js
import React, { useEffect } from 'react';
import '../styling/Notification.css';

const Notification = ({ message, onClose }) => {
  useEffect(() => {
    const timer = setTimeout(onClose, 3000); // Hide after 3 seconds
    return () => clearTimeout(timer);
  }, [onClose]);

  return (
    <div className="notification">
      {message}
    </div>
  );
};

export default Notification;
