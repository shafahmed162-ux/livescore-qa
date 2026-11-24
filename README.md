
# LiveScore QA Automation

Automated functional and regression testing of the LiveScore
website using Python, Playwright, and Pytest.

This is an independent QA portfolio project and is not
affiliated with LiveScore.

## Project Overview

LiveScore QA demonstrates automated browser testing,
cross-browser validation, reusable page objects,
manual QA documentation, and continuous integration
using GitHub Actions.

The project focuses on testing key user journeys
within the LiveScore football website.

## Technology Stack

- Python
- Playwright
- Pytest
- pytest-playwright
- pytest-html
- Git and GitHub
- GitHub Actions

## Automated Test Coverage

| Test | Description |
|------|-------------|
| Website Smoke Test | Checks HTTP response, URL, title, and visible football content |
| Football Navigation | Navigates from Hockey to Football and verifies the destination |
| Football Homepage | Verifies football content and the LIVE navigation link |
| Match Information | Verifies participating teams on a football match page |

Each scenario runs against Chromium, Firefox, and WebKit.

## Latest Local Test Results

Execution date: November 24, 2026

| Browser | Passed | Failed |
|---------|--------|--------|
| Chromium | 4 | 0 |
| Firefox | 4 | 0 |
| WebKit | 4 | 0 |
| Total | 12 | 0 |

All 12 tests passed during the latest reported full-suite
execution. The homepage test was subsequently improved
and passed individually across all three browsers.

## Project Structure

```text
livescore-qa/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
├── docs/
│   ├── manual-test-cases.md
│   ├── test-plan.md
│   └── bug-report-template.md
├── pages/
│   ├── __init__.py
│   └── livescore_page.py
├── reports/
├── tests/
│   ├── test_browser.py
│   ├── test_football_navigation.py
│   ├── test_livescore_homepage.py
│   └── test_match_information.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/shafahmed162-ux/livescore-qa.git
cd livescore-qa
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Install supported browsers:

```bash
python -m playwright install chromium firefox webkit
```

## Running Tests

Run the default Chromium tests:

```bash
python -m pytest -v
```

Run all three browsers:

```bash
python -m pytest -v \
  --browser chromium \
  --browser firefox \
  --browser webkit
```

Run with the browser window visible:

```bash
python -m pytest -v --headed
```

## HTML Test Reports

Generate a standalone HTML report:

```bash
mkdir -p reports

python -m pytest tests/ -v \
  --browser chromium \
  --browser firefox \
  --browser webkit \
  --html=reports/cross-browser-report.html \
  --self-contained-html
```

Open the generated report on macOS:

```bash
open reports/cross-browser-report.html
```

## Page Object Model

The project uses the Page Object Model (POM)
to separate browser interactions from test assertions.

The `LiveScorePage` class contains reusable functionality
for opening pages, navigating between sports sections,
and verifying the football homepage.

This design improves readability and reduces repeated
browser interaction code.

## Continuous Integration

GitHub Actions automatically executes the cross-browser
test suite when:

- Changes are pushed to the main branch
- Pull requests target main
- The workflow is manually triggered

The workflow uses Ubuntu and Python 3.13.

It also captures Playwright screenshots and traces when
tests fail, helping investigate potential regressions.

Workflow:
`.github/workflows/playwright-tests.yml`

## Manual QA Documentation

The project includes:

- [Test Plan](docs/test-plan.md)
- [Manual Test Cases](docs/manual-test-cases.md)
- [Bug Report Template](docs/bug-report-template.md)

Ten manual test cases have been documented.
Four have been executed and passed; six remain unexecuted.

An unresolved observation involving a persistent loading
placeholder is recorded in the manual test documentation.
It has not been confirmed as an application defect.

## Known Limitations

- LiveScore is a third-party website that may change.
- Historical match pages may become unavailable.
- Dynamic content and overlays can affect automation.
- Some selectors may require maintenance over time.
- Network conditions may affect browser tests.
- Test results do not independently verify score accuracy.
- Performance, mobile apps, and backend systems are
  outside the current testing scope.

## Skills Demonstrated

- Functional and smoke testing
- Automated regression testing
- Cross-browser testing
- Playwright browser automation
- Python test development
- Page Object Model architecture
- Test reporting and debugging
- Manual test planning and documentation
- GitHub Actions continuous integration
```

## Step 2 — Fix the bug report filename

Your earlier file listing showed `docs/bug-report-template.d` rather than `.md`. If that is still the filename, run:

<CodeBlock language="bash">mv docs/bug-report-template.d docs/bug-report-template.md