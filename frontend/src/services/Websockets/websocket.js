const WEBSOCKET_URL = "ws://localhost:6001"; // URL del WebSocket en Docker

export const connectWebSocket = () => {
    const socket = new WebSocket(WEBSOCKET_URL);

    socket.onopen = () => {
        console.log("Conexión WebSocket establecida");
    };

    socket.onmessage = (event) => {
        console.log("Mensaje recibido:", event.data);
    };

    socket.onclose = () => {
        console.log("Conexión WebSocket cerrada");
    };

    socket.onerror = (error) => {
        console.error("Error en WebSocket:", error);
    };

    return socket;
};
