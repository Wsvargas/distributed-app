const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

// Conexión a MongoDB (cambia la URL según tu entorno)
mongoose.connect('mongodb://localhost:27017/logs', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Connected to MongoDB');
}).catch(err => {
    console.error('MongoDB connection error:', err);
});

// Definir el esquema y modelo de Log
const logSchema = new mongoose.Schema({
    service: String,
    level: String,
    message: String,
    timestamp: { type: Date, default: Date.now }
});

const Log = mongoose.model('Log', logSchema);

// Endpoint para registrar un log
app.post('/logs', async (req, res) => {
    try {
        const log = new Log(req.body);
        await log.save();
        res.status(201).json({ message: 'Log registered successfully' });
    } catch (err) {
        res.status(500).json({ error: 'Failed to register log' });
    }
});

// Endpoint para obtener todos los logs
app.get('/logs', async (req, res) => {
    try {
        const logs = await Log.find();
        res.status(200).json(logs);
    } catch (err) {
        res.status(500).json({ error: 'Failed to retrieve logs' });
    }
});

app.listen(3001, () => {
    console.log('Logs service running on port 3001');
});
