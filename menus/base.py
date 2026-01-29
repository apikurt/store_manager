import os
from abc import ABC, abstractmethod


class MenuBase(ABC):
    """
    Base class for all menus in the Store Manager application.
    """

    APP_HEADER = "Store Manager"

    def __init__(self, data_manager):
        self.data_manager = data_manager

    @abstractmethod
    def run(self):
        """
        Generic runner for menu views.
        """
        pass

    def clear_screen(self):
        """
        Clears the console screen.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def show_header(self, menu_title: str) -> None:
        """
        Clears the screen and prints the global header and menu title.
        """
        self.clear_screen()
        inner_width = max(40, len(self.APP_HEADER), len(menu_title)) + 6
        border = "+" + ("-" * inner_width) + "+"
        print(border)
        print("|" + self.APP_HEADER.center(inner_width) + "|")
        print(border)
        print(menu_title.center(inner_width))
        print(("-" * len(menu_title)).center(inner_width))
        print()

    def exit_application(self):
        """
        Exits the application.
        """
        self.show_header("Exiting Application, Goodbye!")
        exit(0)
