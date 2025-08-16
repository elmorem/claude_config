# Pre-Commit Code Review

Generate a complete diff of staged changes, then conduct a systematic review:

## 🔍 Code Quality Review
- **Bug Detection**: Scan for logic errors, edge cases, and potential runtime issues
- **Security**: Check for exposed secrets, SQL injection, XSS vulnerabilities
- **Performance**: Identify inefficient algorithms, memory leaks, or blocking operations
- **Standards**: Verify code follows project conventions and best practices

## ✅ Task Validation
- **Completion Check**: Verify all marked-complete tasks are fully implemented
- **Scope Alignment**: Ensure changes match documented requirements and specs
- **Feature Parity**: Confirm no intended functionality was accidentally removed

## 🧪 Test Coverage Analysis
- **Completeness**: Ensure all new code paths have corresponding tests
- **Quality**: Flag placeholder tests, missing assertions, or inadequate mocking
- **Regression**: Verify existing tests still cover their intended functionality
- **Failure Risk**: Identify if new changes could break existing test suites

## 📋 Final Assessment
**Pass Criteria**: All issues resolved, tests comprehensive, documentation aligned
**Recommendations**: Prioritized list of improvements before commit