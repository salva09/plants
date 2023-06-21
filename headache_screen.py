from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt


class HeadacheScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.create_title()

    def create_title(self):
        title = QLabel('Headache')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.grid.addWidget(title, 0, 0)
