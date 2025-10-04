import sys

from PySide6.QtWidgets import QApplication

from app.ui.main_window import MainWindow

if __name__ == "__main__":
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()
    window.showMaximized()
    app.exec()
