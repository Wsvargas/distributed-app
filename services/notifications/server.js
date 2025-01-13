const express = require('express');
const http = require('http');
const WebSocket = require('ws');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// Almacenar las conexiones activas
const clients = new Set();

wss.on('connection', (ws) => {
    console.log('New client connected');
    clients.add(ws);

    ws.on('message', (message) => {
        console.log(`Received message: ${message}`);
    });

    ws.on('close', () => {
        console.log('Client disconnected');
        clients.delete(ws);
    });
});

// Endpoint para enviar notificaciones a todos los clientes
app.post('/notify', express.json(), (req, res) => {
    const { message } = req.body;
    clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(message);
        }
    });
    res.status(200).json({ message: 'Notification sent to all clients' });
});

server.listen(3000, () => {
    console.log('WebSocket server running on port 3000');
});
