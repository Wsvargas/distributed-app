import React, { useState } from "react";
import { deleteUser } from "services/User-Management/deleteUserService";

const DeleteUser = () => {
    const [userId, setUserId] = useState("");

    const handleDelete = async () => {
        if (!userId) {
            alert("Por favor, ingresa un ID de usuario");
            return;
        }

        try {
            const response = await deleteUser(userId);
            alert(response.message);
            setUserId("");
        } catch (error) {
            console.error("Error eliminando usuario:", error);
            alert("Error al eliminar el usuario");
        }
    };

    return (
        <div>
            <h2>Eliminar Usuario</h2>
            <input
                type="number"
                placeholder="Ingrese ID del usuario"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
            />
            <button onClick={handleDelete}>Eliminar Usuario</button>
        </div>
    );
};

export default DeleteUser;
