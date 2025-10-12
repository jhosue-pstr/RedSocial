# routers/menciones_usuario.py
from fastapi import APIRouter, Depends
from sqlmodel import Session
from config.database import get_session
from models.menciones_usuario import (
    MencionesUsuarioCreate, MencionesUsuarioPublic, MencionesUsuarioUpdate
)
from controlers.menciones_usuario import (
    CrearMencion, LeerMencionPorId, LeerMenciones,
    LeerMencionesPorPublicacion, LeerMencionesPorUsuario,
    ActualizarMencion, EliminarMencion
)
from routers.auth import get_current_active_user
from models.usuario import Usuario
from models.menciones_usuario import MencionesUsuario

router = APIRouter()

# Listar todas las menciones
@router.get("/menciones_usuario", response_model=list[MencionesUsuarioPublic])
def ObtenerMenciones(
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerMenciones(session)

# Listar menciones por publicación
@router.get("/menciones_usuario/publicacion/{IdPublicacion}", response_model=list[MencionesUsuarioPublic])
def ObtenerMencionesDePublicacion(
    IdPublicacion: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerMencionesPorPublicacion(IdPublicacion, session)

# Listar menciones por usuario (mencionado)
@router.get("/menciones_usuario/usuario/{IdUsuario}", response_model=list[MencionesUsuarioPublic])
def ObtenerMencionesDeUsuario(
    IdUsuario: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerMencionesPorUsuario(IdUsuario, session)

# Obtener una mención por IdMencion
@router.get("/menciones_usuario/{IdMencion}", response_model=MencionesUsuarioPublic)
def ObtenerMencion(
    IdMencion: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return LeerMencionPorId(IdMencion, session)

# Crear mención (recibe IdPublicacion e IdUsuario en el body)
@router.post("/menciones_usuario", response_model=MencionesUsuarioPublic)
def CrearMencionRuta(
    data: MencionesUsuarioCreate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return CrearMencion(data, session)

# Actualizar mención (normalmente solo Fecha)
@router.patch("/menciones_usuario/{IdMencion}", response_model=MencionesUsuarioPublic)
def ActualizarMencionRuta(
    IdMencion: int,
    datos: MencionesUsuarioUpdate,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return ActualizarMencion(IdMencion, datos, session)

# Eliminar mención
@router.delete("/menciones_usuario/{IdMencion}")
def EliminarMencionRuta(
    IdMencion: int,
    session: Session = Depends(get_session),
    current_user: Usuario = Depends(get_current_active_user)
):
    return EliminarMencion(IdMencion, session)
