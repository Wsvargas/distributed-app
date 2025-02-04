import axios from "axios";

const API_BASE_URL = "http://localhost:5002";  // Microservicio de obtener todos los usuarios

export const getUsers = async () => {
    try {
        const response = await axios.get(`${API_BASE_URL}/users`);
        return response.data;
    } catch (error) {
        throw error.response?.data || "Error en el servicio de obtención de usuarios";
    }
};
