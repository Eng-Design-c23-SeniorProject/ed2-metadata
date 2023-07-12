import React from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import '../App.css';
import UploadPDF from './UploadPDF';
import SearchPDF from './SearchPDF';
import DisplayPDF from './DisplayPDF';
import UploadImg from './UploadImg';

const BodyContent = () => {
  return (
    <div className="body">
      <div className="grid1">
        <ul>
            <li><h3>Upload</h3></li>
            <li><Link to="/UploadPDF">PDF</Link></li>
            <li><Link to="/">Docs</Link></li>
            <li><Link to="/">Txt</Link></li>
            <li><Link to="/UploadImg">Image</Link></li>
            <li><Link to="/">Video</Link></li>
            <li><h3>Dashboard</h3></li>
            <li><Link to="/">View Dashboard</Link></li>
            <li><h3>Grammar</h3></li>
            <li><Link to="/">Grammar Check</Link></li>
        </ul>
      </div>
      <div className="grid2">
        <Routes>
          <Route path="/UploadPDF" element={<UploadPDF />} />
          <Route path="/SearchPDF" element={<SearchPDF />} />
          <Route path="/DisplayPDF/:id" element={<DisplayPDF />} />
          <Route path="/UploadImg" element={<UploadImg />} />
        </Routes>
      </div>
    </div>
  );
};

export default BodyContent;