import axios from "axios";

const API_BASE_URL = "http://localhost:5005";  // Microservicio de eliminación de usuario

export const deleteUser = async (userId) => {
    try {
        const response = await axios.delete(`${API_BASE_URL}/users/${userId}`);
        return response.data;
    } catch (error) {
        throw error.response?.data || "Error en el servicio de eliminación de usuario";
    }
};
