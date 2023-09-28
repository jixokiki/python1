import React, { useState } from 'react';
import axios from 'axios';

const Form = () => {
  const [formData, setFormData] = useState({
    name: '',
    address: '',
    note: '',
    email: ''
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('/submit', formData) // Replace with your backend URL
      .then(response => {
        console.log('Form submitted successfully!');
        // Reset the form
        setFormData({
          name: '',
          address: '',
          note: '',
          email: ''
        });
      })
      .catch(error => {
        console.error('Error submitting form:', error);
      });
  };

  return (
    <div>
      <h2>Submit Form</h2>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input type="text" name="name" value={formData.name} onChange={handleChange} required />

        <label>Address:</label>
        <input type="text" name="address" value={formData.address} onChange={handleChange} required />

        <label>Note or Purpose:</label>
        <textarea name="note" value={formData.note} onChange={handleChange}></textarea>

        <label>Email:</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} required />

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default Form;
