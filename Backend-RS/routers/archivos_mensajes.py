from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session

from models.archivo_mensaje import (
    ArchivoMensajeCreate,
    ArchivoMensajePublic,
    ArchivoMensajeUpdate
)
from controlers.Archivo_Mensaje import (
    LeerArchivoMensaje,
    LeerArchivoMensajePorId,
    CrearArchivoMensaje,
    ActualizarArchivoMensaje,
    EliminarArchivoMensaje
)

router = APIRouter()

@router.get("/archivosmensajes/", response_model=list[ArchivoMensajePublic])
def Obtener_ArchivosMensajes(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    return LeerArchivoMensaje(session, offset=offset, limit=limit)

@router.post("/archivosmensajes/", response_model=ArchivoMensajePublic)
def Agregar_ArchivoMensaje(
    archivomensaje: ArchivoMensajeCreate,
    session: Session = Depends(get_session)
):
    return CrearArchivoMensaje(archivomensaje, session)

@router.get("/archivosmensajes/{IdArchivo}", response_model=ArchivoMensajePublic)
def Obtener_ArchivoMensaje_Por_Id(
    IdArchivo: int,
    session: Session = Depends(get_session)
):
    return LeerArchivoMensajePorId(IdArchivo, session)

@router.patch("/archivosmensajes/{IdArchivo}", response_model=ArchivoMensajePublic)
def Actualizar_ArchivoMensaje(
    IdArchivo: int,
    datos: ArchivoMensajeUpdate,
    session: Session = Depends(get_session)
):
    return ActualizarArchivoMensaje(IdArchivo, datos, session)

@router.delete("/archivosmensajes/{IdArchivo}")
def Eliminar_ArchivoMensaje(
    IdArchivo: int,
    session: Session = Depends(get_session)
):
    return EliminarArchivoMensaje(IdArchivo, session)
