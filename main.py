from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

import sys


class MainWindow(QMainWindow):
    """ Main window """
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.initVar()
        self.initWindow()


    def initVar(self):
        """ initialize variables """
        self.windowWidth = 300
        self.windowHeight = 150


    def initWindow(self):
        """ initialize window """
        screenSize = QApplication.desktop().availableGeometry()
        x = int((screenSize.width() / 2) - (self.windowWidth / 2))
        y = int(screenSize.height() / 3)

        self.setGeometry(x, y, self.windowWidth, self.windowHeight)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
