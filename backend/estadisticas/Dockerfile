FROM php:8.2-cli

# Instalar extensiones necesarias
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Copiar los archivos al contenedor
WORKDIR /app
COPY server.php .

# Instalar Composer y dependencias
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
COPY composer.json ./
RUN composer install

# Exponer puerto 4000 y ejecutar el servidor PHP
CMD php -S 0.0.0.0:4000 -t /app
