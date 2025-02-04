// src/components/UserList.js
import React, { useState, useEffect } from 'react';
import { getUsers } from '../services/userService';

const UserList = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    // Cargar los usuarios desde el backend
    getUsers().then(response => {
      setUsers(response.data);  // Suponemos que la respuesta es un array de usuarios
    }).catch(error => {
      console.error('Error fetching users:', error);
    });
  }, []);

  return (
    <div>
      <h2>Lista de Usuarios</h2>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name} - {user.email}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;
