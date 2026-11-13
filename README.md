# LiveScore QA Automation

A beginner QA automation portfolio project
using Python, Playwright, and Pytest.

## Project Overview
This project focuses on automated functional
testing of the LiveScore website.

## Technologies
- Python
- Playwright
- Pytest
- Git and GitHub

## Current Progress
- Python environment configured
- Playwright and Pytest installed
- First browser automation test created

## Future Goals
- LiveScore homepage testing
- Football navigation testing
- Functional UI testing
- Bug reporting and documentation

## Running Tests

1. Install dependencies:
   python -m pip install -r requirements.txt

2. Install the Chromium browser:
   python -m playwright install chromium

3. Run tests:
   python -m pytest -v --headed

## Automated Test Cases

### TC-001: LiveScore Football Homepage

**Test Type:** Smoke Testing

**Objective:**
Verify that the LiveScore football homepage
loads successfully and displays the expected title.

**Preconditions:**
- Python environment configured
- Playwright and Pytest installed
- Chromium browser installed
- Internet connection available

**Test Steps:**
1. Launch Chromium using Playwright.
2. Navigate to https://www.livescore.com/en/football/
3. Verify the HTTP response status is 200.
4. Verify that the page title contains "LiveScore".

**Expected Results:**
- Website responds with HTTP 200.
- Page title contains "LiveScore".
- No assertion failures occur.

**Actual Results:**
- LiveScore returned HTTP 200.
- Page title assertion passed.
- Pytest completed with 1 passed and 1 warning.

**Test Status:** PASSED

**Execution Date:** November 10, 2026

**Automation Tools:** Python, Playwright, Pytest

**Execution Browser:** Chromium

## Automated Test Coverage

| ID | Test Case | Latest Result |
|---|---|---|
| TC-001 | LiveScore Homepage | Passed |
| TC-002 | Football Navigation | Passed |
| TC-003 | Match Information | Passed |

## Framework Architecture

The project uses the Page Object Model (POM)
design pattern to separate page interactions
from test logic.

### Project Structure

- `pages/` - Reusable page objects
- `tests/` - Automated test scripts
- `docs/` - Manual testing documentation

### Implemented Features

- Browser automation with Playwright
- Test execution with Pytest
- Football homepage validation
- Football navigation testing
- Match information verification
- Reusable page object for football navigation

## QA Documentation

- [Test Plan](docs/test-plan.md)
- [Manual Test Cases](docs/manual-test-cases.md)
- [Bug Report Template](docs/bug-report-template.md)

## Current Limitations

- Tests currently run using Chromium.
- Match content may change over time.
- Some locators require further refinement.
- A Pytest dependency deprecation warning remains.
- API testing and CI/CD are planned future improvements.