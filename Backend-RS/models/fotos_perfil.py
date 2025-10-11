from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from models.perfil import Perfil  # Asegúrate de importar el modelo Usuario
from config.database import get_session

import datetime
from models.perfil import Perfil  # Asegúrate de importar el modelo Perfil

# Base de datos para el FotosPerfil
class FotosPerfilBase(SQLModel):
    UrlFoto: str
    Tipo: str
    Descripcion: Optional[str] = None
    FechaSubida: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    Estado: bool = True

# Modelo de FotosPerfil (tabla en la base de datos)
class FotosPerfil(FotosPerfilBase, table=True):
    IdFoto: Optional[int] = Field(default=None, primary_key=True)
    IdPerfil: int = Field(foreign_key="perfil.IdPerfil")  # Relación con Perfil

    perfil: "Perfil" = Relationship(back_populates="fotos_perfil")

# Modelos de entrada/salida para el fotos_perfil
class FotosPerfilCreate(FotosPerfilBase):
    pass

class FotosPerfilPublic(FotosPerfilBase):
    IdFoto: int
    IdPerfil: int

class FotosPerfilUpdate(FotosPerfilBase):
    pass



from models.perfil import PerfilPublic
FotosPerfilPublic.model_rebuild()
