# Usa Go como base
FROM golang:1.22

# Configurar directorio de trabajo
WORKDIR /app

# Copiar archivos y dependencias
COPY go.mod go.sum ./
RUN go mod tidy

# Copiar el código fuente
COPY . .

# Compilar el código
RUN go build -o estadisticas

# Exponer el puerto
EXPOSE 8080

# Ejecutar la aplicación
CMD ["./estadisticas"]
