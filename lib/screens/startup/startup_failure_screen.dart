import 'package:flutter/material.dart';

class StartupFailureScreen extends StatelessWidget {
  const StartupFailureScreen({
    super.key,
    required this.message,
    required this.isRetrying,
    required this.onRetry,
  });

  final String message;
  final bool isRetrying;
  final VoidCallback onRetry;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'Offline data could not be opened',
                textAlign: TextAlign.center,
                style: Theme.of(context).textTheme.headlineSmall,
              ),
              const SizedBox(height: 12),
              Text(
                message,
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 24),
              FilledButton(
                onPressed: isRetrying ? null : onRetry,
                child: Text(isRetrying ? 'Retrying…' : 'Retry'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
