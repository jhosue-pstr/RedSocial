from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from routers.auth import get_current_active_user
from models.usuario import Usuario
from models.conversacion import ConversacionCreate,ConversacionPublic,ConversacionUpdate
from controlers.Conversacion import (
    LeerConversacion,LeerConversacionPorId,CrearConversacion,ActualizarConversacion,EliminarConversacion
)

router = APIRouter()

@router.get("/conversaciones/",response_model=list[ConversacionPublic])
def ObtenerConversacion(
    session:Session = Depends(get_session),
    offset:int = 0 ,
    limit : int = 100,
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerConversacion(session,offset=offset,limit=limit)

@router.post("/conversaciones/",response_model = ConversacionPublic)
def Agregar_Conversacion(
    conversacion:ConversacionCreate,
    session:Session=Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearConversacion(conversacion,session)

@router.get("/conversaciones/{IdConversacion}",response_model=ConversacionPublic)
def Obtener_Conversacion_Por_Id(
    IdConversacion:int,
    session:Session=Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerConversacionPorId(IdConversacion,session)

@router.patch("/conversaciones/{IdConversacion}",response_model=ConversacionPublic)
def Actualizar_Conversacion(
    IdConversacion:int,
    datos:ConversacionUpdate,
    session:Session=Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarConversacion(IdConversacion,datos,session)

@router.delete("/conversaciones/{IdConversaciones}")
def Eliminar_Conversacion(
    IdConversacion:int,
    session:Session=Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarConversacion(IdConversacion,session)