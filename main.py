from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import Qt, QTimer, QTime

from datetime import datetime
import json
import sys


class MainWindow(QMainWindow):
    """ Main window """
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.initVar()
        self.initWindow()
        self.initWidgets()
        self.setWidgets()


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
        self.backgroundAnimationFrameCount = self.configData[self.user]["background"]["frameCount"]
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


    def initWidgets(self):
        """ initialize widgets """
        self.backgroundLayer = QLabel(self)
        self.backgroundLayer.setScaledContents(True)
        self.backgroundLayer.setGeometry(0, 0, self.windowWidth, self.windowHeight)

        self.clockText = QLabel(self)
        self.clockText.setAlignment(Qt.AlignCenter)
        self.clockText.setScaledContents(True)

        self.blinkingColonText = QLabel(self)
        self.blinkingColonText.setAlignment(Qt.AlignCenter)
        self.blinkingColonText.setScaledContents(True)

        self.topLayer = QLabel(self)
        self.topLayer.setScaledContents(True)
        self.topLayer.setGeometry(0, 0, self.windowWidth, self.windowHeight)

        self.borderLayer = QLabel(self)
        self.borderLayer.setScaledContents(True)
        self.borderLayer.setGeometry(0, 0, self.windowWidth, self.windowHeight)
        self.borderLayer.setStyleSheet(f'background-color: transparent; border: {self.backgroundBorderSize}px solid rgba{self.backgroundBorderColor}; border-radius: {self.backgroundBorderRadius}')

        self.dateText = QLabel(self)
        self.dateText.setVisible(False)
        self.dateText.setAlignment(Qt.AlignCenter)
        self.dateText.setScaledContents(True)
        self.dateText.setStyleSheet(f'background-color: transparent; color: rgba{self.textColor};')
        self.dateText.setGeometry(0,-15, self.windowWidth, self.windowHeight)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setContentsMargins(10,80,10,10)
        self.centralWidget.installEventFilter(self)
        self.buttons = []

        self.editButton = QLabel(self)
        self.editButton.setVisible(False)
        self.buttonLayout.addWidget(self.editButton)
        self.buttons.append(self.editButton)
        self.editButton.installEventFilter(self)

        self.moveButton = QLabel(self)
        self.moveButton.setVisible(False)
        self.buttonLayout.addWidget(self.moveButton)
        self.buttons.append(self.moveButton)
        self.moveButton.installEventFilter(self)

        self.closeButton = QLabel(self)
        self.closeButton.setVisible(False)
        self.buttonLayout.addWidget(self.closeButton)
        self.buttons.append(self.closeButton)
        self.closeButton.installEventFilter(self)

        self.centralWidget.setLayout(self.buttonLayout)
        self.setCentralWidget(self.centralWidget)

        self.clockTimer = QTimer(self)
        self.clockTimer.timeout.connect(self.updateTime)
        self.clockTimer.start(500)


    def setWidgets(self):
        """ set widgets """
        fontID = QFontDatabase.addApplicationFont(f'{self.fontPath}{self.font}')
        self.fontFamily = QFontDatabase.applicationFontFamilies(fontID)[0]

        self.clockFont = QFont(self.fontFamily, self.clockFontSize)
        self.dateFont = QFont(self.fontFamily, self.dateFontSize)

        currentTime = QTime.currentTime()
        hour = str(currentTime.hour()).zfill(2)
        minute = str(currentTime.minute()).zfill(2)

        currentDate = datetime.now()
        dateString = currentDate.strftime("%d/%m/%Y")
        dayName = currentDate.strftime("%A")
        self.dateText.setText(f'{dateString}\n{dayName}')

        if self.blinkingColonAnimation == True:
            self.clockText.setText(f"{hour} {minute}")
            self.blinkingColonText.setText(":")
        else:
            self.clockText.setText(f"{hour}:{minute}")

        self.clockText.setFont(self.clockFont)
        self.clockText.setStyleSheet(f'background-color: transparent; color: rgba{self.textColor};')
        self.clockText.setGeometry(self.textXCoord, self.textYCoord, self.windowWidth, self.windowHeight)

        self.blinkingColonText.setFont(self.clockFont)
        self.blinkingColonText.setStyleSheet(f'background-color: transparent; color: rgba{self.textColor};')
        self.blinkingColonText.setGeometry(self.textXCoord, self.textYCoord, self.windowWidth, self.windowHeight)

        self.updateWidgets()
        if self.backgroundType == "Gif":
            self.animationTimer = QTimer(self)
            self.animationTimer.timeout.connect(self.updateAnimation)
            self.animationTimer.start(self.backgroundAnimationDuration)


    def updateWidgets(self):
        """ update widgets """
        if self.backgroundType == "Gif":
            self.backgroundLayer.setStyleSheet(f"border-image: url('{self.backgroundGifPath}{self.backgroundNormalGif}bg{self.backgroundAnimationCounter}.png'); border-radius:{self.backgroundBorderRadius}px;")
            self.topLayer.setStyleSheet(f"background-color: transparent; border-image: url('{self.backgroundGifPath}{self.backgroundTopGif}'); border-radius:{self.backgroundBorderRadius}px;")
            self.borderLayer.setStyleSheet(f'background-color: transparent; border: {self.backgroundBorderSize}px solid rgba{self.backgroundBorderColor}; border-radius: {self.backgroundBorderRadius}')

        elif self.backgroundType == "Image":
            self.backgroundLayer.setStyleSheet(f"border-image: url('{self.backgroundImagePath}{self.backgroundNormalImage}'); border-radius:{self.backgroundBorderRadius}px;")
            self.topLayer.setStyleSheet(f"background-color: transparent; border-image: url('{self.backgroundImagePath}{self.backgroundTopImage}'); border-radius:{self.backgroundBorderRadius}px;")
            self.borderLayer.setStyleSheet(f'background-color: transparent; border: {self.backgroundBorderSize}px solid rgba{self.backgroundBorderColor}; border-radius: {self.backgroundBorderRadius}')
            if self.blinkingColonAnimation == True:
                self.clockText.setGeometry(self.textXCoord, self.textYCoord - 10, self.windowWidth, self.windowHeight)
                self.blinkingColonText.setGeometry(self.textXCoord, self.textYCoord - 10, self.windowWidth, self.windowHeight)
            else:
                self.clockText.setGeometry(self.textXCoord, self.textYCoord - 10, self.windowWidth, self.windowHeight)

        elif self.backgroundType == "Color":
            self.backgroundLayer.setStyleSheet(f"background-color: rgba{self.backgroundColor}; border-radius:{self.backgroundBorderRadius}px;")
            self.topLayer.setStyleSheet(f"background-color: transparent; border-radius:{self.backgroundBorderRadius}px;")
            self.borderLayer.setStyleSheet(f'background-color: transparent; border: {self.backgroundBorderSize}px solid rgba{self.backgroundBorderColor}; border-radius: {self.backgroundBorderRadius}')


    def updateAnimation(self):
        """ update background gif frame animation """
        self.backgroundLayer.setStyleSheet(f"border-image: url('{self.backgroundGifPath}{self.backgroundNormalGif}bg{self.backgroundAnimationCounter}.png'); border-radius:{self.backgroundBorderRadius};")
        self.topLayer.setStyleSheet(f"background-color: transparent; border-image: url('{self.backgroundGifPath}{self.backgroundTopGif}'); border-radius:{self.backgroundBorderRadius}px;")
        self.borderLayer.setStyleSheet(f'background-color: transparent; border: {self.backgroundBorderSize}px solid rgba{self.backgroundBorderColor}; border-radius: {self.backgroundBorderRadius}')

        self.backgroundAnimationCounter+=1
        if self.backgroundAnimationCounter == self.backgroundAnimationFrameCount:
            self.backgroundAnimationCounter = 1


    def updateTime(self):
        """ update time and blinking colon animation """
        currentTime = QTime.currentTime()
        hour = str(currentTime.hour()).zfill(2)
        minute = str(currentTime.minute()).zfill(2)

        if self.blinkingColonAnimation == True:
            self.clockText.setText(f"{hour} {minute}")
            self.clockText.setStyleSheet(f'background-color: transparent; color: rgba{self.textColor};')
            self.blinkingColonText.setStyleSheet(f'background-color: transparent; color: rgba{self.textColor};')
            if self.blinkingColonVisibility == True:
                self.blinkingColonText.setText(" ")
                self.blinkingColonVisibility = False
            else:
                self.blinkingColonText.setText(":")
                self.blinkingColonVisibility = True
        else:
            self.blinkingColonVisibility = True
            self.blinkingColonText.setText("")
            self.clockText.setStyleSheet(f'background-color: transparent; color: rgba{self.textColor};')
            self.clockText.setText(f"{hour}:{minute}")


    def __loadConfigData(self):
        """ load configuration data from json """
        with open("src/data/config.json", "r") as data:
            return json.load(data)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
