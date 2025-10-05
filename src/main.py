import sys

from PySide6.QtWidgets import QApplication

from app.ui.main_window import MainWindow

if __name__ == "__main__":
    # App
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()

    # Screen
    screen = app.primaryScreen()
    screen_geometry = screen.availableGeometry()

    # Main window initial conditions
    window.move(
        (screen_geometry.width() - window.width()) // 2,
        (screen_geometry.height() - window.height()) // 2,
    )
    window.show()

    # Execute app
    app.exec()
