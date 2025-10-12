from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
import datetime
from models.perfil import Perfil  # Asegúrate de importar el modelo Usuario
from config.database import get_session


class PublicacionesBase(SQLModel):
    Contenido: str
    FechaCreacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    Estado: bool = True
    Visibilidad: str  # p.ej: "publico", "amigos", "privado"

# Modelo (tabla)
class Publicaciones(PublicacionesBase, table=True):
    IdPublicacion: Optional[int] = Field(default=None, primary_key=True)
    IdPerfil: int = Field(foreign_key="perfil.IdPerfil")

    perfil: "Perfil" = Relationship(back_populates="publicaciones")
    archivos_publicaciones: List["ArchivosPublicaciones"] = Relationship(back_populates="publicacion")
    menciones_usuario: List["MencionesUsuario"] = Relationship(back_populates="publicacion")
    likes: List["Likes"] = Relationship(back_populates="publicacion")
    hashtags_rel: List["PublicacionHashtag"] = Relationship(back_populates="publicacion")

# I/O models
class PublicacionesCreate(PublicacionesBase):
    pass

class PublicacionesPublic(PublicacionesBase):
    IdPublicacion: int
    IdPerfil: int

class PublicacionesUpdate(PublicacionesBase):
    pass

PublicacionesPublic.model_rebuild()
