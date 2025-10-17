import 'dart:convert';
import 'perfil.dart';
import 'archivo_publicacion.dart';
import 'menciones_usuario.dart';
import 'like.dart';
import 'publicacion_hashtag.dart';
import 'comentario.dart';

class Publicaciones {
  final int? idPublicacion;
  final int idPerfil;
  final String contenido;
  final DateTime fechaCreacion;
  final bool estado;
  final String visibilidad;

  final Perfil? perfil;
  final List<ArchivoPublicacion>? archivosPublicaciones;
  final List<MencionesUsuario>? mencionesUsuario;
  final List<Like>? likes;
  final List<PublicacionHashtag>? hashtagsRel;
  final List<Comentario>? comentariosRel;

  Publicaciones({
    this.idPublicacion,
    required this.idPerfil,
    required this.contenido,
    required this.fechaCreacion,
    required this.estado,
    required this.visibilidad,
    this.perfil,
    this.archivosPublicaciones,
    this.mencionesUsuario,
    this.likes,
    this.hashtagsRel,
    this.comentariosRel,
  });

  factory Publicaciones.fromJson(Map<String, dynamic> json) {
    return Publicaciones(
      idPublicacion: json['IdPublicacion'],
      idPerfil: json['IdPerfil'],
      contenido: json['Contenido'],
      fechaCreacion: json['FechaCreacion'] != null
          ? DateTime.parse(json['FechaCreacion'])
          : DateTime.now(),
      estado: json['Estado'] ?? true,
      visibilidad: json['Visibilidad'],
      perfil: json['perfil'] != null ? Perfil.fromJson(json['perfil']) : null,
      archivosPublicaciones: json['archivos_publicaciones'] != null
          ? (json['archivos_publicaciones'] as List)
                .map((e) => ArchivoPublicacion.fromJson(e))
                .toList()
          : [],
      mencionesUsuario: json['menciones_usuario'] != null
          ? (json['menciones_usuario'] as List)
                .map((e) => MencionesUsuario.fromJson(e))
                .toList()
          : [],
      likes: json['likes'] != null
          ? (json['likes'] as List).map((e) => Like.fromJson(e)).toList()
          : [],
      hashtagsRel: json['hashtags_rel'] != null
          ? (json['hashtags_rel'] as List)
                .map((e) => PublicacionHashtag.fromJson(e))
                .toList()
          : [],
      comentariosRel: json['comentarios_rel'] != null
          ? (json['comentarios_rel'] as List)
                .map((e) => Comentario.fromJson(e))
                .toList()
          : [],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'IdPublicacion': idPublicacion,
      'IdPerfil': idPerfil,
      'Contenido': contenido,
      'FechaCreacion': fechaCreacion.toIso8601String(),
      'Estado': estado,
      'Visibilidad': visibilidad,
      'perfil': perfil?.toJson(),
      'archivos_publicaciones': archivosPublicaciones
          ?.map((e) => e.toJson())
          .toList(),
      'menciones_usuario': mencionesUsuario?.map((e) => e.toJson()).toList(),
      'likes': likes?.map((e) => e.toJson()).toList(),
      'hashtags_rel': hashtagsRel?.map((e) => e.toJson()).toList(),
      'comentarios_rel': comentariosRel?.map((e) => e.toJson()).toList(),
    };
  }

  Publicaciones copyWith({
    int? idPublicacion,
    int? idPerfil,
    String? contenido,
    DateTime? fechaCreacion,
    bool? estado,
    String? visibilidad,
    Perfil? perfil,
    List<ArchivoPublicacion>? archivosPublicaciones,
    List<MencionesUsuario>? mencionesUsuario,
    List<Like>? likes,
    List<PublicacionHashtag>? hashtagsRel,
    List<Comentario>? comentariosRel,
  }) {
    return Publicaciones(
      idPublicacion: idPublicacion ?? this.idPublicacion,
      idPerfil: idPerfil ?? this.idPerfil,
      contenido: contenido ?? this.contenido,
      fechaCreacion: fechaCreacion ?? this.fechaCreacion,
      estado: estado ?? this.estado,
      visibilidad: visibilidad ?? this.visibilidad,
      perfil: perfil ?? this.perfil,
      archivosPublicaciones:
          archivosPublicaciones ?? this.archivosPublicaciones,
      mencionesUsuario: mencionesUsuario ?? this.mencionesUsuario,
      likes: likes ?? this.likes,
      hashtagsRel: hashtagsRel ?? this.hashtagsRel,
      comentariosRel: comentariosRel ?? this.comentariosRel,
    );
  }

  @override
  String toString() => jsonEncode(toJson());
}
