# Usamos PHP 8.2 CLI con extensiones necesarias
FROM php:8.2-cli

# Instalamos las extensiones necesarias para MariaDB (MySQL)
RUN docker-php-ext-install mysqli

# Creamos y establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo del servidor
COPY server.php .

# Exponemos el puerto 4000
EXPOSE 4000

# Comando para iniciar el servidor
CMD ["php", "-S", "0.0.0.0:4000", "-t", "."]
