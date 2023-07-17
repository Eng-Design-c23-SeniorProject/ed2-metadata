import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const DisplayText = () => {
  const [textUrl, settextUrl] = useState('');
  const [summary, setSummary] = useState('');
  const { id } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/display-text/${id}`);
        settextUrl(`data:text/plain;base64,${response.data.textData}`);
        setSummary(response.data.summary);
      } catch (error) {
        console.error(error);
      }
    };

    fetchData();
  }, [id]);

  return (
    <div>
      <h1>Text Display</h1>

      {textUrl && (
        <div>
          <h2>Text Content:</h2>
          <embed src={textUrl} type="text/plain" width="50%" height="500px" />
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

export default DisplayText;