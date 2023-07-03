import React from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import '../App.css';
import UploadPDF from './UploadPDF';
import Search from './Search';
import Display from './Display';

const BodyContent = () => {
  return (
    <div className="body">
      <div className="grid1">
        <ul>
            <li><h3>Upload</h3></li>
            <li><Link to="/uploadPDF">PDF</Link></li>
            <li><Link to="/">Docs</Link></li>
            <li><Link to="/">Txt</Link></li>
            <li><Link to="/">Image</Link></li>
            <li><Link to="/">Video</Link></li>
            <li><h3>Dashboard</h3></li>
            <li><Link to="/">View Dashboard</Link></li>
            <li><h3>Grammar</h3></li>
            <li><Link to="/">Grammar Check</Link></li>
        </ul>
      </div>
      <div className="grid2">
        <Routes>
          <Route path="/uploadPDF" element={<UploadPDF />} />
          <Route path="/search" element={<Search />} />
          <Route path="/display/:id" element={<Display />} />
        </Routes>
      </div>
    </div>
  );
};

export default BodyContent;