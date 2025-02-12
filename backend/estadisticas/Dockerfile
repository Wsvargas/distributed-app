FROM php:8.2-cli

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    git \
    unzip \
    zip \
    && docker-php-ext-install pdo pdo_mysql mysqli

# Instalar Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Crear directorio de la aplicación
WORKDIR /app

# Copiar archivos del proyecto
COPY composer.json ./
RUN composer install --no-dev --prefer-dist --optimize-autoloader

COPY server.php ./

# Exponer el puerto 4000 y ejecutar el servidor PHP
CMD php -S 0.0.0.0:4000 -t /app
