import React from 'react';
import axios from 'axios';

class UploadVideo extends React.Component {
  handleFileUpload = async (event) => {
    event.preventDefault();
    const fileInput = event.target.video.files[0];

    const formData = new FormData();
    formData.append('video', fileInput);

    try {
      const response = await axios.post('http://localhost:5000/upload-video', formData);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  render() {
    return (
      <div>
        <h1>Upload a Video</h1>
        <form onSubmit={this.handleFileUpload}>
          <input type="file" name="video" accept="video/*" />
          <button type="submit">Upload</button>
        </form>
      </div>
    );
  }
}

export default UploadVideo;