from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Session, select
from config.database import get_session
from models.mensaje import MensajeCreate,Mensaje,MensajePublic,MensajeUpdate
from models.conversacion import Conversacion,ConversacionPublic
from models.usuario import Usuario,UsuarioPublic




SessionDep = Annotated[Session, Depends(get_session)]

def CrearMensaje(mensaje:MensajeCreate,session :Session)->MensajePublic:
    nuevo_mensaje = Mensaje.model_validate(mensaje)
    session.add(nuevo_mensaje)
    session.commit()
    session.refresh(nuevo_mensaje)
    return MensajePublic.model_validate(nuevo_mensaje)

def LeerMensaje(session:Session,offset:int=0 ,limit :Annotated [int,Query(le=100)]=100)-> list[MensajePublic]:
    mensajes = session.exec(select(Mensaje).offset(offset).limit(limit)).all()
    
    resultados = []
    for mensaje in mensajes:
        mensaje_public = MensajePublic.model_validate(mensaje)

        if mensaje.IdConversacion:
            conversacion = session.get(Conversacion, mensaje.IdConversacion)
            if conversacion:
                mensaje_public.conversacion = ConversacionPublic.model_validate(conversacion)

        if mensaje.IdUsuario:
            usuario = session.get(Usuario , mensaje.IdConversacion)
            if usuario:
                mensaje_public.usuario =  UsuarioPublic.model_validate(usuario)

        resultados.append(mensaje_public)
    return resultados              


def LeerMensajePorId(IdMensaje:int , session:Session)-> MensajePublic:
    mensaje = session.get(Mensaje,IdMensaje)
    if not mensaje:
        raise HTTPException(status_code=404,detail="Inscripcion no encontrada")
    mensaje_public = MensajePublic.model_validate(mensaje)
    if mensaje.IdConversacion:
            conversacion = session.get(Conversacion, mensaje.IdConversacion)
            if conversacion:
                mensaje_public.conversacion = ConversacionPublic.model_validate(conversacion)

    if mensaje.IdUsuario:
            usuario = session.get(Usuario , mensaje.IdConversacion)
            if usuario:
                mensaje_public.usuario =  UsuarioPublic.model_validate(usuario)
    
    return mensaje_public            
        

def ActualizarMensaje(IdMensaje:int , datos:MensajeUpdate,session:Session)->MensajePublic:
    mensaje_db=session.get(MensajePublic)
    if not mensaje_db:
                raise HTTPException(status_code=404,detail="Mensaje no encontrada")
    update_mensaje = datos.model_dump(exclude_unset=True)
    mensaje_db.sqlmodel_update(update_mensaje)

    session.add(mensaje_db)
    session.commit()
    session.refresh(mensaje_db)
    mensaje_public = MensajePublic.model_validate(mensaje_db)
    if mensaje_db.IdConversacion:
            conversacion = session.get(Conversacion, mensaje_db.IdConversacion)
            if conversacion:
                mensaje_public.conversacion = ConversacionPublic.model_validate(conversacion)

    if mensaje_db.IdUsuario:
            usuario = session.get(Usuario , mensaje_db.IdConversacion)
            if usuario:
                mensaje_public.usuario =  UsuarioPublic.model_validate(usuario)
    return mensaje_public

def EliminarMensaje(IdMensaje:int , session:Session):
    mensaje = session.get(Mensaje,IdMensaje)
    if not mensaje:
        raise HTTPException(status_code=404,detail="Mensaje no encontrada")
    session.delete(mensaje)
    session.commit()
    return {"message":"Mensaje eliminada"}

          
