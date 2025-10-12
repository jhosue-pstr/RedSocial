from fastapi import HTTPException
from sqlmodel import Session, select
from config.database import get_session
from models.publicaciones import (Publicaciones, PublicacionesCreate, PublicacionesPublic, PublicacionesUpdate)
from models.perfil import Perfil

# Crear publicación asociada al perfil del usuario autenticado
def CrearPublicacion(data: PublicacionesCreate, session: Session, id_usuario: int) -> PublicacionesPublic:
    perfil_db = session.exec(select(Perfil).where(Perfil.IdUsuario == id_usuario)).first()
    if not perfil_db:
        raise HTTPException(status_code=404, detail="Perfil no encontrado para el usuario")

    nueva = Publicaciones(
        Contenido=data.Contenido,
        Estado=data.Estado,
        Visibilidad=data.Visibilidad,
        IdPerfil=perfil_db.IdPerfil,
    )
    session.add(nueva)
    session.commit()
    session.refresh(nueva)
    return PublicacionesPublic.model_validate(nueva)

# Leer por IdPublicacion
def LeerPublicacionPorId(IdPublicacion: int, session: Session) -> PublicacionesPublic:
    pub = session.get(Publicaciones, IdPublicacion)
    if not pub:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return PublicacionesPublic.model_validate(pub)

# Listar todas
def LeerPublicaciones(session: Session) -> list[PublicacionesPublic]:
    pubs = session.exec(select(Publicaciones)).all()
    return [PublicacionesPublic.model_validate(p) for p in pubs]

# Actualizar por IdPublicacion
def ActualizarPublicacion(IdPublicacion: int, datos: PublicacionesUpdate, session: Session) -> PublicacionesPublic:
    pub_db = session.get(Publicaciones, IdPublicacion)
    if not pub_db:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")

    update_data = datos.model_dump(exclude_unset=True)
    pub_db.sqlmodel_update(update_data)

    session.add(pub_db)
    session.commit()
    session.refresh(pub_db)
    return PublicacionesPublic.model_validate(pub_db)

# Eliminar por IdPublicacion
def EliminarPublicacion(IdPublicacion: int, session: Session):
    pub = session.get(Publicaciones, IdPublicacion)
    if not pub:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    session.delete(pub)
    session.commit()
    return {"message": "Publicación eliminada"}
