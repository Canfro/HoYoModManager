from gbapi import Client


class ViewModel:
    """Viewmodel for the main window of the program."""

    def __init__(self) -> None:
        """Viewmodel for the main window of the program."""
        gb: Client = Client()

    def get_game_names(self) -> list[str]:
        