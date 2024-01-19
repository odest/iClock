from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QColorDialog
from PyQt5.QtGui import QFont, QFontDatabase, QColor
from PyQt5.QtCore import Qt

from lib import Slider, PushButton, ComboBox, ToolButton
from lib import FluentIcon as FIF

import os


class TextPage(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.fontDict = {}
        self.mainVBoxLayout = QVBoxLayout(self)

        self.initWidgets()


    def initWidgets(self):
        self.HBoxLayout1 = QHBoxLayout()
        self.sizeLabel = QLabel(f"Size: {self.parent.clockFontSize}", self)
        self.sizeLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.HBoxLayout1.addWidget(self.sizeLabel)
        self.sizeSlider = Slider(Qt.Horizontal, self)
        self.sizeSlider.setMinimum(1)
        self.sizeSlider.setMaximum(int(self.parent.windowHeight / 1.5))
        self.sizeSlider.setTickInterval(1)
        self.sizeSlider.setSingleStep(1)
        self.sizeSlider.setValue(int(self.parent.clockFontSize))
        self.sizeSlider.valueChanged.connect(lambda value: self.sliderEvent("Size", self.sizeSlider, self.sizeLabel))
        self.HBoxLayout1.addWidget(self.sizeSlider)
        self.mainVBoxLayout.addLayout(self.HBoxLayout1)

        self.HBoxLayout2 = QHBoxLayout()
        self.xCoordLabel = QLabel(f"X Coord: {self.parent.textXCoord}", self)
        self.xCoordLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.HBoxLayout2.addWidget(self.xCoordLabel)
        self.xCoordSlider = Slider(Qt.Horizontal, self)
        self.xCoordSlider.setMinimum(int(-self.parent.width() / 2))
        self.xCoordSlider.setMaximum(int(self.parent.width() / 2))
        self.xCoordSlider.setTickInterval(1)
        self.xCoordSlider.setSingleStep(1)
        self.xCoordSlider.setValue(int(self.parent.textXCoord))
        self.xCoordSlider.valueChanged.connect(lambda value: self.sliderEvent("X Coord", self.xCoordSlider, self.xCoordLabel))
        self.HBoxLayout2.addWidget(self.xCoordSlider)
        self.mainVBoxLayout.addLayout(self.HBoxLayout2)

        self.HBoxLayout3 = QHBoxLayout()
        self.yCoordLabel = QLabel(f"Y Coord: {self.parent.textYCoord}", self)
        self.yCoordLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.HBoxLayout3.addWidget(self.yCoordLabel)
        self.yCoordSlider = Slider(Qt.Horizontal, self)
        self.yCoordSlider.setMinimum(int(-self.parent.height() / 2))
        self.yCoordSlider.setMaximum(int(self.parent.height() / 2))
        self.yCoordSlider.setTickInterval(1)
        self.yCoordSlider.setSingleStep(1)
        self.yCoordSlider.setValue(int(self.parent.textYCoord))
        self.yCoordSlider.valueChanged.connect(lambda value: self.sliderEvent("Y Coord", self.yCoordSlider, self.yCoordLabel))
        self.HBoxLayout3.addWidget(self.yCoordSlider)
        self.mainVBoxLayout.addLayout(self.HBoxLayout3)

        self.HBoxLayout4 = QHBoxLayout()
        self.opacityLabel = QLabel(f"Opacity: %{self.parent.textOpacity}", self)
        self.opacityLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.HBoxLayout4.addWidget(self.opacityLabel)
        self.opacitySlider = Slider(Qt.Horizontal, self)
        self.opacitySlider.setMinimum(0)
        self.opacitySlider.setMaximum(100)
        self.opacitySlider.setTickInterval(1)
        self.opacitySlider.setSingleStep(1)
        self.opacitySlider.setValue(int(self.parent.textOpacity))
        self.opacitySlider.valueChanged.connect(lambda value: self.sliderEvent("Opacity", self.opacitySlider, self.opacityLabel))
        self.HBoxLayout4.addWidget(self.opacitySlider)
        self.mainVBoxLayout.addLayout(self.HBoxLayout4)

        self.HBoxLayout5 = QHBoxLayout()
        self.colorPickerButton = PushButton('Set Text Color', self, FIF.PALETTE)
        self.colorPickerButton.clicked.connect(lambda: self.showColorDialog("text", self.parent.textColor))
        self.HBoxLayout5.addWidget(self.colorPickerButton)
        self.colorPickerMiniButton = PushButton(self)
        self.colorPickerMiniButton.clicked.connect(lambda: self.showColorDialog("text", self.parent.textColor))
        self.colorPickerMiniButton.setStyleSheet("PushButton {background: rgba%s; border-radius: 5px;}" % str(self.parent.textColor))
        self.colorPickerMiniButton.setMaximumSize(32, 32)
        self.HBoxLayout5.addWidget(self.colorPickerMiniButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout5)

        self.HBoxLayout6 = QHBoxLayout()
        self.iconsNormalColorPickerButton = PushButton('Set Icons Normal Color', self, FIF.PALETTE)
        self.HBoxLayout6.addWidget(self.iconsNormalColorPickerButton)
        self.iconsNormalColorPickerMiniButton = PushButton(self)
        self.iconsNormalColorPickerMiniButton.setStyleSheet("PushButton {background: rgb%s; border-radius: 5px;}" % str(self.parent.iconNormalColor))
        self.iconsNormalColorPickerMiniButton.setMaximumSize(32, 32)
        self.HBoxLayout6.addWidget(self.iconsNormalColorPickerMiniButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout6)

        self.HBoxLayout7 = QHBoxLayout()
        self.iconsHoverColorPickerButton = PushButton('Set Icons Hover Color', self, FIF.PALETTE)
        self.HBoxLayout7.addWidget(self.iconsHoverColorPickerButton)
        self.iconsHoverColorPickerMiniButton = PushButton(self)
        self.iconsHoverColorPickerMiniButton.setStyleSheet("PushButton {background: rgb%s; border-radius: 5px;}" % str(self.parent.iconHoverColor))
        self.iconsHoverColorPickerMiniButton.setMaximumSize(32, 32)
        self.HBoxLayout7.addWidget(self.iconsHoverColorPickerMiniButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout7)

        self.HBoxLayout8 = QHBoxLayout()
        self.fontComboBox = ComboBox(self)
        self.fontComboBox.setPlaceholderText("Selected Font:")
        self.folderPath = self.parent.fontPath
        fontNameList = [os.path.basename(file) for file in os.listdir(self.folderPath) if os.path.isfile(os.path.join(self.folderPath, file)) and file.lower().endswith((".ttf", ".otf"))]
        items = []
        fonts = []
        for i in fontNameList:
            fontID = QFontDatabase.addApplicationFont(f'{self.folderPath}{i}')
            fontFamily = QFontDatabase.applicationFontFamilies(fontID)[0]
            font = QFont(fontFamily, 15)
            self.fontDict[fontFamily] = i
            items.append(fontFamily)
            fonts.append(font)
        self.fontComboBox.addItems(items, fonts)
        self.fontComboBox.setCurrentIndex(items.index(str(self.parent.fontFamily)))
        self.HBoxLayout8.addWidget(self.fontComboBox)
        self.filePickerMiniButton = ToolButton(FIF.FOLDER_ADD, self)
        self.filePickerMiniButton.setMaximumSize(32, 32)
        self.HBoxLayout8.addWidget(self.filePickerMiniButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout8)


    def updateTextColor(self, color):
        r, g, b, a = color.getRgb()
        self.parent.textColor = (r, g, b, self.parent.textColor[3])
        self.parent.clockText.setStyleSheet(f'background-color: transparent; color: rgba{self.parent.textColor};')
        self.parent.blinkingColonText.setStyleSheet(f'background-color: transparent; color: rgba{self.parent.textColor};')
        self.parent.dateText.setStyleSheet(f'background-color: transparent; color: rgba{self.parent.textColor};')
        self.colorPickerMiniButton.setStyleSheet("PushButton {background: rgba%s; border-radius: 5px;}" % str(self.parent.textColor))


    def sliderEvent(self, whichWidget, slider, label):
        value = slider.value()
        if whichWidget == "Opacity":
            label.setText(f"{whichWidget}: %{value}")
        else:
            label.setText(f"{whichWidget}: {value}")

        if whichWidget == "Size":
            self.parent.clockFontSize = value
            self.parent.clockFont = QFont(self.parent.fontFamily, self.parent.clockFontSize)
            self.parent.clockText.setFont(self.parent.clockFont)
            self.parent.blinkingColonText.setFont(self.parent.clockFont)

        elif whichWidget == "X Coord":
            self.parent.textXCoord = value
            self.parent.clockText.move(self.parent.textXCoord, self.parent.textYCoord)
            self.parent.blinkingColonText.move(self.parent.textXCoord, self.parent.textYCoord)

        elif whichWidget == "Y Coord":
            self.parent.textYCoord = value
            self.parent.clockText.move(self.parent.textXCoord, self.parent.textYCoord)
            self.parent.blinkingColonText.move(self.parent.textXCoord, self.parent.textYCoord)

        elif whichWidget == "Opacity":
            self.parent.textOpacity = value
            self.parent.textColor = self.parent.textColor[:-1] + (int(value * 2.55),)
            color = f"rgba{str(self.parent.textColor[:-1] + (value * 0.01,))}"
            self.parent.clockText.setStyleSheet(f'background-color : transparent; color: {color};')
            self.colorPickerMiniButton.setStyleSheet("PushButton {background: %s; border-radius: 5px;}" % color)


    def showColorDialog(self, type, currentColor):
        color_dialog = QColorDialog(QColor(*currentColor), self)
        color_dialog.setStyleSheet("QColorDialog {background: QLinearGradient( x1: 0, y1: 0,x2: 1, y2: 0, stop: 0 rgb(7,43,71), stop: 1 rgb(12,76,125)); color: black;}")
        if type == "text":
            color_dialog.currentColorChanged.connect(self.updateTextColor)

        color_dialog.exec_()
