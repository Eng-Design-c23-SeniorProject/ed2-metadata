import React from 'react';
import { Link } from 'react-router-dom';
import '../App.css';

const Navbar = () => {
  return (
    <div className="navbar">
      <div className="title">
        <Link to="/">MetaTracker</Link>
      </div>
      <form className="search-form">
        <input type="text" placeholder="Search..." />
        <button className="search-button"type="submit">Search</button>
      </form>
    </div>
  );
};

export default Navbar;