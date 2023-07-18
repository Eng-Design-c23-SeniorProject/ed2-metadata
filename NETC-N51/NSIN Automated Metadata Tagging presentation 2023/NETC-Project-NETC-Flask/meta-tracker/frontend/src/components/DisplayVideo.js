import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const DisplayVideo = () => {
  const [videoUrl, setVideoUrl] = useState('');
  const { id } = useParams();

  useEffect(() => {
    const fetchVideo = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/display-video/${id}`, {
          responseType: 'blob',
        });

        //creating an object URL for the video blob
        const videoBlob = new Blob([response.data], { type: 'video/mp4' });
        const videoUrl = URL.createObjectURL(videoBlob);
        setVideoUrl(videoUrl);
      } catch (error) {
        console.error('Error displaying video:', error);
      }
    };

    fetchVideo();
  }, [id]);

  return (
    <div>
      <h1>Video Display</h1>

      {videoUrl && (
        <div>
          <h2>Video Content:</h2>
          <video controls src={videoUrl} width="50%" height="auto" />
        </div>
      )}
    </div>
  );
};

export default DisplayVideo;