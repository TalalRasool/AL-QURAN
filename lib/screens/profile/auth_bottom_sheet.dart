import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:get/get.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

import '../../core/constants/app_colors.dart';
import '../../core/constants/app_text_styles.dart';
import '../../core/services/auth_service.dart';
import '../../core/widgets/widgets.dart';

class AuthBottomSheet extends StatefulWidget {
  const AuthBottomSheet({super.key});

  @override
  State<AuthBottomSheet> createState() => _AuthBottomSheetState();
}

class _AuthBottomSheetState extends State<AuthBottomSheet> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _auth = Get.find<AuthService>();

  var _isSignUp = false;
  var _obscurePassword = true;
  var _isLoading = false;
  String? _error;

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  Future<void> _submit() async {
    final email = _emailController.text.trim();
    final password = _passwordController.text;
    if (email.isEmpty || !email.contains('@')) {
      setState(() => _error = 'Enter a valid email address.');
      return;
    }
    if (password.length < 6) {
      setState(() => _error = 'Password must be at least 6 characters.');
      return;
    }

    setState(() {
      _isLoading = true;
      _error = null;
    });

    try {
      if (_isSignUp) {
        await _auth.signUp(email: email, password: password);
        if (!mounted) return;
        if (_auth.currentUser.value == null) {
          Get.back();
          Get.snackbar(
            'Confirm your email',
            'We sent a confirmation link. Sign in after you confirm.',
            snackPosition: SnackPosition.BOTTOM,
          );
          return;
        }
      } else {
        await _auth.signIn(email: email, password: password);
      }
      if (!mounted) return;
      Get.back();
    } on AuthException catch (error) {
      if (!mounted) return;
      setState(() => _error = error.message);
    } catch (_) {
      if (!mounted) return;
      setState(() => _error = 'Unable to continue. Please try again.');
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(
        left: 20.w,
        right: 20.w,
        top: 12.h,
        bottom: MediaQuery.of(context).viewInsets.bottom + 20.h,
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Center(
            child: Container(
              width: 40.w,
              height: 4.h,
              decoration: BoxDecoration(
                color: AppColors.greyLight,
                borderRadius: BorderRadius.circular(4.r),
              ),
            ),
          ),
          SizedBox(height: 16.h),
          Text(
            _isSignUp ? 'Create an account' : 'Sign in',
            style: AppTextStyles.heading2,
          ),
          SizedBox(height: 6.h),
          Text(
            'Optional cloud backup for your reading progress.',
            style: AppTextStyles.bodySmall,
          ),
          SizedBox(height: 16.h),
          CustomTextField(
            controller: _emailController,
            hintText: 'Email',
            showPrefixIcon: false,
            keyboardType: TextInputType.emailAddress,
            textInputAction: TextInputAction.next,
            autofillHints: const [AutofillHints.email],
          ),
          SizedBox(height: 10.h),
          CustomTextField(
            controller: _passwordController,
            hintText: 'Password',
            showPrefixIcon: false,
            obscureText: _obscurePassword,
            textInputAction: TextInputAction.done,
            autofillHints: const [AutofillHints.password],
            suffixIcon: IconButton(
              onPressed: () =>
                  setState(() => _obscurePassword = !_obscurePassword),
              icon: Icon(
                _obscurePassword
                    ? Icons.visibility_outlined
                    : Icons.visibility_off_outlined,
                color: AppColors.textSecondary,
                size: 20.sp,
              ),
            ),
          ),
          if (_error != null) ...[
            SizedBox(height: 10.h),
            Text(
              _error!,
              style: AppTextStyles.bodySmall.copyWith(color: AppColors.error),
            ),
          ],
          SizedBox(height: 16.h),
          PrimaryButton(
            label: _isSignUp ? 'Sign Up' : 'Sign In',
            isLoading: _isLoading,
            onPressed: _submit,
          ),
          SizedBox(height: 8.h),
          Center(
            child: TextButton(
              onPressed: _isLoading
                  ? null
                  : () => setState(() {
                        _isSignUp = !_isSignUp;
                        _error = null;
                      }),
              child: Text(
                _isSignUp
                    ? 'Already have an account? Sign in'
                    : 'Need an account? Sign up',
                style: AppTextStyles.bodySmall.copyWith(
                  color: AppColors.primaryLight,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
