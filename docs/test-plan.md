
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

Operating System: macOS
Programming Language: Python 3.14
Browser: Chromium
Automation Framework: Playwright + Pytest

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
| TC-001 | Homepage loads successfully | Passed |
| TC-002 | Football navigation works | Passed |
| TC-003 | Match page displays team names | Passed |

## 9. Exit Criteria

- Critical automated test cases execute successfully.
- Known test failures are investigated.
- Test results are documented.
- Test scripts and documentation are available on GitHub.
