# routers/comentarios.py
from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.comentarios import ComentarioCreate, ComentarioPublic, ComentarioUpdate
from controlers.comentarios import (
    CrearComentario, LeerComentariosPorPublicacion, LeerComentariosPorUsuario,
    LeerComentarios, LeerComentarioPorId, ActualizarComentario, EliminarComentario
)
from routers.auth import get_current_active_user
from models.usuario import Usuario

router = APIRouter()

# Ruta para crear un comentario
@router.post("/comentarios/{id_publicacion}", response_model=ComentarioPublic)
def CrearComentarioUsuario(
    comentario: ComentarioCreate, 
    id_publicacion: int,  # id_publicacion como parte de la URL
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearComentario(comentario, session, id_publicacion, current_user.IdUsuario)

# Ruta para obtener todos los comentarios
@router.get("/comentarios", response_model=list[ComentarioPublic])
def ObtenerTodosComentarios(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerComentarios(session)

# Ruta para obtener un comentario por IdComentario
@router.get("/comentarios/{IdComentario}", response_model=ComentarioPublic)
def ObtenerComentarioPorId(
    IdComentario: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerComentarioPorId(IdComentario, session)

# Ruta para obtener todos los comentarios de una publicación
@router.get("/comentarios/publicacion/{IdPublicacion}", response_model=list[ComentarioPublic])
def ObtenerComentariosPorPublicacion(
    IdPublicacion: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerComentariosPorPublicacion(IdPublicacion, session)

# Ruta para obtener todos los comentarios de un usuario
@router.get("/comentarios/usuario/{IdUsuario}", response_model=list[ComentarioPublic])
def ObtenerComentariosPorUsuario(
    IdUsuario: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerComentariosPorUsuario(IdUsuario, session)

# Ruta para actualizar un comentario
@router.patch("/comentarios/{IdComentario}", response_model=ComentarioPublic)
def ActualizarComentarioUsuario(
    IdComentario: int, 
    datos: ComentarioUpdate, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarComentario(IdComentario, datos, session)

# Ruta para eliminar un comentario
@router.delete("/comentarios/{IdComentario}")
def EliminarComentarioUsuario(
    IdComentario: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarComentario(IdComentario, session)
