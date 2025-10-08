class Mensaje {
  final int idMensaje;
  final String contenido;
  final bool leido;
  final int idConversacion;
  final int idUsuario;
  final DateTime fechaEnvio;

  const Mensaje({
    required this.idMensaje,
    required this.contenido,
    required this.leido,
    required this.idConversacion,
    required this.idUsuario,
    required this.fechaEnvio,
  });

  factory Mensaje.fromJson(Map<String, dynamic> json) {
    return Mensaje(
      idMensaje: json['idMensaje'] ?? 0,
      contenido: json['contenido'] ?? "",
      leido: json['leido'] ?? "",
      idConversacion: json['idConversacion'] ?? 0,
      idUsuario: json['idUsuario'] ?? 0,
      fechaEnvio: DateTime.parse(json['fechaEnvio']),
    );
  }

  Map<String, dynamic> toJson() => {
    'idMensaje': idMensaje,
    'contenido': contenido,
    'leido': leido,
    'idConversacion': idConversacion,
    'idUsuario': idUsuario,
    'fechaEnvio': fechaEnvio.toIso8601String(),
  };
}
