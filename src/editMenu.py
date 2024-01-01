from PyQt5.QtWidgets import QApplication, QWidget


class EditMenu(QWidget):
    """ EditMenu window """
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.initVar()
        self.initWindow()


    def initVar(self):
        """ initialize variables """
        self.windowWidth = 400
        self.windowHeight = 400


    def initWindow(self):
        """ initialize window """
        _averageTitlebarHeight = 30
        if (self.parent.y() + self.parent.height() + _averageTitlebarHeight + self.windowHeight) > QApplication.desktop().availableGeometry().height():
            windowYCoord = self.parent.y() - _averageTitlebarHeight - self.windowHeight
        else:
            windowYCoord = self.parent.y() + self.parent.height() + _averageTitlebarHeight
        self.setGeometry(int(self.parent.x() - (self.windowWidth - self.parent.width()) / 2), windowYCoord, self.windowWidth, self.windowHeight)
