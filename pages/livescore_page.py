
from playwright.sync_api import Page, expect


class LiveScorePage:
    BASE_URL = "https://www.livescore.com"
    FOOTBALL_URL = f"{BASE_URL}/en/"
    HOCKEY_URL = f"{BASE_URL}/en/hockey/"

    FOOTBALL_HEADING = (
        "LiveScore - Latest Football Scores, "
        "Results, Fixtures and Tables"
    )

    def __init__(self, page: Page):
        self.page = page

        # Navigation locators
        self.football_link = page.get_by_role(
            "link",
            name="Football Football",
            exact=True
        )

        # Page content locators
        self.football_heading = page.get_by_role(
            "heading",
            name=self.FOOTBALL_HEADING,
            exact=True
        )

    def open_hockey(self):
        self.page.goto(
            self.HOCKEY_URL,
            wait_until="domcontentloaded"
        )

    
    def navigate_to_football(self):
        age_button = self.page.get_by_role(
            "button",
            name="21 & Over",
            exact=True
        )

        if age_button.is_visible():
            age_button.click()

        expect(self.football_link).to_be_visible()
        self.football_link.click()


    def verify_football_page(self):
        expect(self.page).to_have_url(self.FOOTBALL_URL)
        expect(self.football_heading).to_be_visible()
