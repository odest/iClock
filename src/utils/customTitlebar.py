from lib import StandardTitleBar
from PyQt5.QtGui import QColor


class CustomTitleBar(StandardTitleBar):
    def __init__(self, parent):
        super().__init__(parent)

        self.minBtn.setNormalColor(QColor(255, 255, 255))
        self.minBtn.setNormalBackgroundColor(QColor(150, 150, 150, 0))
        self.minBtn.setHoverColor(QColor(255, 255, 255))
        self.minBtn.setHoverBackgroundColor(QColor(150, 150, 150, 26))
        self.minBtn.setPressedColor(QColor(255, 255, 255))
        self.minBtn.setPressedBackgroundColor(QColor(150, 150, 150, 51))

        self.maxBtn.setNormalColor(QColor(255, 255, 255))
        self.maxBtn.setNormalBackgroundColor(QColor(150, 150, 150, 0))
        self.maxBtn.setHoverColor(QColor(255, 255, 255))
        self.maxBtn.setHoverBackgroundColor(QColor(150, 150, 150, 26))
        self.maxBtn.setPressedColor(QColor(255, 255, 255))
        self.maxBtn.setPressedBackgroundColor(QColor(150, 150, 150, 51))

        self.closeBtn.setNormalColor(QColor(255, 255, 255))
        self.closeBtn.setNormalBackgroundColor(QColor(150, 150, 150, 0))

        self.titleLabel.setStyleSheet("""
            QLabel{
                color: white;
                background: transparent;
                font: 16px 'Segoe UI';
                padding: 0 4px
            }
        """)
