from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
import datetime
from pydantic import BaseModel


class UsuarioBase(SQLModel):
    Nombre: str
    Apellido: str
    Correo: str = Field(unique=True, index=True)  # Agregar unique para login


class Usuario(UsuarioBase, table=True):
    IdUsuario: Optional[int] = Field(default=None, primary_key=True)
    Contrasena: str
    FechaRegistro: datetime.date = Field(default_factory=datetime.datetime.utcnow)
    estado: bool = True
    mensajes: List["Mensaje"] = Relationship(back_populates="usuario")
    participaciones: list["ParticipanteConversacion"] = Relationship(back_populates="usuario")
    perfil: "Perfil" = Relationship(back_populates="usuario")  
    menciones_recibidas: List["MencionesUsuario"] = Relationship(back_populates="usuario")
    likes_hechos: List["Likes"] = Relationship(back_populates="usuario")
    comentarios_rel: List["Comentario"] = Relationship(back_populates="usuario")

    amistades: List["Amistades"] = Relationship(back_populates="usuario")

class UsuarioCreate(UsuarioBase):
    Contrasena: str


class UsuarioPublic(UsuarioBase):
    IdUsuario: int
    FechaRegistro: datetime.date
    estado: bool


class UsuarioUpdate(SQLModel):
    Nombre: Optional[str] = None
    Apellido: Optional[str] = None
    Correo: Optional[str] = None
    Contrasena: Optional[str] = None
    estado: Optional[bool] = None


# Modelos para autenticación
class Token(BaseModel):
    access_token: str
    token_type: str
    user: UsuarioPublic  # Incluir datos del usuario en la respuesta


class TokenData(BaseModel):
    username: Optional[str] = None


class UserLogin(BaseModel):
    Correo: str  # Usaremos el correo como username
    Contrasena: str