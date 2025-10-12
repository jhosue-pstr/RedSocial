from sqlmodel import Field, SQLModel
from typing import Optional
import datetime

class HashtagBase(SQLModel):
    Nombre: str = Field(unique=True, index=True)
    FechaCreacion: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class Hashtags(HashtagBase, table=True):
    IdHashtag: Optional[int] = Field(default=None, primary_key=True)

class HashtagCreate(HashtagBase):
    pass

class HashtagPublic(HashtagBase):
    IdHashtag: int

class HashtagUpdate(HashtagBase):
    pass

HashtagPublic.model_rebuild()
