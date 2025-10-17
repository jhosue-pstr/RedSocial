from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from config.database import get_session
from models.archivos_publicaciones import (ArchivosPublicaciones, ArchivosPublicacionesCreate, ArchivosPublicacionesPublic, ArchivosPublicacionesUpdate)
from controlers.archivos_publicaciones import (
    CrearArchivoPublicacion, LeerArchivoPorId, LeerArchivos,
    LeerArchivosPorPublicacion, ActualizarArchivo, EliminarArchivo
)
from routers.auth import get_current_active_user
from models.usuario import Usuario
from models.archivos_publicaciones import ArchivosPublicaciones

router = APIRouter()

# Listar todos los archivos
@router.get("/archivos_publicaciones", response_model=list[ArchivosPublicacionesPublic])
def ObtenerArchivos(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerArchivos(session)

# Listar archivos de una publicación
@router.get("/archivos_publicaciones/publicacion/{IdPublicacion}", response_model=list[ArchivosPublicacionesPublic])
def ObtenerArchivosDePublicacion(
    IdPublicacion: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerArchivosPorPublicacion(IdPublicacion, session)

# Obtener un archivo por IdArchivo
@router.get("/archivos_publicaciones/{IdArchivo}", response_model=ArchivosPublicacionesPublic)
def ObtenerArchivo(
    IdArchivo: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerArchivoPorId(IdArchivo, session)

# Crear archivo para una publicación específica
@router.post("/archivos_publicaciones/publicacion/{IdPublicacion}", response_model=ArchivosPublicacionesPublic)
def CrearArchivoParaPublicacion(
    IdPublicacion: int,
    data: ArchivosPublicacionesCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearArchivoPublicacion(data, session, IdPublicacion)

# Actualizar archivo por IdArchivo
@router.patch("/archivos_publicaciones/{IdArchivo}", response_model=ArchivosPublicacionesPublic)
def ActualizarArchivoPublicacion(
    IdArchivo: int,
    datos: ArchivosPublicacionesUpdate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarArchivo(IdArchivo, datos, session)

# Eliminar archivo por IdArchivo
@router.delete("/archivos_publicaciones/{IdArchivo}")
def EliminarArchivoPublicacion(
    IdArchivo: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarArchivo(IdArchivo, session)
