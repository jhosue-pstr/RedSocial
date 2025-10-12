from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.hashtags import HashtagCreate, HashtagPublic, HashtagUpdate
from controlers.hashtags import (
    CrearHashtag, LeerHashtagPorId, LeerHashtags, ActualizarHashtag, EliminarHashtag
)
from routers.auth import get_current_active_user
from models.usuario import Usuario

router = APIRouter()

# Listar todos los hashtags
@router.get("/hashtags", response_model=list[HashtagPublic])
def ObtenerHashtags(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerHashtags(session)

# Obtener un hashtag por ID
@router.get("/hashtags/{IdHashtag}", response_model=HashtagPublic)
def ObtenerHashtag(
    IdHashtag: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerHashtagPorId(IdHashtag, session)

# Crear un hashtag
@router.post("/hashtags", response_model=HashtagPublic)
def CrearHashtagRuta(
    data: HashtagCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearHashtag(data, session)

# Actualizar un hashtag
@router.patch("/hashtags/{IdHashtag}", response_model=HashtagPublic)
def ActualizarHashtagRuta(
    IdHashtag: int,
    datos: HashtagUpdate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarHashtag(IdHashtag, datos, session)

# Eliminar un hashtag
@router.delete("/hashtags/{IdHashtag}")
def EliminarHashtagRuta(
    IdHashtag: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarHashtag(IdHashtag, session)
