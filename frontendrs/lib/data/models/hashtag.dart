class Hashtag {
  final int idHashtag;
  final String nombre;
  final DateTime fechaCreacion;

  const Hashtag({
    required this.idHashtag,
    required this.nombre,
    required this.fechaCreacion,
  });

  factory Hashtag.fromJson(Map<String, dynamic> json) {
    return Hashtag(
      idHashtag: json['IdHashtag'] ?? 0,
      nombre: json['Nombre'] ?? "",
      fechaCreacion: DateTime.parse(json['FechaCreacion']),
    );
  }

  Map<String, dynamic> toJson() => {
    'IdHashtag': idHashtag,
    'Nombre': nombre,
    'FechaCreacion': fechaCreacion.toIso8601String(),
  };
}

class HashtagCreate {
  final String nombre;

  const HashtagCreate({required this.nombre});

  Map<String, dynamic> toJson() => {'Nombre': nombre};
}

class HashtagUpdate {
  final String nombre;

  const HashtagUpdate({required this.nombre});

  Map<String, dynamic> toJson() => {'Nombre': nombre};
}
