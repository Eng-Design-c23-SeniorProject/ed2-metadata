import React from 'react';
import axios from 'axios';

class UploadPDF extends React.Component {
  handleFileUpload = async (event) => {
    event.preventDefault();
    const fileInput = event.target.file.files[0];

    const formData = new FormData();
    formData.append('file', fileInput);

    try {
      const response = await axios.post('http://localhost:5000/upload', formData);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  render() {
    return (
      <div>
        <h1>Upload a PDF</h1>
        <form onSubmit={this.handleFileUpload}>
          <input type="file" name="file" />
          <button type="submit">Upload</button>
        </form>
      </div>
    );
  }
}

export default UploadPDF;