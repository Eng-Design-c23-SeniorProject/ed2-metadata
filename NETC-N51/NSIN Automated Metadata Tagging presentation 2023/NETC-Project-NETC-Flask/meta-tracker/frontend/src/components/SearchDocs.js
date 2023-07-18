import React, { useState } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';

const SearchDocs = () => {
  const [query, setQuery] = useState('');
  const [result, setResult] = useState([]);
  const navigate = useNavigate();

  const handleFormSubmit = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post('http://localhost:5000/search-doc', { query });
      setResult(response.data.result);
    } catch (error) {
      console.error(error);
    }
  };

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  const handleFileClick = (id) => {
    navigate(`/DisplayDocs/${id}`);
  };

  return (
    <div>
      <h1>Search Files</h1>

      <form onSubmit={handleFormSubmit}>
        <input
          type="text"
          name="query"
          value={query}
          onChange={handleInputChange}
          placeholder="Search a file"
          required
        />
        <button type="submit">Search</button>
      </form>

      {result.length > 0 ? (
        <div>
          <h2>Documents found:</h2>
          <ul>
            {result.map((document) => (
              <li key={document._id}>
                <Link to={`/DisplayDocs/${document._id}`} onClick={() => handleFileClick(document._id)}>
                  {document.name}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <p>No documents found.</p>
      )}
    </div>
  );
};

export default SearchDocs;