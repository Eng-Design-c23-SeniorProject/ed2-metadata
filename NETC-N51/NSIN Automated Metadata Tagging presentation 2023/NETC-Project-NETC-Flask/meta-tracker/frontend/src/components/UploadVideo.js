import React from 'react';
import axios from 'axios';

class UploadVideo extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      uploadMessage: '',
    };
  }

  handleFileUpload = async (event) => {
    event.preventDefault();
    const fileInput = event.target.video.files[0];

    const formData = new FormData();
    formData.append('video', fileInput);

    try {
      const response = await axios.post('http://localhost:5000/upload-video', formData);
      console.log(response.data);

      //the state to display the message
      this.setState({ uploadMessage: response.data });

      //refresh the page after 2 seconds, only if the response is not a duplicate
      if (response.data !== 'File is a duplicate. Upload skipped.') {
        setTimeout(() => {
          window.location.reload();
        }, 2000);
      }
    } catch (error) {
      console.error(error);
      this.setState({ uploadMessage: 'Upload failed.' });

      //refresh the page after 2 seconds
      setTimeout(() => {
        window.location.reload();
      }, 2000);
    }
  };

  render() {
    const { uploadMessage } = this.state;

    return (
      <div>
        <h1>Upload a Video</h1>
        <form onSubmit={this.handleFileUpload}>
          <input type="file" name="video" accept="video/*" />
          <button type="submit">Upload</button>
        </form>
        {/* Display the upload message */}
        {uploadMessage && <p>{uploadMessage}</p>}
      </div>
    );
  }
}

export default UploadVideo;