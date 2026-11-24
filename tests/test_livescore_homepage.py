
import re

from playwright.sync_api import Page, expect


def test_livescore_homepage(page: Page):
    """
    Verify football homepage content and
    navigation are available to users.
    """

    response = page.goto(
        "https://www.livescore.com/en/",
        wait_until="domcontentloaded",
    )

    assert response is not None
    assert response.status == 200

    # Confirm the main football heading is visible.
    expect(
        page.get_by_role(
            "heading",
            name=re.compile(
                "Latest Football Scores",
                re.IGNORECASE,
            ),
            level=1,
        )
    ).to_be_visible()

    # Confirm the live football section exists.
    expect(
        page.get_by_role(
            "link",
            name="LIVE",
            exact=True,
        )
    ).to_be_visible()

    # Verify the live section points to
    # the correct destination.
    expect(
        page.get_by_role(
            "link",
            name="LIVE",
            exact=True,
        )
    ).to_have_attribute(
        "href",
        "/en/football/live/",
    )
