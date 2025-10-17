import 'dart:convert';

class ArchivoPublicacion {
  final int idArchivo;
  final int idPublicacion;
  final String urlArchivo;
  final String tipoArchivo;
  final DateTime subidoHace;

  ArchivoPublicacion({
    required this.idArchivo,
    required this.idPublicacion,
    required this.urlArchivo,
    required this.tipoArchivo,
    required this.subidoHace,
  });

  // --- Crear objeto desde JSON ---
  factory ArchivoPublicacion.fromJson(Map<String, dynamic> json) {
    return ArchivoPublicacion(
      idArchivo: json['IdArchivo'] ?? 0,
      idPublicacion: json['IdPublicacion'] ?? 0,
      urlArchivo: json['UrlArchivo'] ?? '',
      tipoArchivo: json['TipoArchivo'] ?? '',
      subidoHace: DateTime.tryParse(json['SubidoHace'] ?? '') ?? DateTime.now(),
    );
  }

  // --- Convertir objeto a JSON ---
  Map<String, dynamic> toJson() {
    return {
      'IdArchivo': idArchivo,
      'IdPublicacion': idPublicacion,
      'UrlArchivo': urlArchivo,
      'TipoArchivo': tipoArchivo,
      'SubidoHace': subidoHace.toIso8601String(),
    };
  }

  // --- Convertir lista JSON a lista de objetos ---
  static List<ArchivoPublicacion> fromJsonList(String jsonString) {
    final data = json.decode(jsonString);
    return List<ArchivoPublicacion>.from(
      data.map((item) => ArchivoPublicacion.fromJson(item)),
    );
  }

  // --- Convertir objeto a string JSON ---
  String toJsonString() => json.encode(toJson());
}
