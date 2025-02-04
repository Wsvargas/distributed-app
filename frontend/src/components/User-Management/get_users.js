import React, { useState, useEffect } from "react";
import { getUsers } from "services/User-Management/getUsersService";

const GetUsers = () => {
    const [users, setUsers] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchUsers();
    }, []);

    const fetchUsers = async () => {
        try {
            const response = await getUsers();
            setUsers(response);
            setError(null);
        } catch (error) {
            console.error("Error obteniendo usuarios:", error);
            setError("No se pudieron obtener los usuarios.");
        }
    };

    return (
        <div>
            <h2>Lista de Usuarios</h2>
            {error && <p style={{ color: "red" }}>{error}</p>}
            <button onClick={fetchUsers}>Actualizar Lista</button>
            <ul>
                {users.length > 0 ? (
                    users.map((user) => (
                        <li key={user.id}>
                            <strong>ID:</strong> {user.id} | <strong>Nombre:</strong> {user.name} | <strong>Email:</strong> {user.email} | <strong>Rol:</strong> {user.role}
                        </li>
                    ))
                ) : (
                    <p>No hay usuarios registrados.</p>
                )}
            </ul>
        </div>
    );
};

export default GetUsers;
