# Autenticación y Gestión de Usuarios

Este microservicio se encarga de la autenticación y gestión de usuarios, permitiendo el registro, inicio de sesión y autenticación mediante tokens JWT.

## Endpoints

### 1. Registro de usuarios
**POST /register**
- Body (JSON):
  ```json
  {
    "username": "user1",
    "password": "password123"
  }