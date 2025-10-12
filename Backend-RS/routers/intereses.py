from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.intereses import InteresCreate, InteresPublic, InteresUpdate
from controlers.intereses import (
    CrearInteres, LeerInteresPorId, LeerIntereses, ActualizarInteres, EliminarInteres
)
from routers.auth import get_current_active_user
from models.usuario import Usuario

router = APIRouter()

# Listar todos los intereses
@router.get("/intereses", response_model=list[InteresPublic])
def ObtenerIntereses(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerIntereses(session)

# Obtener un interés por ID
@router.get("/intereses/{IdInteres}", response_model=InteresPublic)
def ObtenerInteres(
    IdInteres: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerInteresPorId(IdInteres, session)

# Crear un interés
@router.post("/intereses", response_model=InteresPublic)
def CrearInteresRuta(
    data: InteresCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearInteres(data, session)

# Actualizar un interés
@router.patch("/intereses/{IdInteres}", response_model=InteresPublic)
def ActualizarInteresRuta(
    IdInteres: int,
    datos: InteresUpdate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarInteres(IdInteres, datos, session)

# Eliminar un interés
@router.delete("/intereses/{IdInteres}")
def EliminarInteresRuta(
    IdInteres: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarInteres(IdInteres, session)
