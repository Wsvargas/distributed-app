import React, { useState } from "react";
import { updateUser } from "services/User-Management/updateUserService";

const UpdateUser = () => {
    const [userId, setUserId] = useState("");
    const [userData, setUserData] = useState({
        name: "",
        email: "",
        phone: "",
        password: "",
        date_of_birth: "",
        role: "",
        is_active: null
    });
    const [message, setMessage] = useState("");

    const handleChange = (e) => {
        setUserData({ ...userData, [e.target.name]: e.target.value });
    };

    const handleUpdate = async () => {
        if (!userId) {
            alert("Por favor, ingresa un ID de usuario");
            return;
        }

        try {
            const response = await updateUser(userId, userData);
            setMessage(response.message);
        } catch (error) {
            console.error("Error actualizando usuario:", error);
            setMessage("Error al actualizar el usuario");
        }
    };

    return (
        <div>
            <h2>Actualizar Usuario</h2>
            <input
                type="number"
                placeholder="Ingrese ID del usuario"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
            />
            <input type="text" name="name" placeholder="Nombre" onChange={handleChange} />
            <input type="email" name="email" placeholder="Correo" onChange={handleChange} />
            <input type="text" name="phone" placeholder="Teléfono" onChange={handleChange} />
            <input type="password" name="password" placeholder="Contraseña" onChange={handleChange} />
            <input type="date" name="date_of_birth" onChange={handleChange} />
            
            <label>Rol:
                <select name="role" onChange={handleChange}>
                    <option value="">Seleccionar</option>
                    <option value="user">Usuario</option>
                    <option value="admin">Administrador</option>
                </select>
            </label>

            <label>Activo:
                <select name="is_active" onChange={handleChange}>
                    <option value="">Seleccionar</option>
                    <option value="true">Sí</option>
                    <option value="false">No</option>
                </select>
            </label>

            <button onClick={handleUpdate}>Actualizar Usuario</button>

            {message && <p>{message}</p>}
        </div>
    );
};

export default UpdateUser;
