import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { Document, Page } from 'react-pdf';

const Display = () => {
  const [text_content, setPdfData] = useState('');
  const [summary, setSummary] = useState('');
  const { id } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/display/${id}`);
        setPdfData(response.data.text_content);
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

      {text_content && (
        <div>
          <h2>PDF Content:</h2>
          <Document file={text_content}>
            <Page pageNumber={1} />
          </Document>
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

export default Display;