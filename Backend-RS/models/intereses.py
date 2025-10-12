from sqlmodel import Field, SQLModel
from typing import Optional

class InteresBase(SQLModel):
    Nombre: str = Field(index=True)  # si quieres hacerlo único: Field(index=True, unique=True)

class Intereses(InteresBase, table=True):
    IdInteres: Optional[int] = Field(default=None, primary_key=True)

class InteresCreate(InteresBase):
    pass

class InteresPublic(InteresBase):
    IdInteres: int

class InteresUpdate(InteresBase):
    pass

InteresPublic.model_rebuild()
