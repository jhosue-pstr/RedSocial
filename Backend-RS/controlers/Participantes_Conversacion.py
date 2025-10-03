from typing import Annotated
from fastapi import Depends, HTTPException, Query
from sqlmodel import Session, select
from config.database import get_session

from models.participante_conversacion import (
    ParticipanteConversacion,
    ParticipanteConversacionCreate,
    ParticipanteConversacionPublic,
    ParticipanteConversacionUpdate
)
from models.usuario import Usuario, UsuarioPublic
from models.conversacion import Conversacion, ConversacionPublic

SessionDep = Annotated[Session, Depends(get_session)]


def CrearParticipante(
    participante: ParticipanteConversacionCreate,
    session: Session
) -> ParticipanteConversacionPublic:
    if not session.get(Usuario, participante.IdUsuario):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    if not session.get(Conversacion, participante.IdConversacion):
        raise HTTPException(status_code=404, detail="Conversación no encontrada")

    nuevo_participante = ParticipanteConversacion.model_validate(participante)
    session.add(nuevo_participante)

    try:
        session.commit()
    except Exception:
        session.rollback()
        raise HTTPException(
            status_code=400, detail="El usuario ya está en esta conversación"
        )

    session.refresh(nuevo_participante)
    return ParticipanteConversacionPublic.model_validate(nuevo_participante)


def LeerParticipantes(
    session: Session,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100
) -> list[ParticipanteConversacionPublic]:
    participantes = session.exec(
        select(ParticipanteConversacion).offset(offset).limit(limit)
    ).all()

    resultados = []
    for p in participantes:
        p_public = ParticipanteConversacionPublic.model_validate(p)

        if p.IdUsuario:
            usuario = session.get(Usuario, p.IdUsuario)
            if usuario:
                p_public.usuario = UsuarioPublic.model_validate(usuario)

        if p.IdConversacion:
            conversacion = session.get(Conversacion, p.IdConversacion)
            if conversacion:
                p_public.conversacion = ConversacionPublic.model_validate(conversacion)

        resultados.append(p_public)

    return resultados


def LeerParticipantePorId(IdParticipante: int, session: Session) -> ParticipanteConversacionPublic:
    participante = session.get(ParticipanteConversacion, IdParticipante)
    if not participante:
        raise HTTPException(status_code=404, detail="Participante no encontrado")

    participante_public = ParticipanteConversacionPublic.model_validate(participante)

    if participante.IdUsuario:
        usuario = session.get(Usuario, participante.IdUsuario)
        if usuario:
            participante_public.usuario = UsuarioPublic.model_validate(usuario)

    if participante.IdConversacion:
        conversacion = session.get(Conversacion, participante.IdConversacion)
        if conversacion:
            participante_public.conversacion = ConversacionPublic.model_validate(conversacion)

    return participante_public


def ActualizarParticipante(
    IdParticipante: int,
    datos: ParticipanteConversacionUpdate,
    session: Session
) -> ParticipanteConversacionPublic:
    participante_db = session.get(ParticipanteConversacion, IdParticipante)
    if not participante_db:
        raise HTTPException(status_code=404, detail="Participante no encontrado")

    update_data = datos.model_dump(exclude_unset=True)
    participante_db.sqlmodel_update(update_data)

    session.add(participante_db)
    session.commit()
    session.refresh(participante_db)

    return ParticipanteConversacionPublic.model_validate(participante_db)


def EliminarParticipante(IdParticipante: int, session: Session):
    participante = session.get(ParticipanteConversacion, IdParticipante)
    if not participante:
        raise HTTPException(status_code=404, detail="Participante no encontrado")

    session.delete(participante)
    session.commit()
    return {"message": "Participante eliminado correctamente"}
