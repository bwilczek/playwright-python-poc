Proof of concept: building Page Object model with reusable, nestable components using `Playwright` in `Python`.

App under test: https://bwilczek.github.io/watir_pump_tutorial/todo_lists.html

Build Page Object model with the following components:

* MultiToDoListsPage - contains many lists
* ToDoList - contains title, many items and means to add a new item
* ToDoListItem - contains title and mean to remove oneself

See `todo_lists_page_test.py` for example usage.
