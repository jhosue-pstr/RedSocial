from sqlmodel import Field, SQLModel, Relationship, UniqueConstraint
from typing import Optional
import datetime


class ParticipanteConversacionBase(SQLModel):
    IdConversacion: int = Field(foreign_key="conversacion.IdConversacion")
    IdUsuario: int = Field(foreign_key="usuario.IdUsuario")


class ParticipanteConversacion(ParticipanteConversacionBase, table=True):
    __tablename__ = "participantes_conversacion"
    __table_args__ = (UniqueConstraint("IdConversacion", "IdUsuario"),) 

    IdParticipante: Optional[int] = Field(default=None, primary_key=True)
    UnidoHace: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

    conversacion: "Conversacion" = Relationship(back_populates="participantes")
    usuario: "Usuario" = Relationship(back_populates="participaciones")


class ParticipanteConversacionCreate(ParticipanteConversacionBase):
    pass


class ParticipanteConversacionPublic(ParticipanteConversacionBase):
    IdParticipante: int
    UnidoHace: datetime.datetime
    usuario: Optional["UsuarioPublic"] = None
    conversacion: Optional["ConversacionPublic"] = None


class ParticipanteConversacionUpdate(SQLModel):
    pass



from models.usuario import UsuarioPublic
from models.conversacion import ConversacionPublic

ParticipanteConversacionPublic.model_rebuild()
