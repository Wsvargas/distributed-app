import React from 'react';
import ReactDOM from 'react-dom';
import './index.js'; // Si tienes un archivo de estilos global
import App from './App';
import reportWebVitals from './reportWebVitals'; // Opcional, para medir el rendimiento
import { BrowserRouter } from 'react-router-dom'; // Importa BrowserRouter para manejar las rutas

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
);

// Si deseas medir el rendimiento de tu aplicación, puedes usar reportWebVitals
reportWebVitals();