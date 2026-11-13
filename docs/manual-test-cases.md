
# LiveScore QA — Manual Test Cases

## Test Environment
Website: https://www.livescore.com/
Browser: Chromium
Operating System: macOS

## Manual Test Case Matrix

| ID | Test Case | Priority | Status |
|---|---|---|---|
| MTC-001 | Homepage loads | High | Not Run |
| MTC-002 | Football navigation | High | Not Run |
| MTC-003 | Hockey navigation | Medium | Not Run |
| MTC-004 | Match details | High | Not Run |
| MTC-005 | Home and away teams | High | Not Run |
| MTC-006 | Competition navigation | Medium | Not Run |
| MTC-007 | Search functionality | High | Not Run |
| MTC-008 | Live scores section | High | Not Run |
| MTC-009 | Browser back navigation | Medium | Not Run |
| MTC-010 | Responsive layout | Medium | Not Run |

---

## MTC-001: Homepage Loads

**Precondition:** Internet connection available.

**Steps:**
1. Open Chromium.
2. Navigate to https://www.livescore.com/
3. Observe whether the page loads.

**Expected Result:**
The homepage loads and displays sports content.

**Actual Result:** Not executed

**Status:** Not Run

---

## MTC-002: Football Navigation

**Precondition:** LiveScore is accessible.

**Steps:**
1. Navigate to the Hockey section.
2. Locate the Football navigation link.
3. Click Football.

**Expected Result:**
The Football homepage opens and football
content is displayed.

**Actual Result:** Not executed manually

**Status:** Not Run

---

## MTC-003: Hockey Navigation

**Steps:**
1. Open the LiveScore football homepage.
2. Click Hockey.

**Expected Result:**
The Hockey section opens and displays
hockey-related content.

**Actual Result:** Not executed

**Status:** Not Run

---

## MTC-004: Match Details

**Steps:**
1. Open the Football homepage.
2. Select an available match.
3. Open its details.

**Expected Result:**
The correct match details page opens.

**Actual Result:** Not executed manually

**Status:** Not Run

---

## MTC-005: Team Information

**Steps:**
1. Open a football match details page.
2. Identify the home team.
3. Identify the away team.

**Expected Result:**
Both participating teams are displayed.

**Actual Result:** Not executed manually

**Status:** Not Run

---

## MTC-006: Competition Navigation

**Steps:**
1. Open the Football homepage.
2. Select a listed competition.

**Expected Result:**
The corresponding competition page opens.

**Actual Result:** Not executed

**Status:** Not Run

---

## MTC-007: Search Functionality

**Steps:**
1. Locate the search feature.
2. Enter a known football team name.
3. Review the search results.

**Expected Result:**
Relevant search results appear.

**Actual Result:** Not executed

**Status:** Not Run

---

## MTC-008: Live Scores

**Steps:**
1. Open Football.
2. Select LIVE.

**Expected Result:**
The live scores section opens and
displays available live matches, or an
appropriate empty state.

**Actual Result:** Not executed

**Status:** Not Run

---

## MTC-009: Browser Back Navigation

**Steps:**
1. Open the Football homepage.
2. Navigate to another sports section.
3. Use the browser Back button.

**Expected Result:**
The previously visited page is restored.

**Actual Result:** Not executed

**Status:** Not Run

---

## MTC-010: Responsive Layout

**Steps:**
1. Open LiveScore on a desktop browser.
2. Resize the viewport to a mobile width.
3. Inspect navigation and content layout.

**Expected Result:**
Navigation and important content remain
accessible without unintended overlap.

**Actual Result:** Not executed

**Status:** Not Run
