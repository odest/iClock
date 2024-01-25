from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QSizeGrip, QGraphicsOpacityEffect
from PyQt5.QtGui import QFontDatabase, QFont, QImage, QPixmap, QPainter, QResizeEvent, QContextMenuEvent
from PyQt5.QtCore import Qt, QTimer, QTime, QRect, QEvent, QByteArray, QSize
from PyQt5.QtSvg import QSvgRenderer
from PyQt5 import QtCore

from src import EditMenu, SideGrip, ContextMenu
from lib import ToolTipFilter

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
        self.updateTaskbarEvent(self)
        self.updateStaysOnTopEvent(self)


    def initVar(self):
        """ initialize variables """
        self.configData = self.__loadConfigData()
        self.user = self.configData["config"]

        self.isTitlebarPress = False
        self.isWindowPress = False
        self.backgroundType = self.configData[self.user]["background"]["type"]
        self.advancedOptions = self.configData[self.user]["window"]["advancedOptions"]
        self.isOpenEditMenu = self.configData[self.user]["window"]["isOpenEditMenu"]
        self.showOnTaskbar = self.configData[self.user]["window"]["showOnTaskbar"]
        self.showToolTips = self.configData[self.user]["window"]["showToolTips"]
        self.staysOnTop = self.configData[self.user]["window"]["staysOnTop"]
        self.windowHeight = self.configData[self.user]["window"]["size"][self.backgroundType][0]
        self.windowWidth = self.configData[self.user]["window"]["size"][self.backgroundType][1]

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
        self.backgroundCustomGifCount = self.configData[self.user]["background"]["customGifCount"]

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
        self.__loadSvgContent()
        self.editMenu = None
        self._gripSize = 8


    def initWindow(self):
        """ initialize window """
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        screenSize = QApplication.desktop().availableGeometry()
        x = int((screenSize.width() / 2) - (self.windowWidth / 2))
        y = int(screenSize.height() / 3)

        self.setGeometry(x, y, self.windowWidth, self.windowHeight)


    def initWidgets(self):
        """ initialize widgets """
        self.backgroundLayer = QLabel(self)
        self.backgroundLayer.setScaledContents(True)
        self.backgroundLayer.setGeometry(0, 0, self.windowWidth, self.windowHeight)
        self.backgroundLayerOpacityEffect = QGraphicsOpacityEffect()

        self.clockText = QLabel(self)
        self.clockText.setAlignment(Qt.AlignCenter)
        self.clockText.setScaledContents(True)

        self.blinkingColonText = QLabel(self)
        self.blinkingColonText.setAlignment(Qt.AlignCenter)
        self.blinkingColonText.setScaledContents(True)

        self.topLayer = QLabel(self)
        self.topLayer.setScaledContents(True)
        self.topLayer.setGeometry(0, 0, self.windowWidth, self.windowHeight)
        self.topLayerOpacityEffect = QGraphicsOpacityEffect()

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

        self.updateToolTips()

        self.updateSVG((255, 255, 255), self.iconNormalColor)
        self.updateBackgroundOpacity(self.backgroundOpacity)

        self.centralWidget.setLayout(self.buttonLayout)
        self.setCentralWidget(self.centralWidget)

        self.clockTimer = QTimer(self)
        self.clockTimer.timeout.connect(self.updateTime)
        self.clockTimer.start(500)

        self.sideGrips = [SideGrip(self, Qt.LeftEdge), SideGrip(self, Qt.TopEdge), SideGrip(self, Qt.RightEdge), SideGrip(self, Qt.BottomEdge), ]
        self.cornerGrips = [QSizeGrip(self) for i in range(4)]
        [self.cornerGrips[i].setStyleSheet("background-color: transparent;") for i in range(4)]

        self.installEventFilter(self)


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

        if self.isOpenEditMenu:
            self.openEditMenu()


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


    def updateGrips(self):
        self.setContentsMargins(*[self._gripSize] * 4)

        outRect = self.rect()
        inRect = outRect.adjusted(self._gripSize, self._gripSize,
            -self._gripSize, -self._gripSize)

        self.cornerGrips[0].setGeometry(
            QRect(outRect.topLeft(), inRect.topLeft()))
        self.cornerGrips[1].setGeometry(
            QRect(outRect.topRight(), inRect.topRight()).normalized())
        self.cornerGrips[2].setGeometry(
            QRect(inRect.bottomRight(), outRect.bottomRight()))
        self.cornerGrips[3].setGeometry(
            QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())

        self.sideGrips[0].setGeometry(
            0, inRect.top(), self._gripSize, inRect.height())
        self.sideGrips[1].setGeometry(
            inRect.left(), 0, inRect.width(), self._gripSize)
        self.sideGrips[2].setGeometry(
            inRect.left() + inRect.width(), 
            inRect.top(), self._gripSize, inRect.height())
        self.sideGrips[3].setGeometry(
            self._gripSize, inRect.top() + inRect.height(), 
            inRect.width(), self._gripSize)


    def updateSVG(self, oldColor, newColor):
        self.editContent = self.editContent.replace(f'stroke="rgb{oldColor}"', f'stroke="rgb{newColor}"')
        self.editRenderer.load(QByteArray(self.editContent.encode()))
        self.editButton.setPixmap(self.renderSVG(self.editRenderer))

        self.moveContent = self.moveContent.replace(f'stroke="rgb{oldColor}"', f'stroke="rgb{newColor}"')
        self.moveRenderer.load(QByteArray(self.moveContent.encode()))
        self.moveButton.setPixmap(self.renderSVG(self.moveRenderer))

        self.closeContent = self.closeContent.replace(f'stroke="rgb{oldColor}"', f'stroke="rgb{newColor}"')
        self.closeRenderer.load(QByteArray(self.closeContent.encode()))
        self.closeButton.setPixmap(self.renderSVG(self.closeRenderer))


    def updateBackgroundOpacity(self, value):
        self.backgroundLayerOpacityEffect.setOpacity(value * 0.01)
        self.backgroundLayer.setGraphicsEffect(self.backgroundLayerOpacityEffect)
        self.topLayerOpacityEffect.setOpacity(value * 0.01)
        self.topLayer.setGraphicsEffect(self.topLayerOpacityEffect)


    def updateTaskbarEvent(self, window):
        if self.showOnTaskbar:
            window.setWindowFlag(Qt.Tool, False)
        else:
            window.setWindowFlag(Qt.Tool, True)
        self.show()
        if self.editMenu:
            self.editMenu.show()


    def updateStaysOnTopEvent(self, window):
        if self.staysOnTop:
            window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)
        else:
            window.setWindowFlags(window.windowFlags() & ~Qt.WindowStaysOnTopHint)
        self.show()
        if self.editMenu:
            self.editMenu.show()


    def updateToolTips(self):
        self.setToolTip(self.editButton, 'Open Edit Page')
        self.setToolTip(self.moveButton, 'Move The Widget')
        self.setToolTip(self.closeButton, 'Close The Widget')


    def setToolTip(self, widget, text):
        if self.showToolTips:
            widget.setToolTip(text)
            widget.installEventFilter(ToolTipFilter(widget))
            widget.setToolTipDuration(2000)
        else:
            widget.setToolTip("")


    def eventFilter(self, object, event):
        if object == self.centralWidget:
            if event.type() == QEvent.Enter:
                if self.backgroundType == "Gif":
                    self.animationTimer.stop()
                    self.topLayer.setStyleSheet(f"background-color: transparent; border-image: url('{self.backgroundGifPath}{self.backgroundBlurGif}'); border-radius:{self.backgroundBorderRadius};")

                elif self.backgroundType == "Image":
                    self.topLayer.setStyleSheet(f"background-color: transparent; border-image: url('{self.backgroundImagePath}{self.backgroundBlurImage}'); border-radius:{self.backgroundBorderRadius};")

                elif self.backgroundType == "Color":
                    self.topLayer.setStyleSheet(f"background-color: rgba{self.backgroundColor}; border-radius:{self.backgroundBorderRadius};")

                self.dateText.setVisible(True)
                self.editButton.setVisible(True)
                self.moveButton.setVisible(True)
                self.closeButton.setVisible(True)
                self.updateBackgroundOpacity(100)

            elif event.type() == QEvent.Leave:
                if self.backgroundType == "Gif":
                    if self.backgroundAnimation == True:
                        self.animationTimer.start(self.backgroundAnimationDuration)
                    self.topLayer.setStyleSheet(f"background-color: transparent; border-image: url('{self.backgroundGifPath}{self.backgroundTopGif}'); border-radius:{self.backgroundBorderRadius};")

                elif self.backgroundType == "Image":
                    self.topLayer.setStyleSheet(f"background-color: transparent; border-image: url('{self.backgroundImagePath}{self.backgroundTopImage}'); border-radius:{self.backgroundBorderRadius};")

                elif self.backgroundType == "Color":
                    self.topLayer.setStyleSheet(f"background-color: transparent; border-radius:{self.backgroundBorderRadius};")

                self.dateText.setVisible(False)
                self.editButton.setVisible(False)
                self.moveButton.setVisible(False)
                self.closeButton.setVisible(False)
                self.updateBackgroundOpacity(self.backgroundOpacity)

        elif object == self.editButton:
            if event.type() == QEvent.Enter:
                self.editContent = self.editContent.replace(f'stroke="rgb{self.iconNormalColor}"', f'stroke="rgb{self.iconHoverColor}"')
                self.editRenderer.load(QByteArray(self.editContent.encode()))
                self.editButton.setPixmap(self.renderSVG(self.editRenderer))

            elif event.type() == QEvent.Leave:
                self.editContent = self.editContent.replace(f'stroke="rgb{self.iconHoverColor}"', f'stroke="rgb{self.iconNormalColor}"')
                self.editRenderer.load(QByteArray(self.editContent.encode()))
                self.editButton.setPixmap(self.renderSVG(self.editRenderer))

            elif event.type() == QEvent.MouseButtonPress:
                if event.button() == Qt.LeftButton:
                    self.openEditMenu()

        elif object == self.moveButton:
            if event.type() == QEvent.Enter:
                self.moveContent = self.moveContent.replace(f'stroke="rgb{self.iconNormalColor}"', f'stroke="rgb{self.iconHoverColor}"')
                self.moveRenderer.load(QByteArray(self.moveContent.encode()))
                self.moveButton.setPixmap(self.renderSVG(self.moveRenderer))

            elif event.type() == QEvent.Leave:
                self.moveContent = self.moveContent.replace(f'stroke="rgb{self.iconHoverColor}"', f'stroke="rgb{self.iconNormalColor}"')
                self.moveRenderer.load(QByteArray(self.moveContent.encode()))
                self.moveButton.setPixmap(self.renderSVG(self.moveRenderer))

            elif event.type() == QEvent.MouseButtonPress:
                if event.button() == Qt.LeftButton and self.isWindowPress == False:
                    self.oldpos = event.globalPos()
                    self.oldwindowpos = self.pos()
                    self.isTitlebarPress = True
                return True

            elif event.type() == QEvent.MouseButtonRelease:
                self.isTitlebarPress = False
                return True

            elif event.type() == QEvent.MouseMove:
                if (self.isTitlebarPress):
                    distance = event.globalPos()-self.oldpos
                    newwindowpos = self.oldwindowpos + distance
                    self.move(newwindowpos)

                    if self.editMenu != None:
                        self.editMenu.move(int(self.x() - (self.editMenu.width() - self.width()) / 2), self.y() + self.height() + 30)

                return True

            else:
                return False

        elif object == self.closeButton:
            if event.type() == QEvent.Enter:
                self.closeContent = self.closeContent.replace(f'stroke="rgb{self.iconNormalColor}"', f'stroke="rgb(255, 0, 0)"')
                self.closeRenderer.load(QByteArray(self.closeContent.encode()))
                self.closeButton.setPixmap(self.renderSVG(self.closeRenderer))

            elif event.type() == QEvent.Leave:
                self.closeContent = self.closeContent.replace(f'stroke="rgb(255, 0, 0)"', f'stroke="rgb{self.iconNormalColor}"')
                self.closeRenderer.load(QByteArray(self.closeContent.encode()))
                self.closeButton.setPixmap(self.renderSVG(self.closeRenderer))

            elif event.type() == QEvent.MouseButtonPress:
                if event.button() == Qt.LeftButton:
                    self.close()

        return False


    def renderSVG(self, icon):
        image = QImage(self.iconSize[0], self.iconSize[1], QImage.Format_ARGB32)
        image.fill(Qt.transparent)

        painter = QPainter(image)
        icon.render(painter)
        painter.end()

        pixmap = QPixmap.fromImage(image)
        return pixmap


    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        
        self.updateGrips()

        self.windowHeight, self.windowWidth = event.size().height(), event.size().width()

        self.backgroundLayer.resize(event.size())
        self.backgroundLayer.setScaledContents(True)

        self.topLayer.resize(event.size())
        self.topLayer.setScaledContents(True)

        self.borderLayer.resize(event.size())
        self.borderLayer.setScaledContents(True)

        self.clockFontSize = max(8, min(self.clockText.width() // 5, self.clockText.height() // 3))
        self.clockFont = QFont(self.fontFamily, self.clockFontSize)
        self.clockText.resize(event.size())
        self.clockText.setScaledContents(True)
        self.clockText.setFont(self.clockFont)

        self.blinkingColonText.resize(event.size())
        self.blinkingColonText.setScaledContents(True)
        self.blinkingColonText.setFont(self.clockFont)

        self.dateFontSize = max(8, min(self.dateText.width() // 20, self.dateText.height() // 3))
        self.dateFont = QFont(self.fontFamily, self.dateFontSize)
        self.dateText.resize(event.size())
        self.dateText.setScaledContents(True)
        self.dateText.setFont(self.dateFont)

        buttonWidth = event.size().width() / 10
        buttonHeight = event.size().height() / 10

        buttonSize = int((buttonWidth + buttonHeight) / 2)
        self.iconSize = [buttonSize, buttonSize]

        for button in self.buttons:
            button.setFixedSize(buttonSize, buttonSize)

        self.editButton.setPixmap(self.renderSVG(self.editRenderer))
        self.moveButton.setPixmap(self.renderSVG(self.moveRenderer))
        self.closeButton.setPixmap(self.renderSVG(self.closeRenderer))

        self.buttonLayout.setContentsMargins(10, int(event.size().height() / 1.5), 10, 10)


    def openEditMenu(self):
        if not self.editMenu:
            self.editMenu = EditMenu(self)
            self.editMenu.show()


    def closeEvent(self, event):
        if hasattr(self, 'editMenu'):
            if self.editMenu != None:
                self.editMenu.close()
                self.editMenu = None
                self.isOpenEditMenu = False

        self.configData["default"]["window"]["isOpenEditMenu"] = self.isOpenEditMenu
        with open("src/data/config.json", "w") as f:
            json.dump(self.configData, f, indent=4)


    def contextMenuEvent(self, e: QContextMenuEvent):
        contextMenu = ContextMenu(self)
        self.__connectMenuSignalToSlot(contextMenu)
        contextMenu.exec(self.cursor().pos())


    def __connectMenuSignalToSlot(self, menu: ContextMenu):
        menu.center.triggered.connect(lambda: self.alignWindow("Center"))
        menu.horizontallyCentered.triggered.connect(lambda: self.alignWindow("Horizontally Centered"))
        menu.verticallyCentered.triggered.connect(lambda: self.alignWindow("Vertically Centered"))
        menu.topLeft.triggered.connect(lambda: self.alignWindow("Top Left"))
        menu.topRight.triggered.connect(lambda: self.alignWindow("Top Right"))
        menu.bottomLeft.triggered.connect(lambda: self.alignWindow("Bottom Left"))
        menu.bottomRight.triggered.connect(lambda: self.alignWindow("Bottom Right"))

        menu.maximize.triggered.connect(self.maximizeWidget)
        menu.minimize.triggered.connect(self.showMinimized)
        menu.restore.triggered.connect(self.restoreWidget)
        menu.kill.triggered.connect(self.close)
        menu.edit.triggered.connect(self.openEditMenu)
        menu.default.triggered.connect(self.backToDefault)


    def beforeRestart(self):
        if self.editMenu:
            self.configData[self.user]["window"]["isOpenEditMenu"] = True

        self.configData[self.user]["background"]["type"] = self.backgroundType
        with open("src/data/config.json", "w") as f:
            json.dump(self.configData, f, indent=4)

        self.__restart()


    def __restart(self):
        QtCore.QCoreApplication.quit()
        QtCore.QProcess.startDetached(sys.executable, sys.argv)


    def backToDefault(self):
        self.user = "default"
        self.configData["config"] = self.user
        self.beforeRestart()


    def save(self):
        self.user = "custom"

        self.configData["config"] = self.user
        self.configData[self.user]["background"]["type"] = self.backgroundType
        self.configData[self.user]["window"]["advancedOptions"] = self.advancedOptions
        self.configData[self.user]["window"]["isOpenEditMenu"] = self.isOpenEditMenu
        self.configData[self.user]["window"]["showOnTaskbar"] = self.showOnTaskbar
        self.configData[self.user]["window"]["showToolTips"] = self.showToolTips
        self.configData[self.user]["window"]["staysOnTop"] = self.staysOnTop
        self.configData[self.user]["window"]["size"][self.backgroundType][0] = self.windowHeight
        self.configData[self.user]["window"]["size"][self.backgroundType][1] = self.windowWidth

        self.configData[self.user]["background"]["type"] = self.backgroundType
        self.configData[self.user]["background"]["gif"]["normal"] = self.backgroundNormalGif
        self.configData[self.user]["background"]["gif"]["blur"] = self.backgroundBlurGif
        self.configData[self.user]["background"]["gif"]["top"] = self.backgroundTopGif
        self.configData[self.user]["background"]["gif"]["path"] = self.backgroundGifPath
        self.configData[self.user]["background"]["image"]["normal"] = self.backgroundNormalImage
        self.configData[self.user]["background"]["image"]["blur"] = self.backgroundBlurImage
        self.configData[self.user]["background"]["image"]["top"] = self.backgroundTopImage
        self.configData[self.user]["background"]["image"]["path"] = self.backgroundImagePath
        self.configData[self.user]["background"]["opacity"] = self.backgroundOpacity
        self.configData[self.user]["background"]["color"] = self.backgroundColor
        self.configData[self.user]["background"]["borderSize"] = self.backgroundBorderSize
        self.configData[self.user]["background"]["borderColor"][self.backgroundType] = self.backgroundBorderColor
        self.configData[self.user]["background"]["borderRadius"] = self.backgroundBorderRadius
        self.configData[self.user]["background"]["borderOpacity"] = self.backgroundBorderOpacity
        self.configData[self.user]["background"]["animation"] = self.backgroundAnimation
        self.configData[self.user]["background"]["frameCount"] = self.backgroundAnimationFrameCount
        self.configData[self.user]["background"]["animationCounter"] = self.backgroundAnimationCounter
        self.configData[self.user]["background"]["animationDuration"] = self.backgroundAnimationDuration
        self.configData[self.user]["background"]["customGifCount"] = self.backgroundCustomGifCount

        self.configData[self.user]["text"]["blinkingColonVisibility"] = self.blinkingColonVisibility
        self.configData[self.user]["text"]["blinkingColonAnimation"] = self.blinkingColonAnimation
        self.configData[self.user]["text"]["clockFontSize"] = self.clockFontSize
        self.configData[self.user]["text"]["dateFontSize"] = self.dateFontSize
        self.configData[self.user]["text"]["color"][self.backgroundType] = self.textColor
        self.configData[self.user]["text"]["opacity"] = self.textOpacity
        self.configData[self.user]["text"]["xCoord"] = self.textXCoord
        self.configData[self.user]["text"]["yCoord"] = self.textYCoord
        self.configData[self.user]["text"]["fontPath"] = self.fontPath
        self.configData[self.user]["text"]["font"] = self.font
        self.configData[self.user]["text"]["iconPath"] = self.iconPath
        self.configData[self.user]["text"]["iconSize"] = self.iconSize
        self.configData[self.user]["text"]["iconColor"]["normal"][self.backgroundType] = self.iconNormalColor
        self.configData[self.user]["text"]["iconColor"]["hover"][self.backgroundType] = self.iconHoverColor

        with open("src/data/config.json", "w") as f:
            json.dump(self.configData, f, indent=4)

        self.editMenu.close()
        self.editMenu = None


    def maximizeWidget(self):
        self.showMaximized()
        fakeEvent = QResizeEvent(self.size(), QSize())
        self.resizeEvent(fakeEvent)


    def restoreWidget(self):
        self.showNormal()
        fakeEvent = QResizeEvent(self.size(), QSize())
        self.resizeEvent(fakeEvent)


    def alignWindow(self, align):
        if align == "Center":
            windowGeometry = self.frameGeometry()
            centerOfWindowGeometry = QApplication.desktop().availableGeometry().center()
            windowGeometry.moveCenter(centerOfWindowGeometry)
            self.move(windowGeometry.topLeft())

            if self.editMenu != None:
                self.editMenu.move(int(self.x() - (self.editMenu.width() - self.width()) / 2), self.y() + self.height() + 30)

        elif align == "Horizontally Centered":
            screenSize = QApplication.desktop().availableGeometry()
            x = int((screenSize.width() / 2) - (self.windowWidth / 2))
            y = self.y()
            self.move(x, y)

            if self.editMenu != None:
                self.editMenu.move(int(self.x() - (self.editMenu.width() - self.width()) / 2), self.y() + self.height() + 30)

        elif align == "Vertically Centered":
            screenSize = QApplication.desktop().availableGeometry()
            x = self.x()
            y = int((screenSize.height() / 2) - (self.windowHeight / 2))
            self.move(x, y)

            if self.editMenu != None:
                self.editMenu.move(int(self.x() - (self.editMenu.width() - self.width()) / 2), self.y() + self.height() + 30)

        elif align == "Top Left":
            self.move(40, 40)

            if self.editMenu != None:
                self.editMenu.move(int(self.x() - (self.editMenu.width() - self.width()) / 2), self.y() + self.height() + 30)

        elif align == "Top Right":
            screenSize = QApplication.desktop().availableGeometry()
            x = int(screenSize.width() - (self.windowWidth + 40))
            y = 40
            self.move(x, y)

            if self.editMenu != None:
                self.editMenu.move(int(self.x() - (self.editMenu.width() - self.width()) / 2), self.y() + self.height() + 30)

        elif align == "Bottom Left":
            screenSize = QApplication.desktop().availableGeometry()
            x = 40
            y = int(screenSize.height() - (self.windowHeight + 40))
            self.move(x, y)

            if self.editMenu != None:
                self.editMenu.move(int(self.x() - (self.editMenu.width() - self.width()) / 2), self.y() - self.editMenu.height() - 30)

        elif align == "Bottom Right":
            screenSize = QApplication.desktop().availableGeometry()
            x = int(screenSize.width() - (self.windowWidth + 40))
            y = int(screenSize.height() - (self.windowHeight + 40))
            self.move(x, y)

            if self.editMenu != None:
                self.editMenu.move(int(self.x() - (self.editMenu.width() - self.width()) / 2), self.y() - self.editMenu.height() - 30)


    def __loadConfigData(self):
        """ load configuration data from json """
        with open("src/data/config.json", "r") as data:
            return json.load(data)


    def __loadSvgContent(self):
        with open(f'{self.iconPath}edit.svg', 'r') as f:
            self.editContent = f.read()

        with open(f'{self.iconPath}move.svg', 'r') as f:
            self.moveContent = f.read()

        with open(f'{self.iconPath}close.svg', 'r') as f:
            self.closeContent = f.read()

        self.editRenderer = QSvgRenderer(f'{self.iconPath}edit.svg')
        self.moveRenderer = QSvgRenderer(f'{self.iconPath}move.svg')
        self.closeRenderer = QSvgRenderer(f'{self.iconPath}close.svg')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
