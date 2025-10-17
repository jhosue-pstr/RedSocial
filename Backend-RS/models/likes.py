from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
import datetime
from sqlalchemy import UniqueConstraint  # para la clave única

class LikesBase(SQLModel):
    Fecha: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class Likes(LikesBase, table=True):
    __table_args__ = (
        UniqueConstraint("IdPublicacion", "IdUsuario", name="uq_like_pub_user"),
    )

    IdLike: Optional[int] = Field(default=None, primary_key=True)
    IdPublicacion: int = Field(foreign_key="publicaciones.IdPublicacion")
    IdUsuario: int = Field(foreign_key="usuario.IdUsuario")

    publicacion: "Publicaciones" = Relationship(back_populates="likes")
    usuario: "Usuario" = Relationship(back_populates="likes_hechos")

class LikesCreate(SQLModel):
    IdPublicacion: int  # el usuario lo tomaremos del token

class LikesPublic(LikesBase):
    IdLike: int
    IdPublicacion: int
    IdUsuario: int

class LikesUpdate(LikesBase):
    pass

LikesPublic.model_rebuild()
