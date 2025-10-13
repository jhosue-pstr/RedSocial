
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'models'))

from fastapi import FastAPI
from contextlib import asynccontextmanager
from config.database import create_db_and_tables
from routers.usuarios import router as users_router
from routers.conversaciones import router as conversacion_router
from routers.mensajes import router as mensaje_router
from routers.archivos_mensajes import router as archivo_router
from routers.participantes_conversacion import router as participante_router
from routers.auth import router as auth_router  # Nuevo router de autenticación
from routers.perfil import router as perfil_router  # Nuevo router de perfil
from routers.enlaces_perfil import router as enlaces_perfil_router
from routers.fotos_perfil import router as fotos_perfil_router
from routers.musica_perfil import router as musica_perfil_router
from routers.publicaciones import router as publicaciones_router
from routers.archivos_publicaciones import router as archivos_publicaciones_router
from routers.menciones_usuario import router as menciones_usuario_router
from routers.likes import router as likes_router
from routers.intereses import router as intereses_router
from routers.perfil_interes import router as perfil_interes_router
from routers.hashtags import router as hashtags_router
from routers.publicacion_hashtag import router as publicacion_hashtag_router
from routers.comentarios import router as comentarios_router  
app = FastAPI()

# Incluir los routers de la API
app.include_router(auth_router, tags=["authentication"])

# Rutas para los recursos de la red social
app.include_router(users_router, prefix="/api", tags=["usuarios"])
app.include_router(conversacion_router, prefix="/api", tags=["conversaciones"])
app.include_router(mensaje_router, prefix="/api", tags=["mensajes"])
app.include_router(archivo_router, prefix="/api", tags=["archivosmensajes"])
app.include_router(participante_router, prefix="/api", tags=["participantes"])
app.include_router(perfil_router, prefix="/api", tags=["perfiles"])
app.include_router(enlaces_perfil_router, prefix="/api", tags=["enlaces_perfil"])
app.include_router(fotos_perfil_router, prefix="/api", tags=["fotos_perfil"])
app.include_router(musica_perfil_router, prefix="/api", tags=["musica_perfil"])
app.include_router(publicaciones_router, prefix="/api", tags=["publicaciones"])
app.include_router(archivos_publicaciones_router, prefix="/api", tags=["archivos_publicaciones"])
app.include_router(menciones_usuario_router, prefix="/api", tags=["menciones_usuario"])
app.include_router(likes_router, prefix="/api", tags=["likes"])
app.include_router(intereses_router, prefix="/api", tags=["intereses"])
app.include_router(perfil_interes_router, prefix="/api", tags=["perfil_interes"])
app.include_router(hashtags_router, prefix="/api", tags=["hashtags"])
app.include_router(publicacion_hashtag_router, prefix="/api", tags=["publicacion_hashtag"])
app.include_router(comentarios_router, prefix="/api", tags=["comentarios"])

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "API funcionando"}
