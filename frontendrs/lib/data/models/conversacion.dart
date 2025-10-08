class Conversacion {
  final int idConversacion;
  final String nombre;
  final DateTime fechaCreacion;
  final bool esConversacion;
  final bool estado;

  const Conversacion({
    required this.idConversacion,
    required this.nombre,
    required this.fechaCreacion,
    required this.esConversacion,
    required this.estado,
  });

  factory Conversacion.fromJson(Map<String, dynamic> json) {
    return Conversacion(
      idConversacion: json['IdConversacion'] ?? 0,
      nombre: json['Nombre'] ?? '',
      fechaCreacion: DateTime.parse(json['FechaCreacion']),
      esConversacion: bool.fromEnvironment(json['EsConversacion']),
      estado: bool.fromEnvironment(json['Estado']),
    );
  }
  Map<String, dynamic> toJson() => {
    'IdConversacion': idConversacion,
    'Nombre': nombre,
    'FechaCreacion': fechaCreacion.toIso8601String(),
    'EsConversacion': esConversacion,
    'Estado': estado,
  };
}
