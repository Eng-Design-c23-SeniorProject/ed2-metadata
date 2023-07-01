import React from 'react';
import { Link } from 'react-router-dom';
import '../App.css';

const Footer = () => {
  return (
    <div className="footer">
      {/* Footer content */}
        <p><b>Footer</b></p>
        <p><Link to="/">About</Link></p>
    </div>
  );
};

export default Footer;