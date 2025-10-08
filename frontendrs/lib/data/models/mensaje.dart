import 'dart:convert';

class Mensaje {
  final int? idMensaje;
  final String contenido;
  final bool leido;
  final int idConversacion;
  final int idUsuario;
  final DateTime? fechaEnvio;

  const Mensaje({
    this.idMensaje,
    required this.contenido,
    this.leido = false,
    required this.idConversacion,
    required this.idUsuario,
    this.fechaEnvio,
  });

  factory Mensaje.fromJson(Map<String, dynamic> json) {
    return Mensaje(
      idMensaje: json['IdMensaje'],
      contenido: json['Contenido'] ?? '',
      leido: json['Leido'] ?? false,
      idConversacion: json['IdConversacion'] ?? 0,
      idUsuario: json['IdUsuario'] ?? 0,
      fechaEnvio: json['FechaEnvio'] != null
          ? DateTime.tryParse(json['FechaEnvio'])
          : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'IdMensaje': idMensaje,
      'Contenido': contenido,
      'Leido': leido,
      'IdConversacion': idConversacion,
      'IdUsuario': idUsuario,
      'FechaEnvio': fechaEnvio?.toIso8601String(),
    };
  }

  Mensaje copyWith({
    int? idMensaje,
    String? contenido,
    bool? leido,
    int? idConversacion,
    int? idUsuario,
    DateTime? fechaEnvio,
  }) {
    return Mensaje(
      idMensaje: idMensaje ?? this.idMensaje,
      contenido: contenido ?? this.contenido,
      leido: leido ?? this.leido,
      idConversacion: idConversacion ?? this.idConversacion,
      idUsuario: idUsuario ?? this.idUsuario,
      fechaEnvio: fechaEnvio ?? this.fechaEnvio,
    );
  }

  @override
  String toString() => jsonEncode(toJson());
}
