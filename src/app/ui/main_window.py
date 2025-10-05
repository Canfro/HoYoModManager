from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """Main window of the program."""

    def __init__(self) -> None:
        """Main window of the program."""
        super().__init__()

        # Window
        self.setWindowTitle("HoYoModManager")
        self.resize(800, 600)
        self.setWindowIcon(QPixmap("src/assets/icon.png"))
