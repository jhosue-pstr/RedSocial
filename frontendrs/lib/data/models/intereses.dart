class Interes {
  final int idInteres;
  final String nombre;

  const Interes({required this.idInteres, required this.nombre});

  factory Interes.fromJson(Map<String, dynamic> json) {
    return Interes(
      idInteres: json['IdInteres'] ?? 0,
      nombre: json['Nombre'] ?? "",
    );
  }

  Map<String, dynamic> toJson() => {'IdInteres': idInteres, 'Nombre': nombre};
}

class InteresCreate {
  final String nombre;

  const InteresCreate({required this.nombre});

  Map<String, dynamic> toJson() => {'Nombre': nombre};
}

class InteresUpdate {
  final String nombre;

  const InteresUpdate({required this.nombre});

  Map<String, dynamic> toJson() => {'Nombre': nombre};
}
