from playwright.sync_api import Page, expect

class GreetingPage:
    def __init__(self, page):
        self.page = page
        self.name_input = page.locator('#name')
        self.set_name_button = page.locator('#set_name')
        self.greeting_text = page.locator('#greeting')

    def navigate(self):
        self.page.goto("https://bwilczek.github.io/watir_pump_tutorial/greeter.html")

    def greet(self, name):
        self.name_input.fill(name)
        self.set_name_button.click()

class ToDoListComponent:
    def __init__(self, root):
        self.root = root
        self.title = self.root.locator("xpath=//*[@role='title']")

class MultiToDoListPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://bwilczek.github.io/watir_pump_tutorial/todo_lists.html")

    def lists(self):
        return [ ToDoListComponent(list) for list in self.page.locator("xpath=//*[@role='todo_list']").all() ]

def test_has_title(page: Page):
    app = GreetingPage(page)
    app.navigate()
    app.greet("Marzena")

    expect(app.greeting_text).to_contain_text("Hello Marzena!")

def test_multi_todo_lists(page: Page):
    app = MultiToDoListPage(page)
    app.navigate()

    expect(app.lists()[0].title).to_contain_text ("Home")
