import 'dart:convert';

class EnlacesPerfil {
  final int idEnlace;
  final int idPerfil;
  final String tipo;
  final String url;
  final DateTime fechaAgregado;

  EnlacesPerfil({
    required this.idEnlace,
    required this.idPerfil,
    required this.tipo,
    required this.url,
    required this.fechaAgregado,
  });

  // --- Convertir JSON a objeto ---
  factory EnlacesPerfil.fromJson(Map<String, dynamic> json) {
    return EnlacesPerfil(
      idEnlace: json['IdEnlace'] ?? 0,
      idPerfil: json['IdPerfil'] ?? 0,
      tipo: json['Tipo'] ?? '',
      url: json['Url'] ?? '',
      fechaAgregado:
          DateTime.tryParse(json['FechaAgregado'] ?? '') ?? DateTime.now(),
    );
  }

  // --- Convertir objeto a JSON ---
  Map<String, dynamic> toJson() {
    return {
      'IdEnlace': idEnlace,
      'IdPerfil': idPerfil,
      'Tipo': tipo,
      'Url': url,
      'FechaAgregado': fechaAgregado.toIso8601String(),
    };
  }

  // --- Convertir lista JSON a lista de objetos ---
  static List<EnlacesPerfil> fromJsonList(String jsonString) {
    final data = json.decode(jsonString);
    return List<EnlacesPerfil>.from(
      data.map((item) => EnlacesPerfil.fromJson(item)),
    );
  }

  // --- Convertir objeto a string JSON ---
  String toJsonString() => json.encode(toJson());
}
