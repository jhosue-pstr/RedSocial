from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from sqlalchemy import UniqueConstraint

class PublicacionHashtagBase(SQLModel):
    # PON los foreign_key correctos:
    IdPublicacion: int = Field(foreign_key="publicaciones.IdPublicacion")
    IdHashtag: int = Field(foreign_key="hashtags.IdHashtag")

class PublicacionHashtag(PublicacionHashtagBase, table=True):
    __table_args__ = (
        UniqueConstraint("IdPublicacion", "IdHashtag", name="uq_publicacion_hashtag"),
    )

    IdPublicacionHashtag: Optional[int] = Field(default=None, primary_key=True)

    publicacion: "Publicaciones" = Relationship(back_populates="hashtags_rel")
    hashtag: "Hashtags" = Relationship(back_populates="publicaciones_rel")

class PublicacionHashtagCreate(PublicacionHashtagBase):
    pass

class PublicacionHashtagPublic(PublicacionHashtagBase):
    IdPublicacionHashtag: int

class PublicacionHashtagUpdate(PublicacionHashtagBase):
    pass

PublicacionHashtagPublic.model_rebuild()
