from pathlib import Path

from data_manager import DataManager
from menus.main_menu import MainMenu


class Runner:
    def __init__(self):
        self.data_manager = DataManager(Path("db.json"))

    def run(self):
        current_state = MainMenu(self.data_manager)
        while current_state is not None:
            current_state = current_state.run()


if __name__ == "__main__":
    app = Runner()
    app.run()
