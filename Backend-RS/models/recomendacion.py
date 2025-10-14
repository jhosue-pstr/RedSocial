from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
import datetime
from models.usuario import Usuario  # Asegúrate de tener el modelo Usuario

# Base para las recomendaciones
class RecomendacionBase(SQLModel):
    Motivo: str
    Fecha: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

# Modelo (tabla) para la recomendación
class Recomendacion(RecomendacionBase, table=True):
    IdRecomendacion: Optional[int] = Field(default=None, primary_key=True)
    IdUsuario: int = Field(foreign_key="usuario.IdUsuario")  # Relación con el usuario

    # Relación con Usuario
    usuario: "Usuario" = Relationship(back_populates="recomendaciones")

# Modelos de entrada y salida
class RecomendacionCreate(RecomendacionBase):
    pass

class RecomendacionPublic(RecomendacionBase):
    IdRecomendacion: int
    IdUsuario: int

class RecomendacionUpdate(RecomendacionBase):
    pass

RecomendacionPublic.model_rebuild()
