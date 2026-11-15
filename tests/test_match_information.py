
import re

from playwright.sync_api import Page, expect


def test_match_information(page: Page):
    # Step 1: Open the Netherlands vs Greece match page
    page.goto(
        "https://www.livescore.com/en/football/uefa-nations-league/league-a-group-2/netherlands-vs-greece/1738287/",
        wait_until="domcontentloaded"
    )

    # Step 2: Verify the correct match URL
    expect(page).to_have_url(
        re.compile(r"/netherlands-vs-greece/1738287/?$")
    )

    # Step 3: Locate team names using exact text
    home_team = page.get_by_text("Netherlands", exact=True)
    away_team = page.get_by_text("Greece", exact=True)

    # Step 4: Verify each team name exists and is unique
    expect(home_team).to_have_count(1)
    expect(away_team).to_have_count(1)

    # Step 5: Verify both team names are visible
    expect(home_team).to_be_visible()
    expect(away_team).to_be_visible()

    # Step 6: Verify the displayed text matches expectations
    expect(home_team).to_have_text("Netherlands")
    expect(away_team).to_have_text("Greece")
