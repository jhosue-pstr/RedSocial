import 'dart:convert';

class Conversacion {
  final int? idConversacion;
  final String nombre;
  final DateTime? fechaCreacion;
  final bool esConversacion;
  final bool estado;

  const Conversacion({
    this.idConversacion,
    required this.nombre,
    this.fechaCreacion,
    this.esConversacion = true,
    this.estado = true,
  });

  factory Conversacion.fromJson(Map<String, dynamic> json) {
    return Conversacion(
      idConversacion: json['IdConversacion'],
      nombre: json['Nombre'] ?? '',
      fechaCreacion: json['FechaCreacion'] != null
          ? DateTime.tryParse(json['FechaCreacion'])
          : null,
      esConversacion:
          json['EsConversacion'] == true ||
          json['EsConversacion'] == 1 ||
          json['EsConversacion'] == 'true',
      estado:
          json['Estado'] == true ||
          json['Estado'] == 1 ||
          json['Estado'] == 'true',
    );
  }

  Map<String, dynamic> toJson() => {
    'IdConversacion': idConversacion,
    'Nombre': nombre,
    'FechaCreacion': fechaCreacion?.toIso8601String(),
    'EsConversacion': esConversacion,
    'Estado': estado,
  };

  Conversacion copyWith({
    int? idConversacion,
    String? nombre,
    DateTime? fechaCreacion,
    bool? esConversacion,
    bool? estado,
  }) {
    return Conversacion(
      idConversacion: idConversacion ?? this.idConversacion,
      nombre: nombre ?? this.nombre,
      fechaCreacion: fechaCreacion ?? this.fechaCreacion,
      esConversacion: esConversacion ?? this.esConversacion,
      estado: estado ?? this.estado,
    );
  }

  @override
  String toString() => jsonEncode(toJson());
}
