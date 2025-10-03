from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session

from models.participante_conversacion import (
    ParticipanteConversacionCreate,
    ParticipanteConversacionPublic,
    ParticipanteConversacionUpdate
)
from controlers.Participantes_Conversacion import (
    LeerParticipantes,
    LeerParticipantePorId,
    CrearParticipante,
    ActualizarParticipante,
    EliminarParticipante
)

router = APIRouter()

@router.get("/participantes/", response_model=list[ParticipanteConversacionPublic])
def Obtener_Participantes(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100
):
    return LeerParticipantes(session, offset=offset, limit=limit)


@router.post("/participantes/", response_model=ParticipanteConversacionPublic)
def Agregar_Participante(
    participante: ParticipanteConversacionCreate,
    session: Session = Depends(get_session)
):
    return CrearParticipante(participante, session)


@router.get("/participantes/{IdParticipante}", response_model=ParticipanteConversacionPublic)
def Obtener_Participante_Por_Id(
    IdParticipante: int,
    session: Session = Depends(get_session)
):
    return LeerParticipantePorId(IdParticipante, session)


@router.patch("/participantes/{IdParticipante}", response_model=ParticipanteConversacionPublic)
def Actualizar_Participante(
    IdParticipante: int,
    datos: ParticipanteConversacionUpdate,
    session: Session = Depends(get_session)
):
    return ActualizarParticipante(IdParticipante, datos, session)


@router.delete("/participantes/{IdParticipante}")
def Eliminar_Participante(
    IdParticipante: int,
    session: Session = Depends(get_session)
):
    return EliminarParticipante(IdParticipante, session)
