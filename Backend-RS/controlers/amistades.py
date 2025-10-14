# controlers/amistades.py
from fastapi import HTTPException
from sqlmodel import Session, select
from models.amistades import Amistades, AmistadCreate, AmistadPublic, AmistadUpdate
from models.usuario import Usuario
import datetime

def CrearAmistad(data: AmistadCreate, session: Session) -> AmistadPublic:
    user = session.get(Usuario, data.IdUsuario)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    nueva = Amistades(
        IdUsuario=data.IdUsuario,
        Estado=data.Estado,
        FechaSolicitud=data.FechaSolicitud or datetime.datetime.utcnow(),
        FechaAceptacion=data.FechaAceptacion,
    )
    session.add(nueva)
    session.commit()
    session.refresh(nueva)
    return AmistadPublic.model_validate(nueva)

def LeerAmistadPorId(IdAmistad: int, session: Session) -> AmistadPublic:
    item = session.get(Amistades, IdAmistad)
    if not item:
        raise HTTPException(status_code=404, detail="Amistad no encontrada")
    return AmistadPublic.model_validate(item)

def LeerAmistades(session: Session) -> list[AmistadPublic]:
    items = session.exec(select(Amistades)).all()
    return [AmistadPublic.model_validate(i) for i in items]

def LeerAmistadesPorUsuario(IdUsuario: int, session: Session) -> list[AmistadPublic]:
    items = session.exec(
        select(Amistades).where(Amistades.IdUsuario == IdUsuario)
    ).all()
    return [AmistadPublic.model_validate(i) for i in items]

def ActualizarAmistad(IdAmistad: int, datos: AmistadUpdate, session: Session) -> AmistadPublic:
    item = session.get(Amistades, IdAmistad)
    if not item:
        raise HTTPException(status_code=404, detail="Amistad no encontrada")

    update_data = datos.model_dump(exclude_unset=True)
    item.sqlmodel_update(update_data)
    if "Estado" in update_data and update_data["Estado"] == "aceptada" and not item.FechaAceptacion:
        item.FechaAceptacion = datetime.datetime.utcnow()

    session.add(item)
    session.commit()
    session.refresh(item)
    return AmistadPublic.model_validate(item)

def EliminarAmistad(IdAmistad: int, session: Session):
    item = session.get(Amistades, IdAmistad)
    if not item:
        raise HTTPException(status_code=404, detail="Amistad no encontrada")
    session.delete(item)
    session.commit()
    return {"message": "Amistad eliminada"}
