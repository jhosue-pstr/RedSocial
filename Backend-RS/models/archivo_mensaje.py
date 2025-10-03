from sqlmodel import SQLModel, Field
from typing import Optional
import datetime

class ArchivoMensaje(SQLModel, table=True):
    IdArchivo: Optional[int] = Field(default=None, primary_key=True)
    IdMensaje: int = Field(foreign_key="mensaje.IdMensaje")
    UrlArchivo: str
    TipoArchivo: str
    SubidoHace: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)


class ArchivoMensajeBase(SQLModel):
    IdMensaje: int
    UrlArchivo: str
    TipoArchivo: str

class ArchivoMensajeCreate(ArchivoMensajeBase):
    pass

class ArchivoMensajePublic(ArchivoMensajeBase):
    IdArchivo: int
    SubidoHace: datetime.datetime
    mensaje: Optional["MensajePublic"] = None 

class ArchivoMensajeUpdate(SQLModel):
    UrlArchivo: Optional[str] = None
    TipoArchivo: Optional[str] = None


from models.mensaje import MensajePublic
ArchivoMensajePublic.model_rebuild()
