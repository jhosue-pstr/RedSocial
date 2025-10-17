from fastapi import HTTPException
from sqlmodel import Session, select
from models.recomendacion import RecomendacionCreate, RecomendacionPublic, RecomendacionUpdate
from models.usuario import Usuario
from models.recomendacion import Recomendacion
import datetime

# Crear una recomendación
def CrearRecomendacion(data: RecomendacionCreate, session: Session, id_usuario: int) -> RecomendacionPublic:
    usuario_db = session.get(Usuario, id_usuario)
    
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    nueva_recomendacion = Recomendacion(
        Motivo=data.Motivo,
        IdUsuario=id_usuario,
        Fecha=datetime.datetime.utcnow()
    )
    
    session.add(nueva_recomendacion)
    session.commit()
    session.refresh(nueva_recomendacion)
    return RecomendacionPublic.model_validate(nueva_recomendacion)

# Leer todas las recomendaciones
def LeerRecomendaciones(session: Session) -> list[RecomendacionPublic]:
    recomendaciones = session.exec(select(Recomendacion)).all()
    return [RecomendacionPublic.model_validate(r) for r in recomendaciones]

# Leer una recomendación por IdRecomendacion
def LeerRecomendacionPorId(IdRecomendacion: int, session: Session) -> RecomendacionPublic:
    recomendacion = session.get(Recomendacion, IdRecomendacion)
    if not recomendacion:
        raise HTTPException(status_code=404, detail="Recomendación no encontrada")
    return RecomendacionPublic.model_validate(recomendacion)

# Leer todas las recomendaciones de un usuario
def LeerRecomendacionesPorUsuario(IdUsuario: int, session: Session) -> list[RecomendacionPublic]:
    recomendaciones = session.exec(select(Recomendacion).where(Recomendacion.IdUsuario == IdUsuario)).all()
    return [RecomendacionPublic.model_validate(r) for r in recomendaciones]

# Actualizar una recomendación
def ActualizarRecomendacion(IdRecomendacion: int, datos: RecomendacionUpdate, session: Session) -> RecomendacionPublic:
    recomendacion_db = session.get(Recomendacion, IdRecomendacion)
    if not recomendacion_db:
        raise HTTPException(status_code=404, detail="Recomendación no encontrada")

    update_data = datos.model_dump(exclude_unset=True)
    recomendacion_db.sqlmodel_update(update_data)

    session.add(recomendacion_db)
    session.commit()
    session.refresh(recomendacion_db)
    return RecomendacionPublic.model_validate(recomendacion_db)

# Eliminar una recomendación
def EliminarRecomendacion(IdRecomendacion: int, session: Session):
    recomendacion_db = session.get(Recomendacion, IdRecomendacion)
    if not recomendacion_db:
        raise HTTPException(status_code=404, detail="Recomendación no encontrada")
    
    session.delete(recomendacion_db)
    session.commit()
    return {"message": "Recomendación eliminada"}
