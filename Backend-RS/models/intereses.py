from sqlmodel import Field, SQLModel, Relationship
from typing import List
from typing import Optional

from config.database import get_session
class InteresBase(SQLModel):
    Nombre: str = Field(index=True)  # si quieres hacerlo único: Field(index=True, unique=True)

class Intereses(InteresBase, table=True):
    IdInteres: Optional[int] = Field(default=None, primary_key=True)
    perfiles_rel: List["PerfilInteres"] = Relationship(back_populates="interes")

class InteresCreate(InteresBase):
    pass

class InteresPublic(InteresBase):
    IdInteres: int

class InteresUpdate(InteresBase):
    pass

InteresPublic.model_rebuild()
