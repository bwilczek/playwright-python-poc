from playwright.sync_api import Locator, Page, expect


class ToDoListItemComponent:
    def __init__(self, root: Locator):
        self.root = root
        self.name = self.root.locator("xpath=./*[@role='name']")
        self.remove_button = self.root.locator("xpath=./*[@role='rm']")

    def remove(self) -> None:
        self.remove_button.click()


class ToDoListComponent:
    def __init__(self, root: Locator):
        self.root = root
        self.title = self.root.locator("xpath=./*[@role='title']")
        self.add_button = self.root.locator("xpath=./*[@role='add']")
        self.new_item_input = self.root.locator("xpath=./*[@role='new_item']")

    @property
    def items(self) -> dict[str:ToDoListItemComponent]:
        items_list = [ToDoListItemComponent(tdl) for tdl in self.root.get_by_role("listitem").all()]
        return {item.name.text_content(): item for item in items_list}

    @property
    def items_as_text(self) -> list[str]:
        return list(self.items.keys())

    def add_item(self, item: str) -> None:
        self.new_item_input.fill(item)
        self.add_button.click()


class MultiToDoListPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self) -> None:
        self.page.goto("https://bwilczek.github.io/watir_pump_tutorial/todo_lists.html")

    @property
    def lists(self) -> dict[str, ToDoListComponent]:
        locators_list = [ToDoListComponent(tdl) for tdl in self.page.locator("xpath=//*[@role='todo_list']").all()]
        return {tdl.title.text_content(): tdl for tdl in locators_list}


def test_multi_todo_lists(page: Page) -> None:
    app = MultiToDoListPage(page)
    app.navigate()

    expect(app.lists["Home"].title).to_contain_text("Home")
    expect(app.lists["Home"].items["Dishes"].name).to_be_visible()

    app.lists["Home"].add_item("Shopping")
    assert "Shopping" in app.lists["Home"].items_as_text

    app.lists["Home"].items["Vacuum"].remove()
    assert "Vacuum" not in app.lists["Home"].items_as_text
