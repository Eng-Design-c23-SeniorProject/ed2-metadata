import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const DisplayDocs = () => {
  const [docContent, setDocContent] = useState(null);
  const [summary, setSummary] = useState('');
  const { id } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/display-doc/${id}`);
        setDocContent({ uri: `data:application/vnd.openxmlformats-officedocument.wordprocessingml.document;base64,${response.data.docData}`, name: 'Document' });
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

      {docContent ? (
        <div>
          <h2>DOC Content:</h2>
          {/* using the embed element to display the document  --need to be fix */}
          <embed
            src={docContent.uri}
            type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            width="70%"
            height="500px"
          />
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