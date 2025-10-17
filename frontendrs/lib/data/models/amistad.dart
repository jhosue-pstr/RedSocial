import 'dart:convert';

class Amistad {
  final int idAmistad;
  final int idUsuario;
  final String estado;
  final DateTime fechaSolicitud;
  final DateTime? fechaAceptacion;

  const Amistad({
    required this.idAmistad,
    required this.idUsuario,
    required this.estado,
    required this.fechaSolicitud,
    this.fechaAceptacion,
  });

  // --- Crear objeto desde JSON ---
  factory Amistad.fromJson(Map<String, dynamic> json) {
    return Amistad(
      idAmistad: json['IdAmistad'] ?? 0,
      idUsuario: json['IdUsuario'] ?? 0,
      estado: json['Estado'] ?? '',
      fechaSolicitud:
          DateTime.tryParse(json['FechaSolicitud'] ?? '') ?? DateTime.now(),
      fechaAceptacion: json['FechaAceptacion'] != null
          ? DateTime.tryParse(json['FechaAceptacion'])
          : null,
    );
  }

  // --- Convertir objeto a JSON ---
  Map<String, dynamic> toJson() {
    return {
      'IdAmistad': idAmistad,
      'IdUsuario': idUsuario,
      'Estado': estado,
      'FechaSolicitud': fechaSolicitud.toIso8601String(),
      'FechaAceptacion': fechaAceptacion?.toIso8601String(),
    };
  }

  // --- Convertir lista JSON a lista de objetos ---
  static List<Amistad> fromJsonList(String jsonString) {
    final data = json.decode(jsonString);
    return List<Amistad>.from(data.map((item) => Amistad.fromJson(item)));
  }

  // --- Convertir objeto a string JSON ---
  String toJsonString() => json.encode(toJson());
}
