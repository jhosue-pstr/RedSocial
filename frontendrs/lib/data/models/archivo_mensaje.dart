class ArchivoMensaje {
  final int idArchivo;
  final int idMensaje;
  final String urlArchivo;
  final String tipoArchivo;
  final DateTime subidoHace;

  const ArchivoMensaje({
    required this.idArchivo,
    required this.idMensaje,
    required this.urlArchivo,
    required this.tipoArchivo,
    required this.subidoHace,
  });

  factory ArchivoMensaje.fromJson(Map<String, dynamic> json) {
    return ArchivoMensaje(
      idArchivo: json['IdArchivo'] ?? 0,
      idMensaje: json['IdMensaje'] ?? 0,
      urlArchivo: json['UrlArchivo'] ?? '',
      tipoArchivo: json['TipoArchivo'] ?? '',
      subidoHace: DateTime.parse(json['SubidoHace']),
    );
  }

  Map<String, dynamic> toJson() => {
    'IdArchivo': idArchivo,
    'IdMensaje': idMensaje,
    'UrlArchivo': urlArchivo,
    'TipoArchivo': tipoArchivo,
    'SubidoHace': subidoHace.toIso8601String(),
  };
}
