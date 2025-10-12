from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from sqlalchemy import UniqueConstraint
from config.database import get_session

class PerfilInteresBase(SQLModel):
    IdPerfil: int
    IdInteres: int
class PerfilInteres(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("IdPerfil", "IdInteres", name="uq_perfil_interes"),)

    IdPerfilInteres: Optional[int] = Field(default=None, primary_key=True)
    IdPerfil: int = Field(foreign_key="perfil.IdPerfil")
    IdInteres: int = Field(foreign_key="intereses.IdInteres")

    perfil: "Perfil" = Relationship(back_populates="intereses_rel")
    interes: "Intereses" = Relationship(back_populates="perfiles_rel")
class PerfilInteresCreate(PerfilInteresBase):
    pass

class PerfilInteresPublic(PerfilInteresBase):
    IdPerfilInteres: int

class PerfilInteresUpdate(PerfilInteresBase):
    pass

PerfilInteresPublic.model_rebuild()
