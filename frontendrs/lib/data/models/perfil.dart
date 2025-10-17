import 'dart:convert';
import 'usuario.dart';
import 'enlace_perfil.dart';
import 'foto_perfil.dart';
import 'musica_perfil.dart';
import 'publicaciones.dart';
import 'perfil_interes.dart';

class Perfil {
  final int? idPerfil;
  final DateTime fechaCreacion;
  final DateTime ultimaActualizacion;
  final int idUsuario;

  final String? descripcion;
  final String? fotoPerfil;
  final String? fotoPortada;
  final String? pronombres;
  final DateTime? fechaNacimiento;
  final String? genero;
  final String? orientacionSexual;
  final String? direccion;
  final String? ciudad;
  final String? pais;
  final String? telefono;
  final String? estudios;
  final String? ocupacion;
  final String? estadoRelacion;
  final String? biografia;
  final String? sitioWeb;

  final Usuario? usuario;
  final List<EnlacesPerfil>? enlacesPerfil;
  final List<FotosPerfil>? fotosPerfil;
  final List<MusicaPerfil>? musicaPerfil;
  final List<Publicaciones>? publicaciones;
  final List<PerfilInteres>? interesesRel;

  Perfil({
    this.idPerfil,
    required this.fechaCreacion,
    required this.ultimaActualizacion,
    required this.idUsuario,
    this.descripcion,
    this.fotoPerfil,
    this.fotoPortada,
    this.pronombres,
    this.fechaNacimiento,
    this.genero,
    this.orientacionSexual,
    this.direccion,
    this.ciudad,
    this.pais,
    this.telefono,
    this.estudios,
    this.ocupacion,
    this.estadoRelacion,
    this.biografia,
    this.sitioWeb,
    this.usuario,
    this.enlacesPerfil,
    this.fotosPerfil,
    this.musicaPerfil,
    this.publicaciones,
    this.interesesRel,
  });

  factory Perfil.fromJson(Map<String, dynamic> json) {
    return Perfil(
      idPerfil: json['IdPerfil'],
      fechaCreacion: json['FechaCreacion'] != null
          ? DateTime.parse(json['FechaCreacion'])
          : DateTime.now(),
      ultimaActualizacion: json['UltimaActualizacion'] != null
          ? DateTime.parse(json['UltimaActualizacion'])
          : DateTime.now(),
      idUsuario: json['IdUsuario'],
      descripcion: json['Descripcion'],
      fotoPerfil: json['FotoPerfil'],
      fotoPortada: json['FotoPortada'],
      pronombres: json['Pronombres'],
      fechaNacimiento: json['FechaNacimiento'] != null
          ? DateTime.parse(json['FechaNacimiento'])
          : null,
      genero: json['Genero'],
      orientacionSexual: json['OrientacionSexual'],
      direccion: json['Direccion'],
      ciudad: json['Ciudad'],
      pais: json['Pais'],
      telefono: json['Telefono'],
      estudios: json['Estudios'],
      ocupacion: json['Ocupacion'],
      estadoRelacion: json['EstadoRelacion'],
      biografia: json['Biografia'],
      sitioWeb: json['SitioWeb'],
      usuario: json['usuario'] != null
          ? Usuario.fromJson(json['usuario'])
          : null,
      enlacesPerfil: json['enlaces_perfil'] != null
          ? (json['enlaces_perfil'] as List)
                .map((e) => EnlacesPerfil.fromJson(e))
                .toList()
          : [],
      fotosPerfil: json['fotos_perfil'] != null
          ? (json['fotos_perfil'] as List)
                .map((e) => FotosPerfil.fromJson(e))
                .toList()
          : [],
      musicaPerfil: json['musica_perfil'] != null
          ? (json['musica_perfil'] as List)
                .map((e) => MusicaPerfil.fromJson(e))
                .toList()
          : [],
      publicaciones: json['publicaciones'] != null
          ? (json['publicaciones'] as List)
                .map((e) => Publicaciones.fromJson(e))
                .toList()
          : [],
      interesesRel: json['intereses_rel'] != null
          ? (json['intereses_rel'] as List)
                .map((e) => PerfilInteres.fromJson(e))
                .toList()
          : [],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'IdPerfil': idPerfil,
      'FechaCreacion': fechaCreacion.toIso8601String(),
      'UltimaActualizacion': ultimaActualizacion.toIso8601String(),
      'IdUsuario': idUsuario,
      'Descripcion': descripcion,
      'FotoPerfil': fotoPerfil,
      'FotoPortada': fotoPortada,
      'Pronombres': pronombres,
      'FechaNacimiento': fechaNacimiento?.toIso8601String(),
      'Genero': genero,
      'OrientacionSexual': orientacionSexual,
      'Direccion': direccion,
      'Ciudad': ciudad,
      'Pais': pais,
      'Telefono': telefono,
      'Estudios': estudios,
      'Ocupacion': ocupacion,
      'EstadoRelacion': estadoRelacion,
      'Biografia': biografia,
      'SitioWeb': sitioWeb,
      'usuario': usuario?.toJson(),
      'enlaces_perfil': enlacesPerfil?.map((e) => e.toJson()).toList(),
      'fotos_perfil': fotosPerfil?.map((e) => e.toJson()).toList(),
      'musica_perfil': musicaPerfil?.map((e) => e.toJson()).toList(),
      'publicaciones': publicaciones?.map((e) => e.toJson()).toList(),
      'intereses_rel': interesesRel?.map((e) => e.toJson()).toList(),
    };
  }

