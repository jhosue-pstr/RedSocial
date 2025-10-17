from sqlmodel import Field, SQLModel, Relationship   # ← añade Relationship
from typing import Optional, List                    # ← añade List
import datetime

class HashtagBase(SQLModel):
    Nombre: str = Field(unique=True, index=True)
    FechaCreacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class Hashtags(HashtagBase, table=True):
    IdHashtag: Optional[int] = Field(default=None, primary_key=True)

    # relación inversa hacia el link-model (forward ref con string)
    publicaciones_rel: List["PublicacionHashtag"] = Relationship(back_populates="hashtag")

class HashtagCreate(HashtagBase):
    pass

class HashtagPublic(HashtagBase):
    IdHashtag: int

class HashtagUpdate(HashtagBase):
    pass

HashtagPublic.model_rebuild()
