from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLabel

from lib import CardWidget, SwitchButton



class ListCard(CardWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.title = title
        self.setFixedHeight(48)

        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.setContentsMargins(20, 11, 11, 11)
        self.mainLayout.setSpacing(15)

        self.title = QLabel(self.title, self)
        self.title.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.mainLayout.addWidget(self.title, 0, Qt.AlignVCenter)

        self.switch = SwitchButton(self)
        self.mainLayout.addStretch(1)
        self.mainLayout.addWidget(self.switch, 0, Qt.AlignRight)
