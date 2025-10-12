from fastapi import HTTPException
from sqlmodel import Session, select
from models.likes import Likes, LikesCreate, LikesPublic, LikesUpdate
from models.publicaciones import Publicaciones

def CrearLike(data: LikesCreate, session: Session, id_usuario: int) -> LikesPublic:
    # verificar publicacion
    pub = session.get(Publicaciones, data.IdPublicacion)
    if not pub:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")

    # evitar duplicados (por la restricción única y por lógica)
    existente = session.exec(
        select(Likes).where(
            Likes.IdPublicacion == data.IdPublicacion,
            Likes.IdUsuario == id_usuario
        )
    ).first()
    if existente:
        raise HTTPException(status_code=409, detail="Ya diste like a esta publicación")

    nuevo = Likes(IdPublicacion=data.IdPublicacion, IdUsuario=id_usuario)
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return LikesPublic.model_validate(nuevo)

def LeerLikePorId(IdLike: int, session: Session) -> LikesPublic:
    like = session.get(Likes, IdLike)
    if not like:
        raise HTTPException(status_code=404, detail="Like no encontrado")
    return LikesPublic.model_validate(like)

def LeerLikes(session: Session) -> list[LikesPublic]:
    items = session.exec(select(Likes)).all()
    return [LikesPublic.model_validate(i) for i in items]

def LeerLikesPorPublicacion(IdPublicacion: int, session: Session) -> list[LikesPublic]:
    items = session.exec(select(Likes).where(Likes.IdPublicacion == IdPublicacion)).all()
    return [LikesPublic.model_validate(i) for i in items]

def LeerLikesPorUsuario(IdUsuario: int, session: Session) -> list[LikesPublic]:
    items = session.exec(select(Likes).where(Likes.IdUsuario == IdUsuario)).all()
    return [LikesPublic.model_validate(i) for i in items]

def EliminarLike(IdLike: int, session: Session):
    like = session.get(Likes, IdLike)
    if not like:
        raise HTTPException(status_code=404, detail="Like no encontrado")
    session.delete(like)
    session.commit()
    return {"message": "Like eliminado"}

# útil para "unlike" por par (pub, usuario autenticado)
def EliminarLikePorPar(IdPublicacion: int, id_usuario: int, session: Session):
    like = session.exec(
        select(Likes).where(Likes.IdPublicacion == IdPublicacion, Likes.IdUsuario == id_usuario)
    ).first()
    if not like:
        raise HTTPException(status_code=404, detail="Like no encontrado para este usuario/publicación")
    session.delete(like)
    session.commit()
    return {"message": "Like eliminado"}
