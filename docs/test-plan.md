
# LiveScore QA — Test Plan

## 1. Project Overview

This project evaluates the functionality and
reliability of the LiveScore website using
manual and automated software testing.

## 2. Testing Objectives

- Verify that key pages load correctly.
- Validate navigation between sports sections.
- Verify football match information is displayed.
- Identify and document potential defects.
- Develop reliable automated regression tests.

## 3. Scope of Testing

### In Scope
- Website homepage
- Football navigation
- Match details
- Team names and match information
- Basic user interactions
- Browser functionality

### Out of Scope
- LiveScore's internal backend systems
- Payment and betting functionality
- Mobile application testing
- Performance and load testing

## 4. Testing Tools

- Python
- Playwright
- Pytest
- Chromium
- Git and GitHub

## 5. Testing Types

### Smoke Testing
Verify that critical pages and basic features work.

### Functional Testing
Verify that website features behave as expected.

### Regression Testing
Rerun existing tests after changes to detect
unexpected failures.

### Exploratory Testing
Manually investigate website functionality and
identify possible defects.


## 6. Test Environment

### Local Testing
- Operating System: macOS
- Python: 3.14
- Framework: Playwright + Pytest
- Browsers: Chromium, Firefox, WebKit

### Continuous Integration
- Platform: GitHub Actions
- Operating System: Ubuntu Linux
- Python: 3.13
- Browsers: Chromium, Firefox, WebKit

### Test Execution
- 4 automated test scenarios
- 3 browser engines
- 12 cross-browser test executions
- Latest verified full-suite result: 12 passed, 0 failed


## 7. Risks and Limitations

- Live match data changes frequently.
- Website layout and locators may change.
- Internet connectivity can affect tests.
- Third-party website restrictions may affect automation.
- Tests cannot validate backend data accuracy without
  an independent trusted source.


## 8. Current Automated Test Cases

| ID | Test Case | Status |
|---|---|---|
| TC-001 | LiveScore homepage validation | Passed |
| TC-002 | Football navigation | Passed |
| TC-003 | Match information verification | Passed |
| TC-004 | Website smoke test | Passed |

All four tests execute across Chromium, Firefox,
and WebKit.

Latest full-suite execution:
November 24, 2026 — 12 passed, 0 failed.


## 9. Exit Criteria

- Critical automated test cases execute successfully.
- Known test failures are investigated.
- Test results are documented.
- Test scripts and documentation are available on GitHub.
