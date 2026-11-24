
import re

from playwright.sync_api import Page, expect


def test_browser_opens_website(page: Page):
    """
    Verify that the LiveScore football homepage
    loads successfully.
    """

    response = page.goto(
        "https://www.livescore.com/en/",
        wait_until="domcontentloaded",
    )

    # Verify the website responds successfully.
    assert response is not None
    assert response.status == 200, (
        f"Expected HTTP 200, got {response.status}"
    )

    # Verify the canonical football homepage URL.
    expect(page).to_have_url(
        "https://www.livescore.com/en/"
    )

    # Verify the website title.
    expect(page).to_have_title(
        re.compile("LiveScore", re.IGNORECASE)
    )

    # Verify meaningful football homepage content.
    football_heading = page.get_by_role(
        "heading",
        name=re.compile(
            "Latest Football Scores",
            re.IGNORECASE,
        ),
        level=1,
    )

    expect(football_heading).to_be_visible()
