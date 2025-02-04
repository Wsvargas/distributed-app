import axios from "axios";

const API_BASE_URL = "http://localhost:5003";  // Microservicio de obtener usuario por ID

export const getUser = async (userId) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/users/${userId}`);
        return response.data;
    } catch (error) {
        throw error.response?.data || "Error en el servicio de obtención de usuario";
    }
};
