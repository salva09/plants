from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QVBoxLayout, QGroupBox, QPushButton


class WelcomeScreen(QWidget):
    def __init__(self, go_to_headache):
        super().__init__()

        self.go_to_headache = go_to_headache

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.create_welcome_description()
        self.create_button_group()

    def create_welcome_description(self):
        vbox = QVBoxLayout()
        group = QGroupBox()

        description = QLabel('The program asks the user the ailments they have, and will show pictures of a medicinal '
                             'plant they can use to treat it, as well as the a data sheet containing the main '
                             'information of it.')
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignmentFlag.AlignJustify)
        description.setMaximumWidth(200)

        vbox.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        vbox.addWidget(description)
        group.setLayout(vbox)

        self.grid.addWidget(group, 0, 0)

    def create_button_group(self):
        vbox = QVBoxLayout()
        group = QGroupBox()

        title = QLabel('Please select which kind of ailment are you feeling:')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setWordWrap(True)

        headache_button = QPushButton('Headache')
        headache_button.clicked.connect(self.go_to_headache)
        flu_button = QPushButton('Flu')
        stomachache_button = QPushButton('Stomachache')
        menstrual_cramps_button = QPushButton('Menstrual Cramps')
        burns_button = QPushButton('Burns')

        vbox.addWidget(title)
        vbox.addWidget(headache_button)
        vbox.addWidget(flu_button)
        vbox.addWidget(stomachache_button)
        vbox.addWidget(menstrual_cramps_button)
        vbox.addWidget(burns_button)
        group.setLayout(vbox)

        self.grid.addWidget(group, 0, 1)
