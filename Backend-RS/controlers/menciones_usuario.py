# controlers/menciones_usuario.py
from fastapi import HTTPException
from sqlmodel import Session, select
from models.menciones_usuario import (
    MencionesUsuario, MencionesUsuarioCreate, MencionesUsuarioPublic, MencionesUsuarioUpdate
)
from models.publicaciones import Publicaciones
from models.usuario import Usuario

def CrearMencion(data: MencionesUsuarioCreate, session: Session) -> MencionesUsuarioPublic:
    pub = session.get(Publicaciones, data.IdPublicacion)
    if not pub:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")

    user = session.get(Usuario, data.IdUsuario)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario mencionado no encontrado")

    nueva = MencionesUsuario(
        IdPublicacion=data.IdPublicacion,
        IdUsuario=data.IdUsuario,
        Fecha=data.Fecha
    )
    session.add(nueva)
    session.commit()
    session.refresh(nueva)
    return MencionesUsuarioPublic.model_validate(nueva)

def LeerMencionPorId(IdMencion: int, session: Session) -> MencionesUsuarioPublic:
    m = session.get(MencionesUsuario, IdMencion)
    if not m:
        raise HTTPException(status_code=404, detail="Mención no encontrada")
    return MencionesUsuarioPublic.model_validate(m)

def LeerMenciones(session: Session) -> list[MencionesUsuarioPublic]:
    items = session.exec(select(MencionesUsuario)).all()
    return [MencionesUsuarioPublic.model_validate(i) for i in items]

def LeerMencionesPorPublicacion(IdPublicacion: int, session: Session) -> list[MencionesUsuarioPublic]:
    items = session.exec(
        select(MencionesUsuario).where(MencionesUsuario.IdPublicacion == IdPublicacion)
    ).all()
    return [MencionesUsuarioPublic.model_validate(i) for i in items]

def LeerMencionesPorUsuario(IdUsuario: int, session: Session) -> list[MencionesUsuarioPublic]:
    items = session.exec(
        select(MencionesUsuario).where(MencionesUsuario.IdUsuario == IdUsuario)
    ).all()
    return [MencionesUsuarioPublic.model_validate(i) for i in items]

def ActualizarMencion(IdMencion: int, datos: MencionesUsuarioUpdate, session: Session) -> MencionesUsuarioPublic:
    m_db = session.get(MencionesUsuario, IdMencion)
    if not m_db:
        raise HTTPException(status_code=404, detail="Mención no encontrada")
    update_data = datos.model_dump(exclude_unset=True)
    m_db.sqlmodel_update(update_data)
    session.add(m_db)
    session.commit()
    session.refresh(m_db)
    return MencionesUsuarioPublic.model_validate(m_db)

def EliminarMencion(IdMencion: int, session: Session):
    m = session.get(MencionesUsuario, IdMencion)
    if not m:
        raise HTTPException(status_code=404, detail="Mención no encontrada")
    session.delete(m)
    session.commit()
    return {"message": "Mención eliminada"}
