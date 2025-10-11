from fastapi import HTTPException
from sqlmodel import Session
from config.database import get_session
from models.perfil import Perfil, PerfilCreate, PerfilPublic, PerfilUpdate
from models.usuario import Usuario  # Asegúrate de importar Usuario para verificar la relación

# Crear un perfil para un usuario
def CrearPerfil(perfil: PerfilCreate, session: Session, user_id: int) -> PerfilPublic:
    # Asegurarse de que el usuario existe
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
        IdUsuario=user_id  # Relacionamos el perfil con el usuario
    )

    session.add(nuevo_perfil)
    session.commit()
    session.refresh(nuevo_perfil)
    return PerfilPublic.model_validate(nuevo_perfil)

# Leer el perfil por IdPerfil
def LeerPerfilPorId(IdPerfil: int, session: Session) -> PerfilPublic:
    perfil = session.get(Perfil, IdPerfil)  # Usamos `IdPerfil` en lugar de `IdUsuario`
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return PerfilPublic.model_validate(perfil)


# Actualizar el perfil de un usuario
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

# Eliminar un perfil
def EliminarPerfil(IdPerfil: int, session: Session):
    perfil = session.get(Perfil, IdPerfil)
    if not perfil:
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    session.delete(perfil)
    session.commit()
    return {"message": "Perfil eliminado"}
