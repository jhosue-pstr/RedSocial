from sqlmodel import Field, SQLModel, Relationship

from typing import List
from typing import Optional
import datetime
from models.usuario import Usuario  # Asegúrate de importar el modelo Usuario
from config.database import get_session

# Base de datos para el Perfil
class PerfilBase(SQLModel):
    Descripcion: Optional[str] = None
    FotoPerfil: Optional[str] = None
    FotoPortada: Optional[str] = None
    Pronombres: Optional[str] = None
    FechaNacimiento: Optional[datetime.date] = None
    Genero: Optional[str] = None
    OrientacionSexual: Optional[str] = None
    Direccion: Optional[str] = None
    Ciudad: Optional[str] = None
    Pais: Optional[str] = None
    Telefono: Optional[str] = None
    Estudios: Optional[str] = None
    Ocupacion: Optional[str] = None
    EstadoRelacion: Optional[str] = None
    Biografia: Optional[str] = None
    SitioWeb: Optional[str] = None

class Perfil(PerfilBase, table=True):
    IdPerfil: Optional[int] = Field(default=None, primary_key=True)
    FechaCreacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    UltimaActualizacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    IdUsuario: int = Field(foreign_key="usuario.IdUsuario")  # Relación con Usuario

    # Relación inversa: Un perfil pertenece a un usuario
    usuario: "Usuario" = Relationship(back_populates="perfil")
    enlaces_perfil: List["EnlacesPerfil"] = Relationship(back_populates="perfil")
    fotos_perfil: List["FotosPerfil"] = Relationship(back_populates="perfil")
    musica_perfil: List["MusicaPerfil"] = Relationship(back_populates="perfil")
    publicaciones: List["Publicaciones"] = Relationship(back_populates="perfil")

    

# Modelos de entrada/salida para el perfil
class PerfilCreate(PerfilBase):
    pass

class PerfilPublic(PerfilBase):
    IdPerfil: int
    FechaCreacion: datetime.datetime
    UltimaActualizacion: datetime.datetime
    IdUsuario: int

class PerfilUpdate(PerfilBase):
    pass


from models.usuario import UsuarioPublic
PerfilPublic.model_rebuild()