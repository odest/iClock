from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from lib import RoundMenu, setTheme, Theme

class ContextMenu(RoundMenu):
    setTheme(Theme.DARK)

    def __init__(self, parent):
        super().__init__("", parent)
        iconPath = "src/assets/icons/"

        alignSubmenu = RoundMenu("Align...", self)
        alignSubmenu.setIcon(QIcon(f"{iconPath}align.png"))
        self.center = QAction("Center", self)
        self.center.setIcon(QIcon(f"{iconPath}center.png"))
        self.horizontallyCentered = QAction("Horizontally Centered", self)
        self.horizontallyCentered.setIcon(QIcon(f"{iconPath}horizantal.png"))
        self.verticallyCentered = QAction("Vertically Centered", self)
        self.verticallyCentered.setIcon(QIcon(f"{iconPath}vertical.png"))
        self.topLeft = QAction("Top Left", self)
        self.topLeft.setIcon(QIcon(f"{iconPath}topLeft.png"))
        self.topRight = QAction("Top Right", self)
        self.topRight.setIcon(QIcon(f"{iconPath}topRight.png"))
        self.bottomLeft = QAction("Bottom Left", self)
        self.bottomLeft.setIcon(QIcon(f"{iconPath}bottomLeft.png"))
        self.bottomRight = QAction("Bottom Right", self)
        self.bottomRight.setIcon(QIcon(f"{iconPath}bottomRight.png"))
        alignSubmenu.addActions([
            self.center, self.horizontallyCentered, self.verticallyCentered, 
            self.topLeft, self.topRight, self.bottomLeft, self.bottomRight
        ])
        self.addMenu(alignSubmenu)

        self.maximize = QAction("Maximize", self)
        self.maximize.setIcon(QIcon(f"{iconPath}maximize.png"))
        self.minimize = QAction("Minimize", self)
        self.minimize.setIcon(QIcon(f"{iconPath}minimize.png"))
        self.restore = QAction("Restore", self)
        self.restore.setIcon(QIcon(f"{iconPath}restore.png"))
        self.kill = QAction("Close", self)
        self.kill.setIcon(QIcon(f"{iconPath}close.svg"))
        self.edit = QAction("Edit", self)
        self.edit.setIcon(QIcon(f"{iconPath}edit.svg"))
        self.default = QAction("Back to Default", self)
        self.default.setIcon(QIcon(f"{iconPath}return.png"))

        self.addActions(
            [self.maximize, self.minimize, self.restore, self.kill])
        self.addSeparator()
        self.addActions(
            [self.edit, self.default])
