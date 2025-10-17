from fastapi import HTTPException
from sqlmodel import Session, select
from models.intereses import Intereses, InteresCreate, InteresPublic, InteresUpdate

def CrearInteres(data: InteresCreate, session: Session) -> InteresPublic:
    # (opcional) validar duplicado por nombre
    existente = session.exec(select(Intereses).where(Intereses.Nombre == data.Nombre)).first()
    if existente:
        raise HTTPException(status_code=409, detail="El interés ya existe")

    nuevo = Intereses(Nombre=data.Nombre)
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return InteresPublic.model_validate(nuevo)

def LeerInteresPorId(IdInteres: int, session: Session) -> InteresPublic:
    item = session.get(Intereses, IdInteres)
    if not item:
        raise HTTPException(status_code=404, detail="Interés no encontrado")
    return InteresPublic.model_validate(item)

def LeerIntereses(session: Session) -> list[InteresPublic]:
    items = session.exec(select(Intereses)).all()
    return [InteresPublic.model_validate(i) for i in items]

def ActualizarInteres(IdInteres: int, datos: InteresUpdate, session: Session) -> InteresPublic:
    item_db = session.get(Intereses, IdInteres)
    if not item_db:
        raise HTTPException(status_code=404, detail="Interés no encontrado")

    update_data = datos.model_dump(exclude_unset=True)
    item_db.sqlmodel_update(update_data)
    session.add(item_db)
    session.commit()
    session.refresh(item_db)
    return InteresPublic.model_validate(item_db)

def EliminarInteres(IdInteres: int, session: Session):
    item = session.get(Intereses, IdInteres)
    if not item:
        raise HTTPException(status_code=404, detail="Interés no encontrado")
    session.delete(item)
    session.commit()
    return {"message": "Interés eliminado"}
