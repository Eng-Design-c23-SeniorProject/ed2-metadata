import React from 'react';
import axios from 'axios';

class UploadDocs extends React.Component {
  state = {
    message: '',
  };

  handleFileUpload = async (event) => {
    event.preventDefault();
    const fileInput = event.target.file.files[0];

    const formData = new FormData();
    formData.append('file', fileInput);

    try {
      const response = await axios.post('http://localhost:5000/upload-doc', formData);
      this.setState({ message: response.data });

      // Refresh the page after 2 seconds
      setTimeout(() => {
        window.location.reload();
      }, 2000);
    } catch (error) {
      console.error(error);
      this.setState({ message: 'Upload failed.' });

      // Refresh the page after 2 seconds
      setTimeout(() => {
        window.location.reload();
      }, 2000);
    }
  };

  render() {
    const { message } = this.state;

    return (
      <div>
        <h1>Upload a Docx</h1>
        <form onSubmit={this.handleFileUpload}>
          <input type="file" name="file" />
          <button type="submit">Upload</button>
        </form>
        {message && <p>{message}</p>}
      </div>
    );
  }
}

export default UploadDocs;