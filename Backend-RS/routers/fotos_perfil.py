from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from config.database import get_session
from models.fotos_perfil import FotosPerfilCreate, FotosPerfilPublic, FotosPerfilUpdate
from controlers.fotos_perfil import (
    CrearFoto, LeerFotoPorId, LeerFotos, ActualizarFoto, EliminarFoto
)
from routers.auth import get_current_active_user
from models.usuario import Usuario
from models.fotos_perfil import FotosPerfil

router = APIRouter()

@router.get("/fotos_perfil", response_model=list[FotosPerfilPublic])
def ObtenerFotos(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    # Ejecutar la consulta para obtener todos los enlaces (fotos)
    fotos = session.exec(select(FotosPerfil)).all()
    return [FotosPerfilPublic.model_validate(foto) for foto in fotos]

# Ruta para obtener una foto por IdFoto
@router.get("/fotos_perfil/{IdFoto}", response_model=FotosPerfilPublic)
def ObtenerFoto(
    IdFoto: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerFotoPorId(IdFoto, session)


# Ruta para crear una foto para un perfil
@router.post("/fotos_perfil", response_model=FotosPerfilPublic)
def CrearFotoUsuario(
    foto: FotosPerfilCreate, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearFoto(foto, session, current_user.IdUsuario)


# Ruta para actualizar una foto
@router.patch("/fotos_perfil/{IdFoto}", response_model=FotosPerfilPublic)
def ActualizarFotoUsuario(
    IdFoto: int, 
    datos: FotosPerfilUpdate, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarFoto(IdFoto, datos, session)


# Ruta para eliminar una foto
@router.delete("/fotos_perfil/{IdFoto}")
def EliminarFotoUsuario(
    IdFoto: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarFoto(IdFoto, session)
