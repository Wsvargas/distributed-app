import React, { useState } from "react";
import { createUser } from "services/User-Management/createUserService";

const CreateUser = () => {
    const [userData, setUserData] = useState({
        name: "",
        email: "",
        phone: "",
        password: "",
        date_of_birth: "",
        role: "user",
        is_active: true
    });

    const handleChange = (e) => {
        setUserData({ ...userData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await createUser(userData);
            alert(response.data.message);
            setUserData({
                name: "",
                email: "",
                phone: "",
                password: "",
                date_of_birth: "",
                role: "user",
                is_active: true
            });
        } catch (error) {
            console.error("Error creando usuario:", error.response?.data || error);
            alert("Error al crear el usuario");
        }
    };

    return (
        <div>
            <h2>Crear Usuario</h2>
            <form onSubmit={handleSubmit}>
                <input type="text" name="name" placeholder="Nombre" value={userData.name} onChange={handleChange} required />
                <input type="email" name="email" placeholder="Correo" value={userData.email} onChange={handleChange} required />
                <input type="text" name="phone" placeholder="Teléfono" value={userData.phone} onChange={handleChange} />
                <input type="password" name="password" placeholder="Contraseña" value={userData.password} onChange={handleChange} required />
                <input type="date" name="date_of_birth" value={userData.date_of_birth} onChange={handleChange} />
                
                <label>Rol:
                    <select name="role" value={userData.role} onChange={handleChange}>
                        <option value="user">Usuario</option>
                        <option value="admin">Administrador</option>
                    </select>
                </label>
                
                <label>Activo:
                    <input type="checkbox" name="is_active" checked={userData.is_active} onChange={(e) => setUserData({ ...userData, is_active: e.target.checked })} />
                </label>

                <button type="submit">Crear Usuario</button>
            </form>
        </div>
    );
};

export default CreateUser;