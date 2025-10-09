from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

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
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        # Top bar
        game_layout = QHBoxLayout()
        central_layout.addLayout(game_layout)

        # Game selector
        self.game_selector: QComboBox = QComboBox()
        self.game_selector.addItems(self.vm.get_game_names())
        game_layout.addWidget(self.game_selector)

        # Path input
        self.path_input: QLineEdit = QLineEdit()
        self.path_input.setPlaceholderText("Mods path")
        game_layout.addWidget(self.path_input)

        # Horizontal splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        central_layout.addWidget(splitter, 1)

        # Characters
        self.character_list: QListWidget = QListWidget()
        self.character_list.setIconSize(QSize(64, 64))
        splitter.addWidget(self.character_list)

        # Mods
        self.mod_list: QListWidget = QListWidget()
        self.mod_list.setViewMode(QListWidget.ViewMode.IconMode)
        self.mod_list.setIconSize(QSize(128, 128))
        splitter.addWidget(self.mod_list)

        # Signals connect
        _ = self.game_selector.currentTextChanged.connect(self.on_game_changed)
        _ = self.character_list.currentTextChanged.connect(self.on_character_changed)
        _ = self.mod_list.currentTextChanged.connect(self.on_mod_changed)
        _ = self.path_input.editingFinished.connect(self.on_path_changed)

    def on_game_changed(self, name: str) -> None:
        self.path_input.setText(self.vm.get_game_path(name))
        self.character_list.clear()
        character_names = self.vm.select_game(name)
        self.character_list.addItems(character_names)
        self.mod_list.clear()

    def on_character_changed(self, name: str) -> None:
        self.mod_list.clear()
        mod_names = self.vm.select_character(name)
        self.mod_list.addItems(mod_names)

    def on_mod_changed(self, name: str) -> None:
        pass

    def on_path_changed(self) -> None:
        pass
