from fastapi import HTTPException
from sqlmodel import Session
from config.database import get_session
from models.enlaces_perfil import EnlacesPerfil, EnlacesPerfilCreate, EnlacesPerfilPublic, EnlacesPerfilUpdate
from models.perfil import Perfil  # Asegurarse de importar el modelo Perfil

# Crear un enlace para un perfil
def CrearEnlace(enlace: EnlacesPerfilCreate, session: Session, perfil_id: int) -> EnlacesPerfilPublic:
    # Asegurarse de que el perfil exista
    perfil_db = session.get(Perfil, perfil_id)
    if not perfil_db:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")

    nuevo_enlace = EnlacesPerfil(
        Tipo=enlace.Tipo,
        Url=enlace.Url,
        IdPerfil=perfil_id  # Relacionamos el enlace con el perfil
    )

    session.add(nuevo_enlace)
    session.commit()
    session.refresh(nuevo_enlace)
    return EnlacesPerfilPublic.model_validate(nuevo_enlace)

# Leer un enlace por IdEnlace
def LeerEnlacePorId(IdEnlace: int, session: Session) -> EnlacesPerfilPublic:
    enlace = session.get(EnlacesPerfil, IdEnlace)  # Usamos `IdEnlace` para obtener el enlace
    if not enlace:
        raise HTTPException(status_code=404, detail="Enlace no encontrado")
    return EnlacesPerfilPublic.model_validate(enlace)

# Leer todos los enlaces
def LeerEnlaces(session: Session) -> list[EnlacesPerfilPublic]:
    enlaces = session.exec(select(EnlacesPerfil)).all()  # Obtener todos los enlaces
    return [EnlacesPerfilPublic.model_validate(e) for e in enlaces]

# Actualizar un enlace por IdEnlace
def ActualizarEnlace(IdEnlace: int, datos: EnlacesPerfilUpdate, session: Session) -> EnlacesPerfilPublic:
    enlace_db = session.get(EnlacesPerfil, IdEnlace)
    if not enlace_db:
        raise HTTPException(status_code=404, detail="Enlace no encontrado")

    update_data = datos.model_dump(exclude_unset=True)
    enlace_db.sqlmodel_update(update_data)

    session.add(enlace_db)
    session.commit()
    session.refresh(enlace_db)
    return EnlacesPerfilPublic.model_validate(enlace_db)

# Eliminar un enlace
def EliminarEnlace(IdEnlace: int, session: Session):
    enlace = session.get(EnlacesPerfil, IdEnlace)
    if not enlace:
        raise HTTPException(status_code=404, detail="Enlace no encontrado")
    session.delete(enlace)
    session.commit()
    return {"message": "Enlace eliminado"}
