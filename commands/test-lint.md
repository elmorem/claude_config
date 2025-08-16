# Test and Lint Command

Run all linting and tests that mirror the GitHub Actions CI pipeline. Execute comprehensive testing and linting across the entire codebase.

## Instructions

Execute the following steps in order, mirroring the GitHub Actions workflow:

### 1. Python Code Formatting
- Run `black` to format all Python files
- Fix any formatting issues automatically

### 2. TypeScript Linting
- Run linting for all TypeScript files using the project's ESLint configuration
- Fix any auto-fixable linting issues
- Report any remaining manual fixes needed

### 3. Backend Tests
- Run all backend tests (Python/Django/FastAPI/etc.)
- Identify and fix any failing tests
- Ensure all backend test suites pass

### 4. Frontend Tests
- Run all frontend tests (Jest/Vitest/etc.)
- Identify and fix any failing tests
- Ensure all frontend test suites pass

### 5. End-to-End Tests
- Run all E2E tests (Playwright/Cypress/etc.)
- Identify and fix any failing E2E tests
- Ensure all integration tests pass

## Execution Strategy

1. **Create a todo list** to track each phase
2. **Run each phase sequentially** - don't proceed to next phase until current phase passes
3. **Fix issues immediately** when tests fail before moving to next phase
4. **Report comprehensive results** showing pass/fail status for each phase
5. **Ensure CI/CD compatibility** by matching exact commands used in GitHub Actions

The goal is to ensure the codebase passes all checks that would run in the CI pipeline.