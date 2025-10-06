import 'package:flutter/material.dart';
import '../../data/models/usuario.dart';
import '../controllers/auth_controller.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});

  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final _controller = AuthController();
  final _nombre = TextEditingController();
  final _apellido = TextEditingController();
  final _correo = TextEditingController();
  final _contrasena = TextEditingController();

  Future<Usuario>? _futureUsuario;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Registro de Usuario")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: (_futureUsuario == null) ? _buildForm() : _buildFutureBuilder(),
      ),
    );
  }

  Widget _buildForm() {
    return Column(
      children: [
        TextField(
          controller: _nombre,
          decoration: const InputDecoration(labelText: 'Nombre'),
        ),
        TextField(
          controller: _apellido,
          decoration: const InputDecoration(labelText: 'Apellido'),
        ),
        TextField(
          controller: _correo,
          decoration: const InputDecoration(labelText: 'Correo'),
        ),
        TextField(
          controller: _contrasena,
          decoration: const InputDecoration(labelText: 'Contraseña'),
          obscureText: true,
        ),
        const SizedBox(height: 20),
        ElevatedButton(
          onPressed: () {
            final usuario = Usuario(
              idUsuario: 0,
              nombre: _nombre.text,
              apellido: _apellido.text,
              correo: _correo.text,
              contrasena: _contrasena.text,
              fechaRegistro: DateTime.now(),
              estado: true,
            );
            setState(() {
              _futureUsuario = _controller.registrarUsuario(usuario);
            });
          },
          child: const Text('Registrar'),
        ),
      ],
    );
  }

  Widget _buildFutureBuilder() {
    return FutureBuilder<Usuario>(
      future: _futureUsuario,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return Text('✅ Usuario registrado: ${snapshot.data!.nombre}');
        } else if (snapshot.hasError) {
          return Text('❌ Error: ${snapshot.error}');
        }
        return const CircularProgressIndicator();
      },
    );
  }
}
