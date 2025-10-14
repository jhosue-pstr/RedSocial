# routers/amistades.py
from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.amistades import AmistadCreate, AmistadPublic, AmistadUpdate
from controlers.amistades import (
    CrearAmistad, LeerAmistadPorId, LeerAmistades, LeerAmistadesPorUsuario,
    ActualizarAmistad, EliminarAmistad
)
from routers.auth import get_current_active_user
from models.usuario import Usuario

router = APIRouter()

# Listar todas
@router.get("/amistades", response_model=list[AmistadPublic])
def ObtenerAmistades(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerAmistades(session)

# Listar por usuario
@router.get("/amistades/usuario/{IdUsuario}", response_model=list[AmistadPublic])
def ObtenerAmistadesDeUsuario(
    IdUsuario: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerAmistadesPorUsuario(IdUsuario, session)

# Obtener por IdAmistad
@router.get("/amistades/{IdAmistad}", response_model=AmistadPublic)
def ObtenerAmistad(
    IdAmistad: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerAmistadPorId(IdAmistad, session)

# Crear
@router.post("/amistades", response_model=AmistadPublic)
def CrearAmistadUsuario(
    data: AmistadCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    # Si prefieres forzar que siempre sea del usuario autenticado:
    # data.IdUsuario = current_user.IdUsuario
    return CrearAmistad(data, session)

# Actualizar
@router.patch("/amistades/{IdAmistad}", response_model=AmistadPublic)
def ActualizarAmistadUsuario(
    IdAmistad: int,
    datos: AmistadUpdate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarAmistad(IdAmistad, datos, session)

# Eliminar
@router.delete("/amistades/{IdAmistad}")
def EliminarAmistadUsuario(
    IdAmistad: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarAmistad(IdAmistad, session)
