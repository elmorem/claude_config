# Error Handling Optimizer

Analyze the provided code and implement comprehensive error handling following language-specific best practices:

## 🔧 Error Detection & Prevention
- **Input Validation**: Validate all user inputs, API parameters, and data types
- **Null/Undefined Checks**: Implement proper guards against null pointer exceptions
- **Type Safety**: Use static typing (TypeScript, mypy) to catch errors at compile time
- **Boundary Conditions**: Handle edge cases, empty arrays, zero values

## ⚠️ Exception Management
- **Try-Catch Blocks**: Wrap risky operations with appropriate exception handling
- **Specific Exceptions**: Catch specific error types rather than generic exceptions
- **Error Propagation**: Decide when to handle vs. bubble up errors
- **Cleanup Operations**: Ensure resources are freed in finally blocks or using statements

## 📝 Logging & Monitoring
- **Structured Logging**: Log errors with context, timestamps, and severity levels
- **Error Tracking**: Implement error reporting (Sentry, Rollbar, CloudWatch)
- **Correlation IDs**: Track errors across distributed systems
- **Performance Impact**: Log errors without blocking main execution

## 👤 User Experience
- **Graceful Degradation**: Provide fallback functionality when possible
- **User-Friendly Messages**: Show helpful, non-technical error messages
- **Loading States**: Handle async operation failures with proper UI feedback
- **Retry Mechanisms**: Implement exponential backoff for transient failures

## 🏗️ System Resilience
- **Circuit Breakers**: Prevent cascade failures in distributed systems
- **Timeouts**: Set appropriate timeouts for external calls
- **Health Checks**: Monitor system components and dependencies
- **Rollback Strategies**: Plan for quick recovery from deployment issues