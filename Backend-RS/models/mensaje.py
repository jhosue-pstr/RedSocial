from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
import datetime
from sqlalchemy import Column, Text, DateTime

class MensajeBase(SQLModel):
    contenido: str
    Leido: bool = False

class Mensaje(MensajeBase, table=True):
    IdMensaje: Optional[int] = Field(default=None, primary_key=True)
    IdConversacion: int = Field(foreign_key="conversacion.IdConversacion")
    IdUsuario: int = Field(foreign_key="usuario.IdUsuario") 
    FechaEnvio: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow,
        sa_column=Column(DateTime(timezone=True))
    )
    conversacion: "Conversacion" = Relationship(back_populates="mensajes")
    usuario: "Usuario" = Relationship(back_populates="mensajes")

class MensajeCreate(MensajeBase):
    IdConversacion: int
    IdUsuario: int

class MensajePublic(MensajeBase):
    IdMensaje: int
    IdConversacion: int
    IdUsuario: int
    FechaEnvio: datetime.datetime
    usuario: Optional["UsuarioPublic"] = None
    conversacion:Optional["ConversacionPublic"] = None


class MensajeUpdate(SQLModel):
    contenido: Optional[str] = None
    Leido: Optional[bool] = None



from models.conversacion import ConversacionPublic
from models.usuario import UsuarioPublic
MensajePublic.model_rebuild()        