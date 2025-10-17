from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
import datetime
from models.publicaciones import Publicaciones
from models.usuario import Usuario

# Base para los comentarios
class ComentariosBase(SQLModel):
    Contenido: str
    Fecha: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    Estado: bool = True

# Modelo (tabla) para comentarios
class Comentario(ComentariosBase, table=True):
    IdComentario: Optional[int] = Field(default=None, primary_key=True)
    IdPublicacion: int = Field(foreign_key="publicaciones.IdPublicacion")
    IdUsuario: int = Field(foreign_key="usuario.IdUsuario")

    # Relaciones
    publicacion: "Publicaciones" = Relationship(back_populates="comentarios_rel")
    usuario: "Usuario" = Relationship(back_populates="comentarios_rel")

# Modelos de entrada y salida
class ComentarioCreate(ComentariosBase):
    pass

class ComentarioPublic(ComentariosBase):
    IdComentario: int
    IdPublicacion: int
    IdUsuario: int

class ComentarioUpdate(ComentariosBase):
    pass

ComentarioPublic.model_rebuild()
