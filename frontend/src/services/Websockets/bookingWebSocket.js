import { connectWebSocket } from "./websocket";

export const bookingSocket = connectWebSocket();

bookingSocket.onmessage = (event) => {
    console.log("Evento de reserva recibido:", event.data);
};
