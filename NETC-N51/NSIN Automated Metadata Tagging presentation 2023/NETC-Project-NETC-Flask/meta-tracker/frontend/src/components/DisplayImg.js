import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const DisplayImg = () => {
  const [imageUrl, setImageUrl] = useState('');
  const { id } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/display-image/${id}`, {
          responseType: 'blob',
        });
    
        const reader = new FileReader();
    
        reader.onloadend = () => {
          setImageUrl(reader.result);
        };
    
        reader.readAsDataURL(response.data);
      } catch (error) {
        console.error(error);
      }
    };
    

    fetchData();
  }, [id]);

  return (
    <div>
      <h1>Image Display after search</h1>

      {imageUrl && (
        <div>
          <h2>Image:</h2>
          <img src={imageUrl} alt="search display placeholder" style={{ width: '50%', height: 'auto' }} />
        </div>
      )}
    </div>
  );
};

export default DisplayImg;