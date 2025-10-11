from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from config.database import get_session
from models.enlaces_perfil import EnlacesPerfilCreate, EnlacesPerfilPublic, EnlacesPerfilUpdate
from controlers.enlaces_perfil import (
    CrearEnlace, LeerEnlacePorId, LeerEnlaces, ActualizarEnlace, EliminarEnlace
)
from routers.auth import get_current_active_user
from models.usuario import Usuario
from models.enlaces_perfil import EnlacesPerfil

router = APIRouter()

# Ruta para obtener todos los enlaces
@router.get("/enlaces_perfil", response_model=list[EnlacesPerfilPublic])
def ObtenerEnlaces(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    # Obtener todos los enlaces de la base de datos
    enlaces = session.exec(select(EnlacesPerfil)).all()  # Ejecutar la consulta
    return [EnlacesPerfilPublic.model_validate(enlace) for enlace in enlaces]


# Ruta para obtener un enlace por IdEnlace
@router.get("/enlaces_perfil/{IdEnlace}", response_model=EnlacesPerfilPublic)
def ObtenerEnlace(
    IdEnlace: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerEnlacePorId(IdEnlace, session)


# Ruta para crear un enlace para un perfil
@router.post("/enlaces_perfil", response_model=EnlacesPerfilPublic)
def CrearEnlaceUsuario(
    enlace: EnlacesPerfilCreate, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearEnlace(enlace, session, current_user.IdUsuario)


# Ruta para actualizar un enlace
@router.patch("/enlaces_perfil/{IdEnlace}", response_model=EnlacesPerfilPublic)
def ActualizarEnlaceUsuario(
    IdEnlace: int, 
    datos: EnlacesPerfilUpdate, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarEnlace(IdEnlace, datos, session)


# Ruta para eliminar un enlace
@router.delete("/enlaces_perfil/{IdEnlace}")
def EliminarEnlaceUsuario(
    IdEnlace: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarEnlace(IdEnlace, session)
