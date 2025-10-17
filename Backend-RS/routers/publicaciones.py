from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from config.database import get_session
from models.publicaciones import (
    Publicaciones, PublicacionesCreate, PublicacionesPublic, PublicacionesUpdate
)
from controlers.publicaciones import (
    CrearPublicacion, LeerPublicacionPorId, LeerPublicaciones, ActualizarPublicacion, EliminarPublicacion
)
from routers.auth import get_current_active_user
from models.usuario import Usuario

router = APIRouter()

# Listar todas las publicaciones
@router.get("/publicaciones", response_model=list[PublicacionesPublic])
def ObtenerPublicaciones(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPublicaciones(session)

# Obtener una publicación por IdPublicacion
@router.get("/publicaciones/{IdPublicacion}", response_model=PublicacionesPublic)
def ObtenerPublicacion(
    IdPublicacion: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPublicacionPorId(IdPublicacion, session)

# Crear publicación (usa el perfil del usuario autenticado)
@router.post("/publicaciones", response_model=PublicacionesPublic)
def CrearPublicacionUsuario(
    data: PublicacionesCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearPublicacion(data, session, current_user.IdUsuario)

# Actualizar publicación
@router.patch("/publicaciones/{IdPublicacion}", response_model=PublicacionesPublic)
def ActualizarPublicacionUsuario(
    IdPublicacion: int,
    datos: PublicacionesUpdate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarPublicacion(IdPublicacion, datos, session)

# Eliminar publicación
@router.delete("/publicaciones/{IdPublicacion}")
def EliminarPublicacionUsuario(
    IdPublicacion: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarPublicacion(IdPublicacion, session)
