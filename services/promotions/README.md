# Gestión de Promociones

Este microservicio permite gestionar las promociones asociadas a los vuelos o usuarios.

## Endpoints

### 1. Crear una promoción
**POST /promotions**

- Body (JSON):
  ```json
  {
    "title": "Descuento de Verano",
    "description": "20% de descuento en todos los vuelos internacionales",
    "discount": 20.0,
    "active": true
  }
**Respuesta**
```json
  {
    "message": "Promotion created successfully"
  }