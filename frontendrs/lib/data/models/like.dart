class Like {
  final int idLike;
  final int idPublicacion;
  final int idUsuario;
  final DateTime fecha;

  const Like({
    required this.idLike,
    required this.idPublicacion,
    required this.idUsuario,
    required this.fecha,
  });

  factory Like.fromJson(Map<String, dynamic> json) {
    return Like(
      idLike: json['IdLike'] ?? 0,
      idPublicacion: json['IdPublicacion'] ?? 0,
      idUsuario: json['IdUsuario'] ?? 0,
      fecha: DateTime.parse(json['Fecha']),
    );
  }

  Map<String, dynamic> toJson() => {
    'IdLike': idLike,
    'IdPublicacion': idPublicacion,
    'IdUsuario': idUsuario,
    'Fecha': fecha.toIso8601String(),
  };
}

class LikeCreate {
  final int idPublicacion;

  const LikeCreate({required this.idPublicacion});

  Map<String, dynamic> toJson() => {'IdPublicacion': idPublicacion};
}

class LikeUpdate {
  final DateTime fecha;

  const LikeUpdate({required this.fecha});

  Map<String, dynamic> toJson() => {'Fecha': fecha.toIso8601String()};
}
