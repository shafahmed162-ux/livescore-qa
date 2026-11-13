
from playwright.sync_api import Page
from pages.livescore_page import LiveScorePage


def test_football_navigation(page: Page):
    livescore = LiveScorePage(page)

    livescore.open_hockey()
    livescore.navigate_to_football()
    livescore.verify_football_page()
