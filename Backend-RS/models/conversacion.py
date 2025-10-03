from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
import datetime

class ConversacionBase(SQLModel):
    EsConversacion: bool
    Nombre: str

class Conversacion(ConversacionBase, table=True):
    IdConversacion: Optional[int] = Field(default=None, primary_key=True)
    FechaCreacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    estado: bool = True
    mensajes: List["Mensaje"] = Relationship(back_populates="conversacion")
    participantes: list["ParticipanteConversacion"] = Relationship(back_populates="conversacion")

class ConversacionCreate(ConversacionBase):
    pass

class ConversacionPublic(ConversacionBase):
    IdConversacion: int
    FechaCreacion: datetime.datetime
    estado: bool

class ConversacionUpdate(SQLModel):
    EsConversacion: Optional[bool] = None
    Nombre: Optional[str] = None
    estado: Optional[bool] = None