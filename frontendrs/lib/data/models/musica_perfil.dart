import 'dart:convert';

class MusicaPerfilBase {
  final String plataforma;
  final String urlCancion;
  final String tituloCancion;
  final String artista;
  final DateTime fechaVinculacion;

  MusicaPerfilBase({
    required this.plataforma,
    required this.urlCancion,
    required this.tituloCancion,
    required this.artista,
    required this.fechaVinculacion,
  });

  factory MusicaPerfilBase.fromJson(Map<String, dynamic> json) {
    return MusicaPerfilBase(
      plataforma: json['Plataforma'],
      urlCancion: json['UrlCancion'],
      tituloCancion: json['TituloCancion'],
      artista: json['Artista'],
      fechaVinculacion: DateTime.parse(json['FechaVinculacion']),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'Plataforma': plataforma,
      'UrlCancion': urlCancion,
      'TituloCancion': tituloCancion,
      'Artista': artista,
      // Convierte la fecha a formato ISO para enviarla al backend
      'FechaVinculacion': fechaVinculacion.toIso8601String(),
    };
  }
}

class MusicaPerfil extends MusicaPerfilBase {
  final int? idMusica;
  final int idPerfil;

  MusicaPerfil({
    this.idMusica,
    required this.idPerfil,
    required String plataforma,
    required String urlCancion,
    required String tituloCancion,
    required String artista,
    required DateTime fechaVinculacion,
  }) : super(
         plataforma: plataforma,
         urlCancion: urlCancion,
         tituloCancion: tituloCancion,
         artista: artista,
         fechaVinculacion: fechaVinculacion,
       );

  factory MusicaPerfil.fromJson(Map<String, dynamic> json) {
    return MusicaPerfil(
      idMusica: json['IdMusica'],
      idPerfil: json['IdPerfil'],
      plataforma: json['Plataforma'],
      urlCancion: json['UrlCancion'],
      tituloCancion: json['TituloCancion'],
      artista: json['Artista'],
      fechaVinculacion: DateTime.parse(json['FechaVinculacion']),
    );
  }

  @override
  Map<String, dynamic> toJson() {
    return {
      'IdMusica': idMusica,
      'IdPerfil': idPerfil,
      'Plataforma': plataforma,
      'UrlCancion': urlCancion,
      'TituloCancion': tituloCancion,
      'Artista': artista,
      'FechaVinculacion': fechaVinculacion.toIso8601String(),
    };
  }
}

class MusicaPerfilCreate {
  final int idPerfil;
  final String plataforma;
  final String urlCancion;
  final String tituloCancion;
  final String artista;

  MusicaPerfilCreate({
    required this.idPerfil,
    required this.plataforma,
    required this.urlCancion,
    required this.tituloCancion,
    required this.artista,
  });

  Map<String, dynamic> toJson() {
    return {
      'IdPerfil': idPerfil,
      'Plataforma': plataforma,
      'UrlCancion': urlCancion,
      'TituloCancion': tituloCancion,
      'Artista': artista,
    };
  }
}

class MusicaPerfilPublic extends MusicaPerfilBase {
  final int idMusica;
  final int idPerfil;

  MusicaPerfilPublic({
    required this.idMusica,
    required this.idPerfil,
    required String plataforma,
    required String urlCancion,
    required String tituloCancion,
    required String artista,
    required DateTime fechaVinculacion,
  }) : super(
         plataforma: plataforma,
         urlCancion: urlCancion,
         tituloCancion: tituloCancion,
         artista: artista,
         fechaVinculacion: fechaVinculacion,
       );

  factory MusicaPerfilPublic.fromJson(Map<String, dynamic> json) {
    return MusicaPerfilPublic(
      idMusica: json['IdMusica'],
      idPerfil: json['IdPerfil'],
      plataforma: json['Plataforma'],
      urlCancion: json['UrlCancion'],
      tituloCancion: json['TituloCancion'],
      artista: json['Artista'],
      fechaVinculacion: DateTime.parse(json['FechaVinculacion']),
    );
  }

  @override
  Map<String, dynamic> toJson() {
    return {
      'IdMusica': idMusica,
      'IdPerfil': idPerfil,
      'Plataforma': plataforma,
      'UrlCancion': urlCancion,
      'TituloCancion': tituloCancion,
      'Artista': artista,
      'FechaVinculacion': fechaVinculacion.toIso8601String(),
    };
  }
}

class MusicaPerfilUpdate {
  final String plataforma;
  final String urlCancion;
  final String tituloCancion;
  final String artista;

  MusicaPerfilUpdate({
    required this.plataforma,
    required this.urlCancion,
    required this.tituloCancion,
    required this.artista,
  });

  Map<String, dynamic> toJson() {
    return {
      'Plataforma': plataforma,
      'UrlCancion': urlCancion,
      'TituloCancion': tituloCancion,
      'Artista': artista,
    };
  }
}
