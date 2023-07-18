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
import DisplayText from './DisplayText';
import SearchVideo from './SearchVideo';
import DisplayVideo from './DisplayVideo';
import UploadVideo from './UploadVideo';
import UploadDocs from './UploadDocs';
import SearchDocs from './SearchDocs';
import DisplayDocs from './DisplayDocs';

const BodyContent = () => {
  return (
    <div className="body">
      <div className="grid1">
        <ul>
            <li><h3>Upload</h3></li>
            <li><Link to="/UploadPDF">PDF</Link></li>
            <li><Link to="/UploadImg">Image</Link></li>
            <li><Link to="/UploadText">Txt</Link></li>
            <li><Link to="/UploadVideo">Video</Link></li>
            <li><Link to="/UploadDocs">Docx</Link></li>
            <li><h3>Dashboard</h3></li>
            <li><Link to="/">View Dashboard</Link></li>
            <li><h3>User Display</h3></li>
            <li><Link to="/">User Display</Link></li>
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
          <Route path="/DisplayText/:id" element={<DisplayText />} />
          <Route path="/SearchVideo" element={<SearchVideo />} />
          <Route path="/UploadVideo" element={<UploadVideo />} />
          <Route path="/DisplayVideo/:id" element={<DisplayVideo />} />
          <Route path="/UploadDocs" element={<UploadDocs />} />
          <Route path="/SearchDocs" element={<SearchDocs />} />
          <Route path="/DisplayDocs/:id" element={<DisplayDocs />} />
        </Routes>
      </div>
    </div>
  );
};

export default BodyContent;