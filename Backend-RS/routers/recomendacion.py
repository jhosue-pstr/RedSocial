from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.recomendacion import RecomendacionCreate, RecomendacionPublic, RecomendacionUpdate
from controlers.recomendacion import (
    CrearRecomendacion, LeerRecomendaciones, LeerRecomendacionPorId, LeerRecomendacionesPorUsuario, 
    ActualizarRecomendacion, EliminarRecomendacion
)
from routers.auth import get_current_active_user
from models.usuario import Usuario

router = APIRouter()

# Ruta para crear una recomendación
@router.post("/recomendaciones", response_model=RecomendacionPublic)
def CrearRecomendacionUsuario(
    recomendacion: RecomendacionCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearRecomendacion(recomendacion, session, current_user.IdUsuario)

# Ruta para obtener todas las recomendaciones
@router.get("/recomendaciones", response_model=list[RecomendacionPublic])
def ObtenerRecomendaciones(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerRecomendaciones(session)

# Ruta para obtener una recomendación por IdRecomendacion
@router.get("/recomendaciones/{IdRecomendacion}", response_model=RecomendacionPublic)
def ObtenerRecomendacionPorId(
    IdRecomendacion: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerRecomendacionPorId(IdRecomendacion, session)

# Ruta para obtener todas las recomendaciones de un usuario
@router.get("/recomendaciones/usuario/{IdUsuario}", response_model=list[RecomendacionPublic])
def ObtenerRecomendacionesDeUsuario(
    IdUsuario: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerRecomendacionesPorUsuario(IdUsuario, session)

# Ruta para actualizar una recomendación
@router.patch("/recomendaciones/{IdRecomendacion}", response_model=RecomendacionPublic)
def ActualizarRecomendacionUsuario(
    IdRecomendacion: int, 
    datos: RecomendacionUpdate, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarRecomendacion(IdRecomendacion, datos, session)

# Ruta para eliminar una recomendación
@router.delete("/recomendaciones/{IdRecomendacion}")
def EliminarRecomendacionUsuario(
    IdRecomendacion: int, 
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarRecomendacion(IdRecomendacion, session)
