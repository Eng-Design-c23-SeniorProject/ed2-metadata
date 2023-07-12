import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const DisplayPDF = () => {
  const [pdfUrl, setPdfUrl] = useState('');
  const [summary, setSummary] = useState('');
  const { id } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/display-pdf/${id}`);
        setPdfUrl(`data:application/pdf;base64,${response.data.pdfData}`);
        setSummary(response.data.summary);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, [id]);

  return (
    <div>
      <h1>PDF Display</h1>

      {pdfUrl && (
        <div>
          <h2>PDF Content:</h2>
          <embed src={pdfUrl} type="application/pdf" width="50%" height="500px" />
        </div>
      )}

      {summary && (
        <div>
          <h2>Summary:</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
};

export default DisplayPDF;