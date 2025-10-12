from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from models.perfil import Perfil  # Asegúrate de importar el modelo Usuario
from config.database import get_session
import datetime

# Base para la tabla MusicaPerfil
class MusicaPerfilBase(SQLModel):
    Plataforma: str
    UrlCancion: str
    TituloCancion: str
    Artista: str
    FechaVinculacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

# Modelo (tabla)
class MusicaPerfil(MusicaPerfilBase, table=True):
    IdMusica: Optional[int] = Field(default=None, primary_key=True)
    IdPerfil: int = Field(foreign_key="perfil.IdPerfil")

    # relación inversa hacia Perfil
    perfil: "Perfil" = Relationship(back_populates="musica_perfil")

# I/O models
class MusicaPerfilCreate(MusicaPerfilBase):
    pass

class MusicaPerfilPublic(MusicaPerfilBase):
    IdMusica: int
    IdPerfil: int

class MusicaPerfilUpdate(MusicaPerfilBase):
    pass

MusicaPerfilPublic.model_rebuild()
