from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

import json
import sys


class MainWindow(QMainWindow):
    """ Main window """
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.initVar()
        self.initWindow()


    def initVar(self):
        """ initialize variables """
        self.configData = self.__loadConfigData()
        self.user = self.configData["config"]

        self.isTitlebarPress = False
        self.isWindowPress = False
        self.advancedOptions = self.configData[self.user]["window"]["advancedOptions"]
        self.isOpenEditMenu = self.configData[self.user]["window"]["isOpenEditMenu"]
        self.showOnTaskbar = self.configData[self.user]["window"]["showOnTaskbar"]
        self.showToolTips = self.configData[self.user]["window"]["showToolTips"]
        self.staysOnTop = self.configData[self.user]["window"]["staysOnTop"]
        self.windowHeight = self.configData[self.user]["window"]["height"]
        self.windowWidth = self.configData[self.user]["window"]["width"]

        self.backgroundType = self.configData[self.user]["background"]["type"]
        self.backgroundNormalGif = self.configData[self.user]["background"]["gif"]["normal"]
        self.backgroundBlurGif = self.configData[self.user]["background"]["gif"]["blur"]
        self.backgroundTopGif = self.configData[self.user]["background"]["gif"]["top"]
        self.backgroundGifPath = self.configData[self.user]["background"]["gif"]["path"]
        self.backgroundNormalImage = self.configData[self.user]["background"]["image"]["normal"]
        self.backgroundBlurImage = self.configData[self.user]["background"]["image"]["blur"]
        self.backgroundTopImage = self.configData[self.user]["background"]["image"]["top"]
        self.backgroundImagePath = self.configData[self.user]["background"]["image"]["path"]
        self.backgroundOpacity = self.configData[self.user]["background"]["opacity"]
        self.backgroundColor = tuple(self.configData[self.user]["background"]["color"])
        self.backgroundBorderSize = self.configData[self.user]["background"]["borderSize"]
        self.backgroundBorderColor = tuple(self.configData[self.user]["background"]["borderColor"][self.backgroundType])
        self.backgroundBorderRadius = self.configData[self.user]["background"]["borderRadius"]
        self.backgroundBorderOpacity = self.configData[self.user]["background"]["borderOpacity"]
        self.backgroundAnimation = self.configData[self.user]["background"]["animation"]
        self.backgroundAnimationCounter = self.configData[self.user]["background"]["animationCounter"]
        self.backgroundAnimationDuration = self.configData[self.user]["background"]["animationDuration"]

        self.blinkingColonVisibility = self.configData[self.user]["text"]["blinkingColonVisibility"]
        self.blinkingColonAnimation = self.configData[self.user]["text"]["blinkingColonAnimation"]
        self.clockFontSize = self.configData[self.user]["text"]["clockFontSize"]
        self.dateFontSize = self.configData[self.user]["text"]["dateFontSize"]
        self.textColor =  tuple(self.configData[self.user]["text"]["color"][self.backgroundType])
        self.textOpacity = self.configData[self.user]["text"]["opacity"]
        self.textXCoord = self.configData[self.user]["text"]["xCoord"]
        self.textYCoord = self.configData[self.user]["text"]["yCoord"]
        self.fontPath = self.configData[self.user]["text"]["fontPath"]
        self.font = self.configData[self.user]["text"]["font"]
        self.iconPath = self.configData[self.user]["text"]["iconPath"]
        self.iconSize = tuple(self.configData[self.user]["text"]["iconSize"])
        self.iconNormalColor = tuple(self.configData[self.user]["text"]["iconColor"]["normal"][self.backgroundType])
        self.iconHoverColor = tuple(self.configData[self.user]["text"]["iconColor"]["hover"][self.backgroundType])
        self.editMenu = None


    def initWindow(self):
        """ initialize window """
        screenSize = QApplication.desktop().availableGeometry()
        x = int((screenSize.width() / 2) - (self.windowWidth / 2))
        y = int(screenSize.height() / 3)

        self.setGeometry(x, y, self.windowWidth, self.windowHeight)


    def __loadConfigData(self):
        with open("src/data/config.json", "r") as data:
            return json.load(data)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
