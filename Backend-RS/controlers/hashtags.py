from fastapi import HTTPException
from sqlmodel import Session, select
from models.hashtags import Hashtags, HashtagCreate, HashtagPublic, HashtagUpdate

def CrearHashtag(data: HashtagCreate, session: Session) -> HashtagPublic:
    existente = session.exec(
        select(Hashtags).where(Hashtags.Nombre == data.Nombre)
    ).first()
    if existente:
        raise HTTPException(status_code=409, detail="El hashtag ya existe")

    nuevo = Hashtags(Nombre=data.Nombre, FechaCreacion=data.FechaCreacion)
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return HashtagPublic.model_validate(nuevo)

def LeerHashtagPorId(IdHashtag: int, session: Session) -> HashtagPublic:
    item = session.get(Hashtags, IdHashtag)
    if not item:
        raise HTTPException(status_code=404, detail="Hashtag no encontrado")
    return HashtagPublic.model_validate(item)

def LeerHashtags(session: Session) -> list[HashtagPublic]:
    items = session.exec(select(Hashtags)).all()
    return [HashtagPublic.model_validate(i) for i in items]

def ActualizarHashtag(IdHashtag: int, datos: HashtagUpdate, session: Session) -> HashtagPublic:
    item = session.get(Hashtags, IdHashtag)
    if not item:
        raise HTTPException(status_code=404, detail="Hashtag no encontrado")

    update = datos.model_dump(exclude_unset=True)

    # si cambia el nombre, validar duplicado
    if "Nombre" in update:
        dup = session.exec(
            select(Hashtags).where(
                Hashtags.Nombre == update["Nombre"],
                Hashtags.IdHashtag != IdHashtag
            )
        ).first()
        if dup:
            raise HTTPException(status_code=409, detail="Ya existe un hashtag con ese nombre")

    item.sqlmodel_update(update)
    session.add(item)
    session.commit()
    session.refresh(item)
    return HashtagPublic.model_validate(item)

def EliminarHashtag(IdHashtag: int, session: Session):
    item = session.get(Hashtags, IdHashtag)
    if not item:
        raise HTTPException(status_code=404, detail="Hashtag no encontrado")
    session.delete(item)
    session.commit()
    return {"message": "Hashtag eliminado"}
