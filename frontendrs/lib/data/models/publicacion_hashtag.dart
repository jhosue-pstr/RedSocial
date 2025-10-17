import 'dart:convert';
import 'publicaciones.dart';
import 'hashtag.dart';

class PublicacionHashtag {
  final int? idPublicacionHashtag;
  final int idPublicacion;
  final int idHashtag;

  final Publicaciones? publicacion;
  final Hashtag? hashtag;

  PublicacionHashtag({
    this.idPublicacionHashtag,
    required this.idPublicacion,
    required this.idHashtag,
    this.publicacion,
    this.hashtag,
  });

  factory PublicacionHashtag.fromJson(Map<String, dynamic> json) {
    return PublicacionHashtag(
      idPublicacionHashtag: json['IdPublicacionHashtag'],
      idPublicacion: json['IdPublicacion'],
      idHashtag: json['IdHashtag'],
      publicacion: json['publicacion'] != null
          ? Publicaciones.fromJson(json['publicacion'])
          : null,
      hashtag: json['hashtag'] != null
          ? Hashtag.fromJson(json['hashtag'])
          : null,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'IdPublicacionHashtag': idPublicacionHashtag,
      'IdPublicacion': idPublicacion,
      'IdHashtag': idHashtag,
      'publicacion': publicacion?.toJson(),
      'hashtag': hashtag?.toJson(),
    };
  }

  PublicacionHashtag copyWith({
    int? idPublicacionHashtag,
    int? idPublicacion,
    int? idHashtag,
    Publicaciones? publicacion,
    Hashtag? hashtag,
  }) {
    return PublicacionHashtag(
      idPublicacionHashtag: idPublicacionHashtag ?? this.idPublicacionHashtag,
      idPublicacion: idPublicacion ?? this.idPublicacion,
      idHashtag: idHashtag ?? this.idHashtag,
      publicacion: publicacion ?? this.publicacion,
      hashtag: hashtag ?? this.hashtag,
    );
  }

  @override
  String toString() => jsonEncode(toJson());
}
