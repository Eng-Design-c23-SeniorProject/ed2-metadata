import React from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import '../App.css';
import UploadPDF from './UploadPDF';
import SearchPDF from './SearchPDF';
import DisplayPDF from './DisplayPDF';
import UploadImg from './UploadImg';
import SearchImg from './SearchImg';
import DisplayImg from './DisplayImg';

import UploadText from './UploadText';
import SearchText from './SearchText';
import SearchVideo from './SearchVideo';
import DisplayText from './DisplayText';
import DisplayVideo from './DisplayVideo';
import UploadVideo from './UploadVideo';



const BodyContent = () => {
  return (
    <div className="body">
      <div className="grid1">
        <ul>
            <li><h3>Upload</h3></li>
            <li><Link to="/UploadPDF">PDF</Link></li>
            <li><Link to="/UploadDocs">Docs</Link></li>
            <li><Link to="/UploadText">Txt</Link></li>
            <li><Link to="/UploadImg">Image</Link></li>
            <li><Link to="/UploadVideo">Video</Link></li>
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
          <Route path="/SearchImg" element={<SearchImg />} />
          <Route path="/DisplayImg/:id" element={<DisplayImg />} />

          <Route path="/UploadText" element={<UploadText />} />
          <Route path="/SearchText" element={<SearchText />} />
          <Route path="/SearchVideo" element={<SearchVideo />} />
          <Route path="/DisplayText/:id" element={<DisplayText />} />
          <Route path="/UploadVideo" element={<UploadVideo />} />
          <Route path="/DisplayVideo/:id" element={<DisplayVideo />} />

          

        </Routes>
      </div>
    </div>
  );
};

export default BodyContent;