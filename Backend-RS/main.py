
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

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "API funcionando"}
