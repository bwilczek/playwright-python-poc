from playwright.sync_api import Page, expect


class GreetingPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = page.locator("#name")
        self.set_name_button = page.locator("#set_name")
        self.greeting_text = page.locator("#greeting")

    def navigate(self) -> None:
        self.page.goto("https://bwilczek.github.io/watir_pump_tutorial/greeter.html")

    def greet(self, name: str) -> None:
        self.name_input.fill(name)
        self.set_name_button.click()


def test_has_title(page: Page) -> None:
    app = GreetingPage(page)
    app.navigate()
    app.greet("Marzena")

    expect(app.greeting_text).to_contain_text("Hello Marzena!")
