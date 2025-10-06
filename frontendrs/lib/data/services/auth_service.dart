import 'dart:convert';
import 'package:http/http.dart' as http;
import '../../core/constants/api.dart';
import '../models/usuario.dart';

class AuthService {
  Future<Usuario> register(Usuario usuario) async {
    final response = await http.post(
      Uri.parse('$baseUrl/auth/register'),
      headers: {'Content-Type': 'application/json; charset=UTF-8'},
      body: jsonEncode(usuario.toJson()),
    );

    if (response.statusCode == 200 || response.statusCode == 201) {
      return Usuario.fromJson(jsonDecode(response.body));
    } else {
      throw Exception('Error al registrar usuario: ${response.body}');
    }
  }
}
