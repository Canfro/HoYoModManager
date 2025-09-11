import sys

from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)

    label = QLabel("Hello World!")
    label.resize(300, 100)
    label.show()

    sys.exit(app.exec())
