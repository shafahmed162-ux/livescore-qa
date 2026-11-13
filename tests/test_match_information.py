import re
from playwright.sync_api import Page, expect


def test_match_information(page: Page):
    # Step 1: Open Netherlands vs Greece match
    page.goto(
        "https://www.livescore.com/en/football/uefa-nations-league/league-a-group-2/netherlands-vs-greece/1738287/",
        wait_until="domcontentloaded"
    )

    # Step 2: Verify we are on the correct match page
    expect(page).to_have_url(
        re.compile(r"/netherlands-vs-greece/1738287/?$")
    )

    # Step 3: Locate the two team names
    home_team = page.get_by_text(
        "Netherlands", exact=True
    ).first

    away_team = page.get_by_text(
        "Greece", exact=True
    ).first

    # Step 4: Verify both team names are visible
    expect(home_team).to_be_visible()
    expect(away_team).to_be_visible()

    # Step 5: Verify neither team name is empty
    assert home_team.inner_text().strip()
    assert away_team.inner_text().strip()
