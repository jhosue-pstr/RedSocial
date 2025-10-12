from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.likes import LikesCreate, LikesPublic, LikesUpdate
from controlers.likes import (
    CrearLike, LeerLikePorId, LeerLikes, LeerLikesPorPublicacion,
    LeerLikesPorUsuario, EliminarLike, EliminarLikePorPar
)
from routers.auth import get_current_active_user
from models.usuario import Usuario

router = APIRouter()

# Listar todos
@router.get("/likes", response_model=list[LikesPublic])
def ObtenerLikes(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerLikes(session)

# Listar por publicación
@router.get("/likes/publicacion/{IdPublicacion}", response_model=list[LikesPublic])
def ObtenerLikesDePublicacion(
    IdPublicacion: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerLikesPorPublicacion(IdPublicacion, session)

# Listar por usuario
@router.get("/likes/usuario/{IdUsuario}", response_model=list[LikesPublic])
def ObtenerLikesDeUsuario(
    IdUsuario: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerLikesPorUsuario(IdUsuario, session)

# Obtener por IdLike
@router.get("/likes/{IdLike}", response_model=LikesPublic)
def ObtenerLike(
    IdLike: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerLikePorId(IdLike, session)

# Crear like (usa el usuario autenticado)
@router.post("/likes", response_model=LikesPublic)
def CrearLikeRuta(
    data: LikesCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearLike(data, session, current_user.IdUsuario)

# Eliminar por IdLike
@router.delete("/likes/{IdLike}")
def EliminarLikeRuta(
    IdLike: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarLike(IdLike, session)

# "Unlike" por par (publicación + usuario autenticado)
@router.delete("/likes/publicacion/{IdPublicacion}")
def EliminarLikePorParRuta(
    IdPublicacion: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarLikePorPar(IdPublicacion, current_user.IdUsuario, session)
