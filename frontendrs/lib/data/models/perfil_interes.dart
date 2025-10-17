class PerfilInteresBase {
  final int idPerfil;
  final int idInteres;

  PerfilInteresBase({required this.idPerfil, required this.idInteres});

  factory PerfilInteresBase.fromJson(Map<String, dynamic> json) {
    return PerfilInteresBase(
      idPerfil: json['IdPerfil'],
      idInteres: json['IdInteres'],
    );
  }

  Map<String, dynamic> toJson() {
    return {'IdPerfil': idPerfil, 'IdInteres': idInteres};
  }
}

class PerfilInteres extends PerfilInteresBase {
  final int? idPerfilInteres;

  PerfilInteres({
    this.idPerfilInteres,
    required int idPerfil,
    required int idInteres,
  }) : super(idPerfil: idPerfil, idInteres: idInteres);

  factory PerfilInteres.fromJson(Map<String, dynamic> json) {
    return PerfilInteres(
      idPerfilInteres: json['IdPerfilInteres'],
      idPerfil: json['IdPerfil'],
      idInteres: json['IdInteres'],
    );
  }

  @override
  Map<String, dynamic> toJson() {
    return {
      'IdPerfilInteres': idPerfilInteres,
      'IdPerfil': idPerfil,
      'IdInteres': idInteres,
    };
  }
}

class PerfilInteresCreate {
  final int idPerfil;
  final int idInteres;

  PerfilInteresCreate({required this.idPerfil, required this.idInteres});

  Map<String, dynamic> toJson() {
    return {'IdPerfil': idPerfil, 'IdInteres': idInteres};
  }
}

class PerfilInteresPublic extends PerfilInteresBase {
  final int idPerfilInteres;

  PerfilInteresPublic({
    required this.idPerfilInteres,
    required int idPerfil,
    required int idInteres,
  }) : super(idPerfil: idPerfil, idInteres: idInteres);

  factory PerfilInteresPublic.fromJson(Map<String, dynamic> json) {
    return PerfilInteresPublic(
      idPerfilInteres: json['IdPerfilInteres'],
      idPerfil: json['IdPerfil'],
      idInteres: json['IdInteres'],
    );
  }

  @override
  Map<String, dynamic> toJson() {
    return {
      'IdPerfilInteres': idPerfilInteres,
      'IdPerfil': idPerfil,
      'IdInteres': idInteres,
    };
  }
}

class PerfilInteresUpdate {
  final int idPerfil;
  final int idInteres;

  PerfilInteresUpdate({required this.idPerfil, required this.idInteres});

  Map<String, dynamic> toJson() {
    return {'IdPerfil': idPerfil, 'IdInteres': idInteres};
  }
}
