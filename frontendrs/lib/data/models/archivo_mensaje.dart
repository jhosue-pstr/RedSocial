import 'package:flutter/material.dart';

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
}
