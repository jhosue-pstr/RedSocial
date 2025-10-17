from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from models.perfil import Perfil  # Asegúrate de importar el modelo Usuario
from config.database import get_session

import datetime

# Base para la tabla EnlacesPerfil
class EnlacesPerfilBase(SQLModel):
    Tipo: str
    Url: str
    FechaAgregado: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

# Modelo de EnlacesPerfil (tabla en la base de datos)
class EnlacesPerfil(EnlacesPerfilBase, table=True):
    IdEnlace: Optional[int] = Field(default=None, primary_key=True)
    IdPerfil: int = Field(foreign_key="perfil.IdPerfil")  # Relación con Perfil

    perfil: "Perfil" = Relationship(back_populates="enlaces_perfil")  # Relación inversa

# Modelos para crear y mostrar enlaces
class EnlacesPerfilCreate(EnlacesPerfilBase):
    pass

class EnlacesPerfilPublic(EnlacesPerfilBase):
    IdEnlace: int
    IdPerfil: int

class EnlacesPerfilUpdate(EnlacesPerfilBase):
    pass


from models.perfil import PerfilPublic
EnlacesPerfilPublic.model_rebuild()