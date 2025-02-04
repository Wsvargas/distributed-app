import axios from "axios";

const API_BASE_URL = "http://localhost:5008";  // Microservicio de actualización de usuario

export const updateUser = async (userId, userData) => {
    try {
        const response = await axios.put(`${API_BASE_URL}/users/${userId}`, userData, {
            headers: { "Content-Type": "application/json" },
        });
        return response.data;
    } catch (error) {
        throw error.response?.data || "Error en el servicio de actualización de usuario";
    }
};
