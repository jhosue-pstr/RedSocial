from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.perfil_interes import PerfilInteresCreate, PerfilInteresPublic, PerfilInteresUpdate
from controlers.perfil_interes import (
    CrearPerfilInteres, LeerPerfilInteresPorId, LeerPerfilIntereses,
    LeerPorPerfil, LeerPorInteres, ActualizarPerfilInteres,
    EliminarPerfilInteres, EliminarPorPar
)
from routers.auth import get_current_active_user
from models.usuario import Usuario

router = APIRouter()

# Listar todas las relaciones
@router.get("/perfil_interes", response_model=list[PerfilInteresPublic])
def ObtenerPerfilIntereses(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPerfilIntereses(session)

# Listar por perfil
@router.get("/perfil_interes/perfil/{IdPerfil}", response_model=list[PerfilInteresPublic])
def ObtenerPorPerfil(
    IdPerfil: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPorPerfil(IdPerfil, session)

# Listar por interés
@router.get("/perfil_interes/interes/{IdInteres}", response_model=list[PerfilInteresPublic])
def ObtenerPorInteres(
    IdInteres: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPorInteres(IdInteres, session)

# Obtener por IdPerfilInteres
@router.get("/perfil_interes/{IdPerfilInteres}", response_model=PerfilInteresPublic)
def ObtenerPerfilInteres(
    IdPerfilInteres: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerPerfilInteresPorId(IdPerfilInteres, session)

# Crear relación
@router.post("/perfil_interes", response_model=PerfilInteresPublic)
def CrearRelacion(
    data: PerfilInteresCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearPerfilInteres(data, session)

# Actualizar relación (cambiar IdPerfil/IdInteres)
@router.patch("/perfil_interes/{IdPerfilInteres}", response_model=PerfilInteresPublic)
def ActualizarRelacion(
    IdPerfilInteres: int,
    datos: PerfilInteresUpdate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarPerfilInteres(IdPerfilInteres, datos, session)

# Eliminar por IdPerfilInteres
@router.delete("/perfil_interes/{IdPerfilInteres}")
def EliminarRelacion(
    IdPerfilInteres: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarPerfilInteres(IdPerfilInteres, session)

# Eliminar por par (IdPerfil, IdInteres)
@router.delete("/perfil_interes/perfil/{IdPerfil}/interes/{IdInteres}")
def EliminarRelacionPorPar(
    IdPerfil: int,
    IdInteres: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarPorPar(IdPerfil, IdInteres, session)
