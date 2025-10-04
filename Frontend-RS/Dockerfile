# Etapa 1: Construir con Flutter (versión reciente)
FROM ghcr.io/cirruslabs/flutter:3.35.5 AS build

WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Compilar la aplicación para Web
RUN flutter build web --release

# Etapa 2: Servir con Nginx
FROM nginx:alpine

# Copiar la build generada al directorio de Nginx
COPY --from=build /app/build/web /usr/share/nginx/html

# Exponer el puerto 80
EXPOSE 80

# Iniciar Nginx
CMD ["nginx", "-g", "daemon off;"]
