import 'package:http/http.dart' as http;
import 'dart:convert'; // <-- NECESARIO para jsonEncode / jsonDecode
import 'package:flutter/material.dart'; // <-- NECESARIO para widgets
import 'package:http/http.dart' as http;

class Usuario {
  final int idUsuario;
  final String nombre;
  final String apellido;
  final String correo;
  final String contrasena;
  final DateTime fechaRegistro;
  final bool estado;

  const Usuario({
    required this.idUsuario,
    required this.nombre,
    required this.apellido,
    required this.correo,
    required this.contrasena,
    required this.fechaRegistro,
    required this.estado,
  });

  factory Usuario.fromJson(Map<String, dynamic> json) {
    return Usuario(
      idUsuario: json['IdUsuario'] as int,
      nombre: json['Nombre'] as String,
      apellido: json['Apellido'] as String,
      correo: json['Correo'] as String,
      contrasena: json['Contrasena'] as String,
      fechaRegistro: DateTime.parse(json['FechaRegistro']),
      estado: json['Estado'] as bool,
    );
  }

  Map<String, dynamic> toJson() => {
    'IdUsuario': idUsuario,
    'Nombre': nombre,
    'Apellido': apellido,
    'Correo': correo,
    'Contrasena': contrasena,
    'FechaRegistro': fechaRegistro.toIso8601String(),
    'Estado': estado,
  };
}

Future<Usuario> createUsuario(Usuario usuario) async {
  final response = await http.post(
    Uri.parse(
      'http://10.0.2.2:9000/auth/register',
    ), // Cambia esto si estás en un dispositivo real
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(usuario.toJson()),
  );

  if (response.statusCode == 200 || response.statusCode == 201) {
    return Usuario.fromJson(jsonDecode(response.body));
  } else {
    throw Exception('Error al registrar usuario: ${response.body}');
  }
}

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final TextEditingController nombreController = TextEditingController();
  final TextEditingController apellidoController = TextEditingController();
  final TextEditingController correoController = TextEditingController();
  final TextEditingController contrasenaController = TextEditingController();

  Future<Usuario>? _futureUsuario;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text("Registro de Usuario")),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: (_futureUsuario == null) ? buildForm() : buildFutureBuilder(),
        ),
      ),
    );
  }

  Widget buildForm() {
    return Column(
      children: [
        TextField(
          controller: nombreController,
          decoration: const InputDecoration(labelText: 'Nombre'),
        ),
        TextField(
          controller: apellidoController,
          decoration: const InputDecoration(labelText: 'Apellido'),
        ),
        TextField(
          controller: correoController,
          decoration: const InputDecoration(labelText: 'Correo'),
        ),
        TextField(
          controller: contrasenaController,
          decoration: const InputDecoration(labelText: 'Contraseña'),
          obscureText: true,
        ),
        const SizedBox(height: 20),
        ElevatedButton(
          onPressed: () {
            Usuario usuario = Usuario(
              idUsuario: 0, // El backend lo debería generar
              nombre: nombreController.text,
              apellido: apellidoController.text,
              correo: correoController.text,
              contrasena: contrasenaController.text,
              fechaRegistro: DateTime.now(),
              estado: true,
            );

            setState(() {
              _futureUsuario = createUsuario(usuario);
            });
          },
          child: const Text('Registrar'),
        ),
      ],
    );
  }

  Widget buildFutureBuilder() {
    return FutureBuilder<Usuario>(
      future: _futureUsuario,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return Text('Usuario registrado: ${snapshot.data!.nombre}');
        } else if (snapshot.hasError) {
          return Text('Error: ${snapshot.error}');
        }
        return const CircularProgressIndicator();
      },
    );
  }
}
