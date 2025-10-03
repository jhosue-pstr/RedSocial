from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Session, select
from config.database import get_session
from models.archivo_mensaje import (
    ArchivoMensaje,
    ArchivoMensajeCreate,
    ArchivoMensajeUpdate,
    ArchivoMensajePublic,
)
from models.mensaje import Mensaje, MensajePublic


SessionDep = Annotated[Session, Depends(get_session)]


def CrearArchivoMensaje(archivomensaje: ArchivoMensajeCreate, session: Session) -> ArchivoMensajePublic:
    nuevo_archivomensaje = ArchivoMensaje.model_validate(archivomensaje)
    session.add(nuevo_archivomensaje)
    session.commit()
    session.refresh(nuevo_archivomensaje)
    return ArchivoMensajePublic.model_validate(nuevo_archivomensaje)


def LeerArchivoMensaje(
    session: Session,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[ArchivoMensajePublic]:
    archivosmensajes = session.exec(
        select(ArchivoMensaje).offset(offset).limit(limit)
    ).all()

    resultados = []
    for archivo in archivosmensajes:
        archivo_public = ArchivoMensajePublic.model_validate(archivo)

        # Si quieres traer info del Mensaje relacionado
        if archivo.IdMensaje:
            mensaje = session.get(Mensaje, archivo.IdMensaje)
            if mensaje:
                archivo_public.mensaje = MensajePublic.model_validate(mensaje)

        resultados.append(archivo_public)

    return resultados


def LeerArchivoMensajePorId(IdArchivo: int, session: Session) -> ArchivoMensajePublic:
    archivo = session.get(ArchivoMensaje, IdArchivo)
    if not archivo:
        raise HTTPException(status_code=404, detail="Archivo de mensaje no encontrado")

    archivo_public = ArchivoMensajePublic.model_validate(archivo)

    if archivo.IdMensaje:
        mensaje = session.get(Mensaje, archivo.IdMensaje)
        if mensaje:
            archivo_public.mensaje = MensajePublic.model_validate(mensaje)

    return archivo_public


def ActualizarArchivoMensaje(
    IdArchivo: int, datos: ArchivoMensajeUpdate, session: Session
) -> ArchivoMensajePublic:
    archivo_db = session.get(ArchivoMensaje, IdArchivo)
    if not archivo_db:
        raise HTTPException(status_code=404, detail="Archivo de mensaje no encontrado")

    update_data = datos.model_dump(exclude_unset=True)
    archivo_db.sqlmodel_update(update_data)

    session.add(archivo_db)
    session.commit()
    session.refresh(archivo_db)

    archivo_public = ArchivoMensajePublic.model_validate(archivo_db)

    if archivo_db.IdMensaje:
        mensaje = session.get(Mensaje, archivo_db.IdMensaje)
        if mensaje:
            archivo_public.mensaje = MensajePublic.model_validate(mensaje)

    return archivo_public


def EliminarArchivoMensaje(IdArchivo: int, session: Session):
    archivo = session.get(ArchivoMensaje, IdArchivo)
    if not archivo:
        raise HTTPException(status_code=404, detail="Archivo de mensaje no encontrado")
    session.delete(archivo)
    session.commit()
    return {"message": "Archivo de mensaje eliminado"}
