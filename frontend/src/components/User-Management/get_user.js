import React, { useState } from "react";
import { getUser } from "services/User-Management/getUserService";

const GetUser = () => {
    const [userId, setUserId] = useState("");
    const [userData, setUserData] = useState(null);
    const [error, setError] = useState(null);

    const handleFetchUser = async () => {
        if (!userId) {
            alert("Por favor, ingresa un ID de usuario");
            return;
        }

        try {
            const response = await getUser(userId);
            setUserData(response);
            setError(null);
        } catch (error) {
            console.error("Error obteniendo usuario:", error);
            setError("Usuario no encontrado");
            setUserData(null);
        }
    };

    return (
        <div>
            <h2>Buscar Usuario</h2>
            <input
                type="number"
                placeholder="Ingrese ID del usuario"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
            />
            <button onClick={handleFetchUser}>Buscar Usuario</button>

            {error && <p style={{ color: "red" }}>{error}</p>}

            {userData && (
                <div>
                    <h3>Información del Usuario</h3>
                    <p><strong>ID:</strong> {userData.id}</p>
                    <p><strong>Nombre:</strong> {userData.name}</p>
                    <p><strong>Email:</strong> {userData.email}</p>
                    <p><strong>Teléfono:</strong> {userData.phone}</p>
                    <p><strong>Fecha de Nacimiento:</strong> {userData.date_of_birth}</p>
                    <p><strong>Rol:</strong> {userData.role}</p>
                    <p><strong>Activo:</strong> {userData.is_active ? "Sí" : "No"}</p>
                </div>
            )}
        </div>
    );
};

export default GetUser;
