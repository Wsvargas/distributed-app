# Imagen base
FROM golang:1.22

# Crear directorio de la app
WORKDIR /app

# Copiar archivos al contenedor
COPY . .

# Descargar dependencias
RUN go mod init estadisticas && go mod tidy

# Compilar el binario
RUN go build -o estadisticas

# Ejecutar el binario
CMD ["/app/estadisticas"]
