from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from routers.auth import get_current_active_user
from models.usuario import Usuario
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
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerArchivoMensaje(session, offset=offset, limit=limit)

@router.post("/archivosmensajes/", response_model=ArchivoMensajePublic)
def Agregar_ArchivoMensaje(
    archivomensaje: ArchivoMensajeCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearArchivoMensaje(archivomensaje, session)

@router.get("/archivosmensajes/{IdArchivo}", response_model=ArchivoMensajePublic)
def Obtener_ArchivoMensaje_Por_Id(
    IdArchivo: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerArchivoMensajePorId(IdArchivo, session)

@router.patch("/archivosmensajes/{IdArchivo}", response_model=ArchivoMensajePublic)
def Actualizar_ArchivoMensaje(
    IdArchivo: int,
    datos: ArchivoMensajeUpdate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarArchivoMensaje(IdArchivo, datos, session)

@router.delete("/archivosmensajes/{IdArchivo}")
def Eliminar_ArchivoMensaje(
    IdArchivo: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarArchivoMensaje(IdArchivo, session)