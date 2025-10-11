from fastapi import HTTPException
from sqlmodel import Session
from config.database import get_session
from models.fotos_perfil import FotosPerfil, FotosPerfilCreate, FotosPerfilPublic, FotosPerfilUpdate
from models.perfil import Perfil  # Asegúrate de importar el modelo Perfil

# Crear una foto para un perfil
def CrearFoto(foto: FotosPerfilCreate, session: Session, perfil_id: int) -> FotosPerfilPublic:
    # Asegurarse de que el perfil exista
    perfil_db = session.get(Perfil, perfil_id)
    if not perfil_db:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")

    nueva_foto = FotosPerfil(
        UrlFoto=foto.UrlFoto,
        Tipo=foto.Tipo,
        Descripcion=foto.Descripcion,
        Estado=foto.Estado,
        IdPerfil=perfil_id  # Relacionamos la foto con el perfil
    )

    session.add(nueva_foto)
    session.commit()
    session.refresh(nueva_foto)
    return FotosPerfilPublic.model_validate(nueva_foto)

# Leer una foto por IdFoto
def LeerFotoPorId(IdFoto: int, session: Session) -> FotosPerfilPublic:
    foto = session.get(FotosPerfil, IdFoto)
    if not foto:
        raise HTTPException(status_code=404, detail="Foto no encontrada")
    return FotosPerfilPublic.model_validate(foto)

# Leer todas las fotos de un perfil
def LeerFotos(session: Session) -> list[FotosPerfilPublic]:
    fotos = session.exec(select(FotosPerfil)).all()  # Obtener todas las fotos
    return [FotosPerfilPublic.model_validate(f) for f in fotos]

# Actualizar una foto por IdFoto
def ActualizarFoto(IdFoto: int, datos: FotosPerfilUpdate, session: Session) -> FotosPerfilPublic:
    foto_db = session.get(FotosPerfil, IdFoto)
    if not foto_db:
        raise HTTPException(status_code=404, detail="Foto no encontrada")

    update_data = datos.model_dump(exclude_unset=True)
    foto_db.sqlmodel_update(update_data)

    session.add(foto_db)
    session.commit()
    session.refresh(foto_db)
    return FotosPerfilPublic.model_validate(foto_db)

# Eliminar una foto
def EliminarFoto(IdFoto: int, session: Session):
    foto = session.get(FotosPerfil, IdFoto)
    if not foto:
        raise HTTPException(status_code=404, detail="Foto no encontrada")
    session.delete(foto)
    session.commit()
    return {"message": "Foto eliminada"}
