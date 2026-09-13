import 'dart:async';

import 'package:get/get.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

class AuthService extends GetxService {
  final currentUser = Rxn<User>();

  StreamSubscription<AuthState>? _authSub;

  bool get isLoggedIn => currentUser.value != null;

  String? get email => currentUser.value?.email;

  Future<AuthService> init() async {
    attach();
    return this;
  }

  void attach() {
    final client = _client;
    if (client == null) return;

    currentUser.value = client.auth.currentUser;
    _authSub?.cancel();
    _authSub = client.auth.onAuthStateChange.listen((state) {
      currentUser.value = state.session?.user;
    });
  }

  Future<void> signUp({
    required String email,
    required String password,
  }) async {
    final client = _requireClient();
    final response = await client.auth.signUp(
      email: email.trim(),
      password: password,
    );
    currentUser.value = response.user ?? client.auth.currentUser;
  }

  Future<void> signIn({
    required String email,
    required String password,
  }) async {
    final client = _requireClient();
    final response = await client.auth.signInWithPassword(
      email: email.trim(),
      password: password,
    );
    currentUser.value = response.user;
  }

  Future<void> signOut() async {
    final client = _requireClient();
    await client.auth.signOut();
    currentUser.value = null;
  }

  Future<void> updateProfile({
    required String name,
    String country = '',
  }) async {
    final client = _client;
    if (client == null || currentUser.value == null) return;
    final response = await client.auth.updateUser(
      UserAttributes(
        data: {
          'full_name': name,
          'name': name,
          'country': country,
        },
      ),
    );
    currentUser.value = response.user ?? client.auth.currentUser;
  }

  SupabaseClient? get _client {
    try {
      return Supabase.instance.client;
    } catch (_) {
      return null;
    }
  }

  SupabaseClient _requireClient() {
    final client = _client;
    if (client == null) {
      throw AuthException('Cloud sync is unavailable right now.');
    }
    return client;
  }

  @override
  void onClose() {
    _authSub?.cancel();
    super.onClose();
  }
}
