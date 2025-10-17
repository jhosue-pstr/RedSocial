from fastapi import HTTPException
from sqlmodel import Session, select
from models.perfil_interes import (
    PerfilInteres, PerfilInteresCreate, PerfilInteresPublic, PerfilInteresUpdate
)
from models.perfil import Perfil
from models.intereses import Intereses

def CrearPerfilInteres(data: PerfilInteresCreate, session: Session) -> PerfilInteresPublic:
    # validar FK
    if not session.get(Perfil, data.IdPerfil):
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    if not session.get(Intereses, data.IdInteres):
        raise HTTPException(status_code=404, detail="Interés no encontrado")

    # evitar duplicados (además del UniqueConstraint de la BD)
    existente = session.exec(
        select(PerfilInteres).where(
            PerfilInteres.IdPerfil == data.IdPerfil,
            PerfilInteres.IdInteres == data.IdInteres
        )
    ).first()
    if existente:
        raise HTTPException(status_code=409, detail="El perfil ya tiene este interés")

    nuevo = PerfilInteres(**data.model_dump())
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return PerfilInteresPublic.model_validate(nuevo)

def LeerPerfilInteresPorId(IdPerfilInteres: int, session: Session) -> PerfilInteresPublic:
    item = session.get(PerfilInteres, IdPerfilInteres)
    if not item:
        raise HTTPException(status_code=404, detail="Relación perfil-interés no encontrada")
    return PerfilInteresPublic.model_validate(item)

def LeerPerfilIntereses(session: Session) -> list[PerfilInteresPublic]:
    items = session.exec(select(PerfilInteres)).all()
    return [PerfilInteresPublic.model_validate(i) for i in items]

def LeerPorPerfil(IdPerfil: int, session: Session) -> list[PerfilInteresPublic]:
    items = session.exec(select(PerfilInteres).where(PerfilInteres.IdPerfil == IdPerfil)).all()
    return [PerfilInteresPublic.model_validate(i) for i in items]

def LeerPorInteres(IdInteres: int, session: Session) -> list[PerfilInteresPublic]:
    items = session.exec(select(PerfilInteres).where(PerfilInteres.IdInteres == IdInteres)).all()
    return [PerfilInteresPublic.model_validate(i) for i in items]

def ActualizarPerfilInteres(IdPerfilInteres: int, datos: PerfilInteresUpdate, session: Session) -> PerfilInteresPublic:
    item = session.get(PerfilInteres, IdPerfilInteres)
    if not item:
        raise HTTPException(status_code=404, detail="Relación perfil-interés no encontrada")

    # si cambian las claves, validar FKs y unicidad
    update = datos.model_dump(exclude_unset=True)
    if "IdPerfil" in update and not session.get(Perfil, update["IdPerfil"]):
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    if "IdInteres" in update and not session.get(Intereses, update["IdInteres"]):
        raise HTTPException(status_code=404, detail="Interés no encontrado")

    # verificar duplicidad del par final
    IdPerfil_final = update.get("IdPerfil", item.IdPerfil)
    IdInteres_final = update.get("IdInteres", item.IdInteres)
    existe_par = session.exec(
        select(PerfilInteres).where(
            PerfilInteres.IdPerfil == IdPerfil_final,
            PerfilInteres.IdInteres == IdInteres_final,
            PerfilInteres.IdPerfilInteres != IdPerfilInteres
        )
    ).first()
    if existe_par:
        raise HTTPException(status_code=409, detail="Ya existe esa combinación Perfil-Interés")

    item.sqlmodel_update(update)
    session.add(item)
    session.commit()
    session.refresh(item)
    return PerfilInteresPublic.model_validate(item)

def EliminarPerfilInteres(IdPerfilInteres: int, session: Session):
    item = session.get(PerfilInteres, IdPerfilInteres)
    if not item:
        raise HTTPException(status_code=404, detail="Relación perfil-interés no encontrada")
    session.delete(item)
    session.commit()
    return {"message": "Relación perfil-interés eliminada"}

# útil para borrar por par (sin conocer el IdPerfilInteres)
def EliminarPorPar(IdPerfil: int, IdInteres: int, session: Session):
    item = session.exec(
        select(PerfilInteres).where(
            PerfilInteres.IdPerfil == IdPerfil,
            PerfilInteres.IdInteres == IdInteres
        )
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="No existe esa combinación Perfil-Interés")
    session.delete(item)
    session.commit()
    return {"message": "Relación eliminada"}
