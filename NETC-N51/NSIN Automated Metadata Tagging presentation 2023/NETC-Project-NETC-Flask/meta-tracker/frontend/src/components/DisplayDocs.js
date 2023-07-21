import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import FileViewer from 'react-file-viewer'

const DisplayDocs = () => {
  const [docURL, setDocURL] = useState(null);
  const [summary, setSummary] = useState('');
  const { id } = useParams();
  const file = {
    url: docURL,
    type: 'docx',
  }


  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/display-doc/${id}`);
        setDocURL(`data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,${response.data.docData}`);
        setSummary(response.data.summary);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, [id]);


  return (
    <div>
      <h1>DOC Display</h1>

      {docURL ? (
        <div>
          <h2>DOC Content:</h2>
          {}
          <FileViewer fileType={file.type} filePath={file.url} />
          
        </div>
      ) : (
        <p>Loading...</p>
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

export default DisplayDocs;