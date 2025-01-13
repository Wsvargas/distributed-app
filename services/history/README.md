# Historial de Reservas

Este microservicio permite consultar el historial de reservas realizadas por los usuarios.

## Endpoints

### 1. Obtener el historial de reservas
**GET /history**

- Respuesta (JSON):
  ```json
  [
    {
      "id": 1,
      "flight_number": "AA123",
      "customer_name": "John Doe",
      "seats_reserved": 2,
      "status": "confirmed",
      "date": "2023-12-10"
    }
  ]
