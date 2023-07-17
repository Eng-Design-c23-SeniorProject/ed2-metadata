import React, { useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

const SearchImg = () => {
  const [query, setQuery] = useState('');
  const [result, setResult] = useState([]);
  const navigate = useNavigate();

  const handleFormSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post('http://localhost:5000/search-image', { query });
      setResult(response.data.result);
    } catch (error) {
      console.error(error);
    }
  };

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  const handleImageClick = (id) => {
    navigate(`/DisplayImg/${id}`);
  };

  return (
    <div>
      <h1>Search Images</h1>

      <form onSubmit={handleFormSubmit}>
        <input
          type="text"
          name="query"
          value={query}
          onChange={handleInputChange}
          placeholder="Search an image"
          required
        />
        <button type="submit">Search</button>
      </form>

      {result.length > 0 ? (
        <div>
          <h2>Images found:</h2>
          <ul>
            {result.map((image) => (
              <li key={image._id}>
                <Link to={`/DisplayImg/${image._id}`} onClick={() => handleImageClick(image._id)}>
                  {image.name}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <p>No images found.</p>
      )}
    </div>
  );
};

export default SearchImg;