from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QComboBox, QMainWindow, QVBoxLayout, QWidget

from app.vm.viewmodel import ViewModel


class MainWindow(QMainWindow):
    """Main window of the program."""

    def __init__(self) -> None:
        """Main window of the program."""
        super().__init__()

        self.vm: ViewModel = ViewModel()

        # Window
        self.setWindowTitle("HoYoModManager")
        self.resize(800, 600)
        self.setWindowIcon(QPixmap("src/assets/icon.png"))
        self.move(
            (self.screen().availableGeometry().width() - self.width()) // 2,
            (self.screen().availableGeometry().height() - self.height()) // 2,
        )

        # Central widget
        central_widget: QWidget = QWidget()
        central_layout: QVBoxLayout = QVBoxLayout()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        # Game selector
        self.game_selector: QComboBox = QComboBox()
        self.game_selector.addItems(self.vm.get_game_names())
