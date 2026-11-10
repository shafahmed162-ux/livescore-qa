import re
from playwright.sync_api import Page, expect

def test_browser_opens_website(page: Page):
  # Open the Playwright website
  page.goto("https://playwright.dev/")

  # Checks that the website title contains Playwright
  expect(page).to_have_title(
    re.compile("Playwright")
  )