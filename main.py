from PyQt5.QtWidgets import *

from headache_screen import HeadacheScreen
from welcome_screen import WelcomeScreen


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.go_to_welcome()
        self.setLayout(self.grid)

        self.setGeometry(50, 50, 460, 260)
        self.setWindowTitle("Medicinal Plants")
        self.show()

    def go_to_welcome(self):
        self.clear_grid()
        self.grid.addWidget(WelcomeScreen(self.go_to_headache), 0, 0)

    def go_to_headache(self):
        self.clear_grid()
        self.grid.addWidget(HeadacheScreen(), 0, 0)

    def clear_grid(self):
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().deleteLater()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
