import 'dart:convert';

class ParticipanteConversacion {
  final int? idParticipante;
  final int idConversacion;
  final int idUsuario;
  final DateTime? unidoHace;
  final UsuarioPublic? usuario;
  final ConversacionPublic? conversacion;

  ParticipanteConversacion({
    this.idParticipante,
    required this.idConversacion,
    required this.idUsuario,
    this.unidoHace,
    this.usuario,
    this.conversacion,
  });

  factory ParticipanteConversacion.fromJson(Map<String, dynamic> json) {
    return ParticipanteConversacion(
      idParticipante: json['IdParticipante'],
      idConversacion: json['IdConversacion'],
      idUsuario: json['IdUsuario'],
      unidoHace: json['UnidoHace'] != null
          ? DateTime.parse(json['UnidoHace'])
          : null,
      usuario: json['usuario'] != null
          ? UsuarioPublic.fromJson(json['usuario'])
          : null,
      conversacion: json['conversacion'] != null
          ? ConversacionPublic.fromJson(json['conversacion'])
          : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'IdParticipante': idParticipante,
      'IdConversacion': idConversacion,
      'IdUsuario': idUsuario,
      'UnidoHace': unidoHace?.toIso8601String(),
      'usuario': usuario?.toJson(),
      'conversacion': conversacion?.toJson(),
    };
  }

  ParticipanteConversacion copyWith({
    int? idParticipante,
    int? idConversacion,
    int? idUsuario,
    DateTime? unidoHace,
    UsuarioPublic? usuario,
    ConversacionPublic? conversacion,
  }) {
    return ParticipanteConversacion(
      idParticipante: idParticipante ?? this.idParticipante,
      idConversacion: idConversacion ?? this.idConversacion,
      idUsuario: idUsuario ?? this.idUsuario,
      unidoHace: unidoHace ?? this.unidoHace,
      usuario: usuario ?? this.usuario,
      conversacion: conversacion ?? this.conversacion,
    );
  }

  @override
  String toString() => jsonEncode(toJson());
}

class UsuarioPublic {
  final int idUsuario;
  final String nombre;
  final String correo;

  UsuarioPublic({
    required this.idUsuario,
    required this.nombre,
    required this.correo,
  });

  factory UsuarioPublic.fromJson(Map<String, dynamic> json) {
    return UsuarioPublic(
      idUsuario: json['IdUsuario'],
      nombre: json['Nombre'],
      correo: json['Correo'],
    );
  }

  Map<String, dynamic> toJson() {
    return {'IdUsuario': idUsuario, 'Nombre': nombre, 'Correo': correo};
  }
}

class ConversacionPublic {
  final int idConversacion;
  final String titulo;
  final DateTime? creadaHace;

  ConversacionPublic({
    required this.idConversacion,
    required this.titulo,
    this.creadaHace,
  });

  factory ConversacionPublic.fromJson(Map<String, dynamic> json) {
    return ConversacionPublic(
      idConversacion: json['IdConversacion'],
      titulo: json['Titulo'],
      creadaHace: json['CreadaHace'] != null
          ? DateTime.parse(json['CreadaHace'])
          : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'IdConversacion': idConversacion,
      'Titulo': titulo,
      'CreadaHace': creadaHace?.toIso8601String(),
    };
  }
}
