# Dockerfile
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que corre Flask
EXPOSE 5003

# Comando para ejecutar el servicio
CMD ["python", "auth.py"]
