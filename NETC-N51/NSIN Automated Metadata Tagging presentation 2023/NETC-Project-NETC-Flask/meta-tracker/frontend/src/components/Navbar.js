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
        <Link to="/SearchAll" className='search-button'>Search</Link>
      </form>
    </div>
  );
};

export default Navbar;