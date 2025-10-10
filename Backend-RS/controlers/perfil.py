from fastapi import HTTPException
from sqlmodel import Session
from models.perfil import Perfil, PerfilCreate, PerfilPublic, PerfilUpdate
from controlers.auth import get_user_by_email


def CrearPerfil(perfil: PerfilCreate, session: Session, user_id: int) -> PerfilPublic:
    # Crear un perfil para el usuario, asegurándonos de que el usuario existe
    usuario_db = session.get(Usuario, user_id)
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    nuevo_perfil = Perfil(
        Descripcion=perfil.Descripcion,
        FotoPerfil=perfil.FotoPerfil,
        FotoPortada=perfil.FotoPortada,
        Pronombres=perfil.Pronombres,
        FechaNacimiento=perfil.FechaNacimiento,
        Genero=perfil.Genero,
        OrientacionSexual=perfil.OrientacionSexual,
        Direccion=perfil.Direccion,
        Ciudad=perfil.Ciudad,
        Pais=perfil.Pais,
        Telefono=perfil.Telefono,
        Estudios=perfil.Estudios,
        Ocupacion=perfil.Ocupacion,
        EstadoRelacion=perfil.EstadoRelacion,
        Biografia=perfil.Biografia,
        SitioWeb=perfil.SitioWeb,
        IdUsuario=user_id  # Asignar al usuario correspondiente
    )

    session.add(nuevo_perfil)
    session.commit()
    session.refresh(nuevo_perfil)
    return PerfilPublic.model_validate(nuevo_perfil)


def LeerPerfilPorUsuario(IdUsuario: int, session: Session) -> PerfilPublic:
    perfil = session.exec(select(Perfil).where(Perfil.IdUsuario == IdUsuario)).first()
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return PerfilPublic.model_validate(perfil)


def ActualizarPerfil(IdPerfil: int, datos: PerfilUpdate, session: Session) -> PerfilPublic:
    perfil_db = session.get(Perfil, IdPerfil)
    if not perfil_db:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")

    update_data = datos.model_dump(exclude_unset=True)
    perfil_db.sqlmodel_update(update_data)

    session.add(perfil_db)
    session.commit()
    session.refresh(perfil_db)
    return PerfilPublic.model_validate(perfil_db)


def EliminarPerfil(IdPerfil: int, session: Session):
    perfil = session.get(Perfil, IdPerfil)
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    session.delete(perfil)
    session.commit()
    return {"message": "Perfil eliminado"}
