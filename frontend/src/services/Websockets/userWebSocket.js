import { connectWebSocket } from "./websocket";

export const userSocket = connectWebSocket();

userSocket.onmessage = (event) => {
    console.log("Evento de usuario recibido:", event.data);
};
