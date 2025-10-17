class MencionesUsuario {
  final int idMencion;
  final int idPublicacion;
  final int idUsuario;
  final DateTime fecha;

  const MencionesUsuario({
    required this.idMencion,
    required this.idPublicacion,
    required this.idUsuario,
    required this.fecha,
  });

  factory MencionesUsuario.fromJson(Map<String, dynamic> json) {
    return MencionesUsuario(
      idMencion: json['IdMencion'] ?? 0,
      idPublicacion: json['IdPublicacion'] ?? 0,
      idUsuario: json['IdUsuario'] ?? 0,
      fecha: DateTime.parse(json['Fecha']),
    );
  }

  Map<String, dynamic> toJson() => {
    'IdMencion': idMencion,
    'IdPublicacion': idPublicacion,
    'IdUsuario': idUsuario,
    'Fecha': fecha.toIso8601String(),
  };
}

class MencionesUsuarioCreate {
  final int idPublicacion;
  final int idUsuario;

  const MencionesUsuarioCreate({
    required this.idPublicacion,
    required this.idUsuario,
  });

  Map<String, dynamic> toJson() => {
    'IdPublicacion': idPublicacion,
    'IdUsuario': idUsuario,
  };
}

class MencionesUsuarioUpdate {
  final DateTime fecha;

  const MencionesUsuarioUpdate({required this.fecha});

  Map<String, dynamic> toJson() => {'Fecha': fecha.toIso8601String()};
}
