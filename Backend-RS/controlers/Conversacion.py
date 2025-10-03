from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Session, select
from config.database import get_session
from models.conversacion import Conversacion, ConversacionCreate, ConversacionPublic, ConversacionUpdate


SessionDep = Annotated[Session,Depends(get_session)]

def CrearConversacion(conversacion: ConversacionCreate, session:Session)->ConversacionPublic:
    nueva_conversacion = Conversacion.model_validate(conversacion)
    
    session.add(nueva_conversacion)
    session.commit()
    session.refresh(nueva_conversacion)
    return ConversacionPublic.model_validate(nueva_conversacion)


def LeerConversacion(
    session: Session,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[ConversacionPublic]:
    Conversaciones= session.exec(select(Conversacion).offset(offset).limit(limit)).all()
    return[ConversacionPublic.model_validate(u)for u in Conversaciones]

def LeerConversacionPorId(IdConversacion:int , session:Session)-> ConversacionPublic:
    conversacion = session.get(Conversacion , IdConversacion)
    if not conversacion:
        raise HTTPException(status_code=404, detail="Conversacion no encontrado")
    return ConversacionPublic.model_validate(Conversacion)

def ActualizarConversacion(IdConversacion:int ,datos:ConversacionUpdate,session:Session)->ConversacionPublic:
    conversacion_db=session.get(Conversacion,IdConversacion)
    if not conversacion_db:
        raise HTTPException(status_code=404, detail="Conversacion no encontrado")

    update_data=datos.model_dump(exclude_unset=True)
    conversacion_db.sqlmodel_update(update_data)

    session.add(conversacion_db)
    session.commit()
    session.refresh(conversacion_db)
    return ConversacionPublic.model_validate(conversacion_db)

def EliminarConversacion(IdConversacion:int,session:Session):
    conversacion = session.get(Conversacion,IdConversacion)
    if not conversacion:
        raise HTTPException(status_code=404, detail="Conversacion no encontrado")
    session.delete(conversacion)
    session.commit()
    return{"message":"Conversacion Eliminada"}






from typing import Annotated

