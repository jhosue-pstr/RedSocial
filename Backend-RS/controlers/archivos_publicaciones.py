from fastapi import HTTPException
from sqlmodel import Session, select
from models.archivos_publicaciones import (
    ArchivosPublicaciones, ArchivosPublicacionesCreate,
    ArchivosPublicacionesPublic, ArchivosPublicacionesUpdate
)
from models.publicaciones import Publicaciones
from config.database import get_session

# Crear archivo asociado a una publicación específica
def CrearArchivoPublicacion(
    data: ArchivosPublicacionesCreate,
    session: Session,
    id_publicacion: int
) -> ArchivosPublicacionesPublic:
    pub = session.get(Publicaciones, id_publicacion)
    if not pub:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")

    nuevo = ArchivosPublicaciones(
        UrlArchivo=data.UrlArchivo,
        TipoArchivo=data.TipoArchivo,
        SubidoHace=data.SubidoHace,
        IdPublicacion=id_publicacion,
    )
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return ArchivosPublicacionesPublic.model_validate(nuevo)

# Obtener por IdArchivo
def LeerArchivoPorId(IdArchivo: int, session: Session) -> ArchivosPublicacionesPublic:
    item = session.get(ArchivosPublicaciones, IdArchivo)
    if not item:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return ArchivosPublicacionesPublic.model_validate(item)

# Listar todos
def LeerArchivos(session: Session) -> list[ArchivosPublicacionesPublic]:
    items = session.exec(select(ArchivosPublicaciones)).all()
    return [ArchivosPublicacionesPublic.model_validate(i) for i in items]

# Listar por publicación
def LeerArchivosPorPublicacion(IdPublicacion: int, session: Session) -> list[ArchivosPublicacionesPublic]:
    items = session.exec(
        select(ArchivosPublicaciones).where(ArchivosPublicaciones.IdPublicacion == IdPublicacion)
    ).all()
    return [ArchivosPublicacionesPublic.model_validate(i) for i in items]

# Actualizar por IdArchivo
def ActualizarArchivo(IdArchivo: int, datos: ArchivosPublicacionesUpdate, session: Session) -> ArchivosPublicacionesPublic:
    item_db = session.get(ArchivosPublicaciones, IdArchivo)
    if not item_db:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    update_data = datos.model_dump(exclude_unset=True)
    item_db.sqlmodel_update(update_data)
    session.add(item_db)
    session.commit()
    session.refresh(item_db)
    return ArchivosPublicacionesPublic.model_validate(item_db)

# Eliminar por IdArchivo
def EliminarArchivo(IdArchivo: int, session: Session):
    item = session.get(ArchivosPublicaciones, IdArchivo)
    if not item:
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    session.delete(item)
    session.commit()
    return {"message": "Archivo eliminado"}
