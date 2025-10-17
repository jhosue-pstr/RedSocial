import 'dart:convert';

class FotosPerfil {
  final int idFoto;
  final int idPerfil;
  final String urlFoto;
  final String tipo;
  final String? descripcion;
  final DateTime fechaSubida;
  final bool estado;

  FotosPerfil({
    required this.idFoto,
    required this.idPerfil,
    required this.urlFoto,
    required this.tipo,
    this.descripcion,
    required this.fechaSubida,
    required this.estado,
  });

  // --- Convertir de JSON a objeto ---
  factory FotosPerfil.fromJson(Map<String, dynamic> json) {
    return FotosPerfil(
      idFoto: json['IdFoto'] ?? 0,
      idPerfil: json['IdPerfil'] ?? 0,
      urlFoto: json['UrlFoto'] ?? '',
      tipo: json['Tipo'] ?? '',
      descripcion: json['Descripcion'],
      fechaSubida:
          DateTime.tryParse(json['FechaSubida'] ?? '') ?? DateTime.now(),
      estado: json['Estado'] ?? true,
    );
  }

  // --- Convertir de objeto a JSON ---
  Map<String, dynamic> toJson() {
    return {
      'IdFoto': idFoto,
      'IdPerfil': idPerfil,
      'UrlFoto': urlFoto,
      'Tipo': tipo,
      'Descripcion': descripcion,
      'FechaSubida': fechaSubida.toIso8601String(),
      'Estado': estado,
    };
  }

  // --- Métodos útiles ---
  static List<FotosPerfil> fromJsonList(String jsonString) {
    final data = json.decode(jsonString);
    return List<FotosPerfil>.from(
      data.map((item) => FotosPerfil.fromJson(item)),
    );
  }

  String toJsonString() => json.encode(toJson());
}
