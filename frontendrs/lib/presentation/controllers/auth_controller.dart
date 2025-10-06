import '../../data/models/usuario.dart';
import '../../data/services/auth_service.dart';

class AuthController {
  final AuthService _authService = AuthService();

  Future<Usuario> registrarUsuario(Usuario usuario) async {
    return await _authService.register(usuario);
  }
}
