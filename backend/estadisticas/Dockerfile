# Usar una imagen de Go
FROM golang:1.20

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . .

# Descargar dependencias
RUN go mod tidy

# Compilar la aplicación
RUN go build -o estadisticas

# Exponer el puerto 8080
EXPOSE 8080

# Ejecutar la aplicación
CMD ["./estadisticas"]
