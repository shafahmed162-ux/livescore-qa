from playwright.sync_api import Page, expect


class LiveScorePage:
    def __init__(self, page: Page):
        self.page = page
        self.football_link = page.get_by_role(
            "link",
            name="Football Football",
            exact=True
        )

    def open_hockey(self):
        self.page.goto(
            "https://www.livescore.com/en/hockey/",
            wait_until="domcontentloaded"
        )

    def navigate_to_football(self):
        expect(self.football_link).to_be_visible()
        self.football_link.click()

    def verify_football_page(self):
        expect(self.page).to_have_url(
            "https://www.livescore.com/en/"
        )

        expect(
            self.page.get_by_role(
                "heading",
                name="LiveScore - Latest Football Scores, Results, Fixtures and Tables"
            )
        ).to_be_visible()
