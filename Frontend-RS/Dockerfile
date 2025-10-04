# Etapa 1: Compilar Flutter web
FROM ghcr.io/cirruslabs/flutter:3.24.3 AS build

WORKDIR /app

# Copiamos el código fuente
COPY . .

# Compilamos el proyecto Flutter para Web
RUN flutter build web --release

# Etapa 2: Servir con Nginx
FROM nginx:alpine

# Limpiamos el html default de Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copiamos la build de Flutter desde la etapa anterior
COPY --from=build /app/build/web /usr/share/nginx/html

# Exponemos el puerto
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
