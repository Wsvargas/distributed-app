// src/components/UserForm.js
import React, { useState } from 'react';
import { createUser } from '../services/userService';

const UserForm = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const userData = { name, email };

    createUser(userData).then(response => {
      console.log('Usuario creado:', response.data);
      setName('');
      setEmail('');
    }).catch(error => {
      console.error('Error creating user:', error);
    });
  };

  return (
    <div>
      <h2>Crear Usuario</h2>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <label>Email:</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <button type="submit">Crear Usuario</button>
      </form>
    </div>
  );
};

export default UserForm;
