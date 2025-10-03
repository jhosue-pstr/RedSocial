from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from controlers.Mensaje import *
from models.mensaje import MensajePublic,MensajeCreate,MensajeUpdate


router = APIRouter()


@router.get("/mensajes/",response_model=list[MensajePublic])
def ObtenerMensaje(
    session:Session = Depends(get_session),
    offset:int = 0 ,
    limit : int = 100,
):
    return LeerMensaje(session,offset=offset,limit=limit)

@router.post("/mensajes/",response_model = MensajePublic)
def Agregar_Mensaje(Mensaje:MensajeCreate,session:Session=Depends(get_session)):
    return CrearMensaje(Mensaje,session)

@router.get("/mensajes/{IdMensaje}",response_model=MensajePublic)
def Obtener_Mensaje_Por_Id(IdMensaje:int,session:Session=Depends(get_session)):
    return LeerMensajePorId(IdMensaje,session)

@router.patch("/mensajes/{IdMensaje}",response_model=MensajePublic)
def Actualizar_Mensaje(IdMensaje:int,datos:MensajeUpdate,session:Session=Depends(get_session)):
    return ActualizarMensaje(IdMensaje,datos,session)

@router.delete("/mensajes/{Idmensajes}")
def Eliminar_Mensaje(IdMensaje:int,session:Session=Depends(get_session)):
    return EliminarMensaje(IdMensaje,session)
