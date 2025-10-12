from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from config.database import get_session
from models.musica_perfil import MusicaPerfil, MusicaPerfilCreate, MusicaPerfilPublic, MusicaPerfilUpdate
from controlers.musica_perfil import (
    CrearMusica, LeerMusicaPorId, LeerMusicas, ActualizarMusica, EliminarMusica
)
from routers.auth import get_current_active_user
from models.usuario import Usuario
from models.musica_perfil import MusicaPerfil

router = APIRouter()

# Listar todo
@router.get("/musica_perfil", response_model=list[MusicaPerfilPublic])
def ObtenerMusicas(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerMusicas(session)

# Obtener por IdMusica
@router.get("/musica_perfil/{IdMusica}", response_model=MusicaPerfilPublic)
def ObtenerMusica(
    IdMusica: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerMusicaPorId(IdMusica, session)

# Crear (usa el perfil del usuario autenticado)
@router.post("/musica_perfil", response_model=MusicaPerfilPublic)
def CrearMusicaUsuario(
    musica: MusicaPerfilCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearMusica(musica, session, current_user.IdUsuario)

# Actualizar por IdMusica
@router.patch("/musica_perfil/{IdMusica}", response_model=MusicaPerfilPublic)
def ActualizarMusicaUsuario(
    IdMusica: int,
    datos: MusicaPerfilUpdate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarMusica(IdMusica, datos, session)

# Eliminar por IdMusica
@router.delete("/musica_perfil/{IdMusica}")
def EliminarMusicaUsuario(
    IdMusica: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarMusica(IdMusica, session)
