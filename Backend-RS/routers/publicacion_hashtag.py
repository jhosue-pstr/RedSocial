from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.publicacion_hashtag import (
    PublicacionHashtagCreate, PublicacionHashtagPublic, PublicacionHashtagUpdate
)
from controlers.publicacion_hashtag import (
    CrearPublicacionHashtag, LeerPublicacionHashtagPorId, LeerPublicacionesHashtags,
    LeerPorPublicacion, LeerPorHashtag, ActualizarPublicacionHashtag,
    EliminarPublicacionHashtag, EliminarPorPar
)
from routers.auth import get_current_active_user
from models.usuario import Usuario

router = APIRouter()

# Listar todas las relaciones
@router.get("/publicacion_hashtag", response_model=list[PublicacionHashtagPublic])
def ObtenerPublicacionesHashtags(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPublicacionesHashtags(session)

# Listar por publicación
@router.get("/publicacion_hashtag/publicacion/{IdPublicacion}", response_model=list[PublicacionHashtagPublic])
def ObtenerPorPublicacion(
    IdPublicacion: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPorPublicacion(IdPublicacion, session)

# Listar por hashtag
@router.get("/publicacion_hashtag/hashtag/{IdHashtag}", response_model=list[PublicacionHashtagPublic])
def ObtenerPorHashtag(
    IdHashtag: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPorHashtag(IdHashtag, session)

# Obtener por IdPublicacionHashtag
@router.get("/publicacion_hashtag/{IdPublicacionHashtag}", response_model=PublicacionHashtagPublic)
def ObtenerPublicacionHashtag(
    IdPublicacionHashtag: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPublicacionHashtagPorId(IdPublicacionHashtag, session)

# Crear relación
@router.post("/publicacion_hashtag", response_model=PublicacionHashtagPublic)
def CrearRelacion(
    data: PublicacionHashtagCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearPublicacionHashtag(data, session)

# Actualizar relación
@router.patch("/publicacion_hashtag/{IdPublicacionHashtag}", response_model=PublicacionHashtagPublic)
def ActualizarRelacion(
    IdPublicacionHashtag: int,
    datos: PublicacionHashtagUpdate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarPublicacionHashtag(IdPublicacionHashtag, datos, session)

# Eliminar por Id
@router.delete("/publicacion_hashtag/{IdPublicacionHashtag}")
def EliminarRelacion(
    IdPublicacionHashtag: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarPublicacionHashtag(IdPublicacionHashtag, session)

# Eliminar por par (IdPublicacion, IdHashtag)
@router.delete("/publicacion_hashtag/publicacion/{IdPublicacion}/hashtag/{IdHashtag}")
def EliminarRelacionPorPar(
    IdPublicacion: int,
    IdHashtag: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarPorPar(IdPublicacion, IdHashtag, session)
