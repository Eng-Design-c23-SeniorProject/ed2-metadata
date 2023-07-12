import React from 'react';
import axios from 'axios';

class UploadImg extends React.Component {
  handleFileUpload = async (event) => {
    event.preventDefault();
    const fileInput = event.target.image.files[0];

    const formData = new FormData();
    formData.append('image', fileInput);

    try {
      const response = await axios.post('http://localhost:5000/upload-image', formData);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  render() {
    return (
      <div>
        <h1>Upload an Image</h1>
        <form onSubmit={this.handleFileUpload}>
          <input type="file" name="image" />
          <button type="submit">Upload</button>
        </form>
      </div>
    );
  }
}

export default UploadImg;
