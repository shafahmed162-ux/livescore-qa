import re 
from playwright.sync_api import Page, expect

def test_livescore_homepage(page:page):
  # Step1: Open LiveScore football homepage
  response = page.goto(
    "https://www.livescore.com/en/football/", 
    wait_until="domcontentloaded"
  )

  # Step2: Check that the website responded
  assert response is not None
  assert response.status == 200

  # Step3: Verify the page title
  expect(page).to_have_title(
    re.compile("LiveScore", re.IGNORECASE)
  )