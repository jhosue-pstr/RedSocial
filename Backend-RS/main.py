from fastapi import FastAPI
from config.database import create_db_and_tables
from routers.usuarios import router as users_router
from routers.conversaciones import router as conversacion_router
from routers.mensajes import router as mensaje_router
from routers.archivos_mensajes import router as archivo_router
from routers.participantes_conversacion import router as participante_router
from routers.auth import router as auth_router  

app = FastAPI()

app.include_router(auth_router, tags=["authentication"])

app.include_router(users_router, prefix="/api", tags=["usuarios"])
app.include_router(conversacion_router, prefix="/api", tags=["conversaciones"])
app.include_router(mensaje_router, prefix="/api", tags=["mensajes"])
app.include_router(archivo_router, prefix="/api", tags=["archivosmensajes"])
app.include_router(participante_router, prefix="/api", tags=["participantes"])

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "API funcionando"}

