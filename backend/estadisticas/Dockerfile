# Usa Go como imagen base
FROM golang:1.22 AS builder

# Configurar directorio de trabajo
WORKDIR /app

# Copiar archivos de dependencias primero (para aprovechar la cache)
COPY go.mod go.sum ./
RUN go mod tidy

# Copiar el código fuente
COPY . .

# Compilar el código
RUN go build -o estadisticas

# Crear una imagen final más ligera
FROM alpine:latest
WORKDIR /root/

# Instalar dependencias mínimas necesarias
RUN apk add --no-cache ca-certificates

# Copiar el binario compilado desde el builder
COPY --from=builder /app/estadisticas .

# Exponer el puerto
EXPOSE 8080

# Ejecutar la aplicación
CMD ["./estadisticas"]
