# controlers/comentarios.py
from fastapi import HTTPException
from sqlmodel import Session, select
from models.comentarios import Comentario, ComentarioCreate, ComentarioPublic, ComentarioUpdate
from models.publicaciones import Publicaciones
from models.usuario import Usuario

# Crear un comentario
def CrearComentario(comentario: ComentarioCreate, session: Session, id_publicacion: int, id_usuario: int) -> ComentarioPublic:
    publicacion_db = session.get(Publicaciones, id_publicacion)
    usuario_db = session.get(Usuario, id_usuario)

    if not publicacion_db:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    nuevo_comentario = Comentario(
        Contenido=comentario.Contenido,
        IdPublicacion=id_publicacion,
        IdUsuario=id_usuario
    )

    session.add(nuevo_comentario)
    session.commit()
    session.refresh(nuevo_comentario)
    return ComentarioPublic.model_validate(nuevo_comentario)

# Leer todos los comentarios
def LeerComentarios(session: Session) -> list[ComentarioPublic]:
    comentarios = session.exec(select(Comentario)).all()
    return [ComentarioPublic.model_validate(c) for c in comentarios]

# Leer comentarios de una publicación
def LeerComentariosPorPublicacion(IdPublicacion: int, session: Session) -> list[ComentarioPublic]:
    comentarios = session.exec(select(Comentario).where(Comentario.IdPublicacion == IdPublicacion)).all()
    return [ComentarioPublic.model_validate(c) for c in comentarios]

# Leer comentarios de un usuario
def LeerComentariosPorUsuario(IdUsuario: int, session: Session) -> list[ComentarioPublic]:
    comentarios = session.exec(select(Comentario).where(Comentario.IdUsuario == IdUsuario)).all()
    return [ComentarioPublic.model_validate(c) for c in comentarios]

# Leer un comentario por IdComentario
def LeerComentarioPorId(IdComentario: int, session: Session) -> ComentarioPublic:
    comentario = session.get(Comentario, IdComentario)
    if not comentario:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return ComentarioPublic.model_validate(comentario)

# Actualizar un comentario
def ActualizarComentario(IdComentario: int, datos: ComentarioUpdate, session: Session) -> ComentarioPublic:
    comentario_db = session.get(Comentario, IdComentario)
    if not comentario_db:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")

    update_data = datos.model_dump(exclude_unset=True)
    comentario_db.sqlmodel_update(update_data)

    session.add(comentario_db)
    session.commit()
    session.refresh(comentario_db)
    return ComentarioPublic.model_validate(comentario_db)

# Eliminar un comentario
def EliminarComentario(IdComentario: int, session: Session):
    comentario_db = session.get(Comentario, IdComentario)
    if not comentario_db:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    session.delete(comentario_db)
    session.commit()
    return {"message": "Comentario eliminado"}
