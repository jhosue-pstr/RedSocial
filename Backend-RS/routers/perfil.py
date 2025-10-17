from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.perfil import PerfilCreate, PerfilPublic, PerfilUpdate
from controlers.perfil import (
    CrearPerfil, LeerPerfilPorId, LeerPerfiles, ActualizarPerfil, EliminarPerfil
)
from routers.auth import get_current_active_user
from models.usuario import Usuario  # Importar Usuario para validación

router = APIRouter()

# Ruta para obtener todos los perfiles
@router.get("/perfil", response_model=list[PerfilPublic])
def ObtenerPerfiles(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPerfiles(session)

# Ruta para obtener el perfil por IdPerfil
@router.get("/perfil/{IdPerfil}", response_model=PerfilPublic)
def ObtenerPerfil(
    IdPerfil: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPerfilPorId(IdPerfil, session)

# Ruta para crear un perfil para el usuario autenticado
@router.post("/perfil/", response_model=PerfilPublic)
def CrearPerfilUsuario(
    perfil: PerfilCreate, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearPerfil(perfil, session, current_user.IdUsuario)

# Ruta para actualizar el perfil (usando PATCH)
@router.patch("/perfil/{IdPerfil}", response_model=PerfilPublic)
def ActualizarPerfilUsuario(
    IdPerfil: int, 
    datos: PerfilUpdate, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarPerfil(IdPerfil, datos, session)

# Ruta para eliminar un perfil
@router.delete("/perfil/{IdPerfil}")
def EliminarPerfilUsuario(
    IdPerfil: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarPerfil(IdPerfil, session)
