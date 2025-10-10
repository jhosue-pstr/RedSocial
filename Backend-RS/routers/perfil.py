from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.perfil import PerfilCreate, PerfilPublic, PerfilUpdate
from controlers.perfil import (
    CrearPerfil, LeerPerfilPorUsuario, ActualizarPerfil, EliminarPerfil
)
from routers.auth import get_current_active_user
from models.usuario import Usuario  # Importar el modelo Usuario para validación

router = APIRouter()

@router.get("/perfil/{IdUsuario}", response_model=PerfilPublic)
def ObtenerPerfil(
    IdUsuario: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPerfilPorUsuario(IdUsuario, session)


@router.post("/perfil/", response_model=PerfilPublic)
def CrearPerfilUsuario(
    perfil: PerfilCreate, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearPerfil(perfil, session, current_user.IdUsuario)


@router.patch("/perfil/{IdPerfil}", response_model=PerfilPublic)
def ActualizarPerfilUsuario(
    IdPerfil: int, 
    datos: PerfilUpdate, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarPerfil(IdPerfil, datos, session)


@router.delete("/perfil/{IdPerfil}")
def EliminarPerfilUsuario(
    IdPerfil: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarPerfil(IdPerfil, session)
