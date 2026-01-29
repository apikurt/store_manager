from abc import ABC, abstractmethod
import os


class MenuBase(ABC):
    """
    Base class for all menus in the Store Manager application.
    """

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

    def exit_application(self):
        """
        Exits the application gracefully.
        """
        self.clear_screen()
        print("Exiting the application. Goodbye!")
        exit(0)
