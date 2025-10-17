from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
import datetime
from models.publicaciones import Publicaciones  # Asegúrate de importar el modelo Usuario
from config.database import get_session

class ArchivosPublicacionesBase(SQLModel):
    UrlArchivo: str
    TipoArchivo: str
    SubidoHace: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class ArchivosPublicaciones(ArchivosPublicacionesBase, table=True):
    IdArchivo: Optional[int] = Field(default=None, primary_key=True)
    IdPublicacion: int = Field(foreign_key="publicaciones.IdPublicacion")

    publicacion: "Publicaciones" = Relationship(back_populates="archivos_publicaciones")

class ArchivosPublicacionesCreate(ArchivosPublicacionesBase):
    pass

class ArchivosPublicacionesPublic(ArchivosPublicacionesBase):
    IdArchivo: int
    IdPublicacion: int

class ArchivosPublicacionesUpdate(ArchivosPublicacionesBase):
    pass

ArchivosPublicacionesPublic.model_rebuild()
