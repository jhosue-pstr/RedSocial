# models/menciones_usuario.py
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
import datetime
from models.publicaciones import Publicaciones  
from models.usuario import Usuario
from config.database import get_session

class MencionesUsuarioBase(SQLModel):
    Fecha: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class MencionesUsuario(MencionesUsuarioBase, table=True):
    IdMencion: Optional[int] = Field(default=None, primary_key=True)
    IdPublicacion: int = Field(foreign_key="publicaciones.IdPublicacion")
    IdUsuario: int = Field(foreign_key="usuario.IdUsuario")

    publicacion: "Publicaciones" = Relationship(back_populates="menciones_usuario")
    usuario: "Usuario" = Relationship(back_populates="menciones_recibidas")

class MencionesUsuarioCreate(MencionesUsuarioBase):
    IdPublicacion: int
    IdUsuario: int

class MencionesUsuarioPublic(MencionesUsuarioBase):
    IdMencion: int
    IdPublicacion: int
    IdUsuario: int

class MencionesUsuarioUpdate(MencionesUsuarioBase):
    pass

MencionesUsuarioPublic.model_rebuild()