  Perfil copyWith({
    int? idPerfil,
    DateTime? fechaCreacion,
    DateTime? ultimaActualizacion,
    int? idUsuario,
    String? descripcion,
    String? fotoPerfil,
    String? fotoPortada,
    String? pronombres,
    DateTime? fechaNacimiento,
    String? genero,
    String? orientacionSexual,
    String? direccion,
    String? ciudad,
    String? pais,
    String? telefono,
    String? estudios,
    String? ocupacion,
    String? estadoRelacion,
    String? biografia,
    String? sitioWeb,
    Usuario? usuario,
    List<EnlacesPerfil>? enlacesPerfil,
    List<FotosPerfil>? fotosPerfil,
    List<MusicaPerfil>? musicaPerfil,
    List<Publicaciones>? publicaciones,
    List<PerfilInteres>? interesesRel,
  }) {
    return Perfil(
      idPerfil: idPerfil ?? this.idPerfil,
      fechaCreacion: fechaCreacion ?? this.fechaCreacion,
      ultimaActualizacion: ultimaActualizacion ?? this.ultimaActualizacion,
      idUsuario: idUsuario ?? this.idUsuario,
      descripcion: descripcion ?? this.descripcion,
      fotoPerfil: fotoPerfil ?? this.fotoPerfil,
      fotoPortada: fotoPortada ?? this.fotoPortada,
      pronombres: pronombres ?? this.pronombres,
      fechaNacimiento: fechaNacimiento ?? this.fechaNacimiento,
      genero: genero ?? this.genero,
      orientacionSexual: orientacionSexual ?? this.orientacionSexual,
      direccion: direccion ?? this.direccion,
      ciudad: ciudad ?? this.ciudad,
      pais: pais ?? this.pais,
      telefono: telefono ?? this.telefono,
      estudios: estudios ?? this.estudios,
      ocupacion: ocupacion ?? this.ocupacion,
      estadoRelacion: estadoRelacion ?? this.estadoRelacion,
      biografia: biografia ?? this.biografia,
      sitioWeb: sitioWeb ?? this.sitioWeb,
      usuario: usuario ?? this.usuario,
      enlacesPerfil: enlacesPerfil ?? this.enlacesPerfil,
      fotosPerfil: fotosPerfil ?? this.fotosPerfil,
      musicaPerfil: musicaPerfil ?? this.musicaPerfil,
      publicaciones: publicaciones ?? this.publicaciones,
      interesesRel: interesesRel ?? this.interesesRel,
    );
  }

  @override
  String toString() => jsonEncode(toJson());
}
