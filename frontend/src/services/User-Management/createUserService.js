import axios from "axios";

const API_BASE_URL = "http://localhost:5001";  // Microservicio de creación de usuario

export const createUser = async (userData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/users`, userData, {
            headers: { "Content-Type": "application/json" },
        });
        return response.data;
    } catch (error) {
        throw error.response?.data || "Error en el servicio de creación de usuario";
    }
};
