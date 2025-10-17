from fastapi import HTTPException
from sqlmodel import Session, select
from models.publicacion_hashtag import (
    PublicacionHashtag, PublicacionHashtagCreate, PublicacionHashtagPublic, PublicacionHashtagUpdate
)
from models.publicaciones import Publicaciones
from models.hashtags import Hashtags

def CrearPublicacionHashtag(data: PublicacionHashtagCreate, session: Session) -> PublicacionHashtagPublic:
    if not session.get(Publicaciones, data.IdPublicacion):
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    if not session.get(Hashtags, data.IdHashtag):
        raise HTTPException(status_code=404, detail="Hashtag no encontrado")

    # evitar duplicado (además del UniqueConstraint)
    existe = session.exec(
        select(PublicacionHashtag).where(
            PublicacionHashtag.IdPublicacion == data.IdPublicacion,
            PublicacionHashtag.IdHashtag == data.IdHashtag
        )
    ).first()
    if existe:
        raise HTTPException(status_code=409, detail="La publicación ya tiene ese hashtag")

    nuevo = PublicacionHashtag(**data.model_dump())
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return PublicacionHashtagPublic.model_validate(nuevo)

def LeerPublicacionHashtagPorId(IdPublicacionHashtag: int, session: Session) -> PublicacionHashtagPublic:
    item = session.get(PublicacionHashtag, IdPublicacionHashtag)
    if not item:
        raise HTTPException(status_code=404, detail="Relación publicación-hashtag no encontrada")
    return PublicacionHashtagPublic.model_validate(item)

def LeerPublicacionesHashtags(session: Session) -> list[PublicacionHashtagPublic]:
    items = session.exec(select(PublicacionHashtag)).all()
    return [PublicacionHashtagPublic.model_validate(i) for i in items]

def LeerPorPublicacion(IdPublicacion: int, session: Session) -> list[PublicacionHashtagPublic]:
    items = session.exec(
        select(PublicacionHashtag).where(PublicacionHashtag.IdPublicacion == IdPublicacion)
    ).all()
    return [PublicacionHashtagPublic.model_validate(i) for i in items]

def LeerPorHashtag(IdHashtag: int, session: Session) -> list[PublicacionHashtagPublic]:
    items = session.exec(
        select(PublicacionHashtag).where(PublicacionHashtag.IdHashtag == IdHashtag)
    ).all()
    return [PublicacionHashtagPublic.model_validate(i) for i in items]

def ActualizarPublicacionHashtag(IdPublicacionHashtag: int, datos: PublicacionHashtagUpdate, session: Session) -> PublicacionHashtagPublic:
    item = session.get(PublicacionHashtag, IdPublicacionHashtag)
    if not item:
        raise HTTPException(status_code=404, detail="Relación publicación-hashtag no encontrada")

    update = datos.model_dump(exclude_unset=True)

    if "IdPublicacion" in update and not session.get(Publicaciones, update["IdPublicacion"]):
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    if "IdHashtag" in update and not session.get(Hashtags, update["IdHashtag"]):
        raise HTTPException(status_code=404, detail="Hashtag no encontrado")

    pub_final = update.get("IdPublicacion", item.IdPublicacion)
    tag_final = update.get("IdHashtag", item.IdHashtag)

    dup = session.exec(
        select(PublicacionHashtag).where(
            PublicacionHashtag.IdPublicacion == pub_final,
            PublicacionHashtag.IdHashtag == tag_final,
            PublicacionHashtag.IdPublicacionHashtag != IdPublicacionHashtag
        )
    ).first()
    if dup:
        raise HTTPException(status_code=409, detail="Ya existe esa combinación Publicación-Hashtag")

    item.sqlmodel_update(update)
    session.add(item)
    session.commit()
    session.refresh(item)
    return PublicacionHashtagPublic.model_validate(item)

def EliminarPublicacionHashtag(IdPublicacionHashtag: int, session: Session):
    item = session.get(PublicacionHashtag, IdPublicacionHashtag)
    if not item:
        raise HTTPException(status_code=404, detail="Relación publicación-hashtag no encontrada")
    session.delete(item)
    session.commit()
    return {"message": "Relación eliminada"}

def EliminarPorPar(IdPublicacion: int, IdHashtag: int, session: Session):
    item = session.exec(
        select(PublicacionHashtag).where(
            PublicacionHashtag.IdPublicacion == IdPublicacion,
            PublicacionHashtag.IdHashtag == IdHashtag
        )
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="No existe esa combinación Publicación-Hashtag")
    session.delete(item)
    session.commit()
    return {"message": "Relación eliminada"}
