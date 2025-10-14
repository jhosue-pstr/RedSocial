# models/amistades.py
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
import datetime
from models.usuario import Usuario  # Asegúrate de importar el modelo Usuario
from config.database import get_session

class AmistadesBase(SQLModel):
    Estado: str                              # "pendiente", "aceptada", "rechazada", etc.
    FechaSolicitud: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    FechaAceptacion: Optional[datetime.datetime] = None

class Amistades(AmistadesBase, table=True):
    IdAmistad: Optional[int] = Field(default=None, primary_key=True)
    IdUsuario: int = Field(foreign_key="usuario.IdUsuario")

    # relación simple: una amistad pertenece a un usuario
    usuario: "Usuario" = Relationship(back_populates="amistades")

class AmistadCreate(AmistadesBase):
    # Un solo FK
    IdUsuario: int

class AmistadPublic(AmistadesBase):
    IdAmistad: int
    IdUsuario: int

# Para actualizaciones parciales
class AmistadUpdate(SQLModel):
    Estado: Optional[str] = None
    FechaAceptacion: Optional[datetime.datetime] = None

AmistadPublic.model_rebuild()
