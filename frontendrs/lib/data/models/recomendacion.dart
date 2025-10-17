import 'dart:convert';
import 'usuario.dart';

class Recomendacion {
  final int? idRecomendacion;
  final int idUsuario;
  final String motivo;
  final DateTime fecha;
  final Usuario? usuario;

  Recomendacion({
    this.idRecomendacion,
    required this.idUsuario,
    required this.motivo,
    required this.fecha,
    this.usuario,
  });

  factory Recomendacion.fromJson(Map<String, dynamic> json) {
    return Recomendacion(
      idRecomendacion: json['IdRecomendacion'],
      idUsuario: json['IdUsuario'],
      motivo: json['Motivo'],
      fecha: json['Fecha'] != null
          ? DateTime.parse(json['Fecha'])
          : DateTime.now(),
      usuario: json['usuario'] != null
          ? Usuario.fromJson(json['usuario'])
          : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'IdRecomendacion': idRecomendacion,
      'IdUsuario': idUsuario,
      'Motivo': motivo,
      'Fecha': fecha.toIso8601String(),
      'usuario': usuario?.toJson(),
    };
  }

  Recomendacion copyWith({
    int? idRecomendacion,
    int? idUsuario,
    String? motivo,
    DateTime? fecha,
    Usuario? usuario,
  }) {
    return Recomendacion(
      idRecomendacion: idRecomendacion ?? this.idRecomendacion,
      idUsuario: idUsuario ?? this.idUsuario,
      motivo: motivo ?? this.motivo,
      fecha: fecha ?? this.fecha,
      usuario: usuario ?? this.usuario,
    );
  }

  @override
  String toString() => jsonEncode(toJson());
}
