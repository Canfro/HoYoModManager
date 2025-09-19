import sys

from PySide6.QtWidgets import QApplication

from app.view.main_window import MainWindow


def main() -> None:
    """Main entry point of the program."""
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
