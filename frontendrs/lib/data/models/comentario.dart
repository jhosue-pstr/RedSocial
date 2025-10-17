import 'dart:convert';

class Comentario {
  final int idComentario;
  final int idPublicacion;
  final int idUsuario;
  final String contenido;
  final DateTime fecha;
  final bool estado;

  Comentario({
    required this.idComentario,
    required this.idPublicacion,
    required this.idUsuario,
    required this.contenido,
    required this.fecha,
    required this.estado,
  });

  // --- Crear objeto desde JSON ---
  factory Comentario.fromJson(Map<String, dynamic> json) {
    return Comentario(
      idComentario: json['IdComentario'] ?? 0,
      idPublicacion: json['IdPublicacion'] ?? 0,
      idUsuario: json['IdUsuario'] ?? 0,
      contenido: json['Contenido'] ?? '',
      fecha: DateTime.tryParse(json['Fecha'] ?? '') ?? DateTime.now(),
      estado: json['Estado'] ?? true,
    );
  }

  // --- Convertir objeto a JSON ---
  Map<String, dynamic> toJson() {
    return {
      'IdComentario': idComentario,
      'IdPublicacion': idPublicacion,
      'IdUsuario': idUsuario,
      'Contenido': contenido,
      'Fecha': fecha.toIso8601String(),
      'Estado': estado,
    };
  }

  // --- Convertir lista JSON a lista de objetos Comentario ---
  static List<Comentario> fromJsonList(String jsonString) {
    final data = json.decode(jsonString);
    return List<Comentario>.from(data.map((item) => Comentario.fromJson(item)));
  }

  // --- Convertir objeto a string JSON ---
  String toJsonString() => json.encode(toJson());
}
