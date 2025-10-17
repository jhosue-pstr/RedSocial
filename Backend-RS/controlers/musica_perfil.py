from fastapi import HTTPException
from sqlmodel import Session, select
from config.database import get_session
from models.musica_perfil import (MusicaPerfil, MusicaPerfilCreate, MusicaPerfilPublic, MusicaPerfilUpdate)
from models.perfil import Perfil

# Crear música vinculada al perfil del usuario
def CrearMusica(musica: MusicaPerfilCreate, session: Session, id_usuario: int) -> MusicaPerfilPublic:
    # Buscar el perfil del usuario autenticado
    perfil_db = session.exec(select(Perfil).where(Perfil.IdUsuario == id_usuario)).first()
    if not perfil_db:
        raise HTTPException(status_code=404, detail="Perfil no encontrado para el usuario")

    nueva = MusicaPerfil(
        Plataforma=musica.Plataforma,
        UrlCancion=musica.UrlCancion,
        TituloCancion=musica.TituloCancion,
        Artista=musica.Artista,
        IdPerfil=perfil_db.IdPerfil
    )
    session.add(nueva)
    session.commit()
    session.refresh(nueva)
    return MusicaPerfilPublic.model_validate(nueva)

# Leer por IdMusica
def LeerMusicaPorId(IdMusica: int, session: Session) -> MusicaPerfilPublic:
    item = session.get(MusicaPerfil, IdMusica)
    if not item:
        raise HTTPException(status_code=404, detail="Música no encontrada")
    return MusicaPerfilPublic.model_validate(item)

# Listar todo
def LeerMusicas(session: Session) -> list[MusicaPerfilPublic]:
    items = session.exec(select(MusicaPerfil)).all()
    return [MusicaPerfilPublic.model_validate(i) for i in items]

# Actualizar por IdMusica
def ActualizarMusica(IdMusica: int, datos: MusicaPerfilUpdate, session: Session) -> MusicaPerfilPublic:
    item_db = session.get(MusicaPerfil, IdMusica)
    if not item_db:
        raise HTTPException(status_code=404, detail="Música no encontrada")
    update_data = datos.model_dump(exclude_unset=True)
    item_db.sqlmodel_update(update_data)
    session.add(item_db)
    session.commit()
    session.refresh(item_db)
    return MusicaPerfilPublic.model_validate(item_db)

# Eliminar
def EliminarMusica(IdMusica: int, session: Session):
    item = session.get(MusicaPerfil, IdMusica)
    if not item:
        raise HTTPException(status_code=404, detail="Música no encontrada")
    session.delete(item)
    session.commit()
    return {"message": "Música eliminada"}
