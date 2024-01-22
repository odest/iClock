from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QColorDialog, QFileDialog
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from lib import Slider, PushButton, ComboBox, ToolButton, InfoBar, InfoBarPosition
from lib import FluentIcon as FIF

from PIL import Image, ImageFilter

import shutil
import os



class BackgroundPage(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.mainVBoxLayout = QVBoxLayout(self)
        self.initWidgets()


    def initWidgets(self):
        self.HBoxLayout1 = QHBoxLayout()
        self.backgroundTypeComboBox = ComboBox(self)
        self.backgroundTypeComboBox.setPlaceholderText("Background")
        _typeList = ["Gif", "Image", "Color"]
        self.backgroundTypeComboBox.addItems(_typeList)
        self.backgroundTypeComboBox.setCurrentIndex(_typeList.index(str(self.parent.backgroundType)))
        self.backgroundTypeComboBox.currentTextChanged.connect(self.comboBoxSelect)
        self.HBoxLayout1.addWidget(self.backgroundTypeComboBox)
        self.filePickerMiniButton = ToolButton(FIF.FOLDER_ADD, self)
        self.filePickerMiniButton.clicked.connect(self.showFileDialog)
        self.filePickerMiniButton.setMaximumSize(32, 32)
        self.HBoxLayout1.addWidget(self.filePickerMiniButton)
        self.colorPickerMiniButton = PushButton(self)
        self.colorPickerMiniButton.clicked.connect(lambda: self.showColorDialog(self.updateBackgroundColor, self.parent.backgroundColor))
        self.colorPickerMiniButton.setStyleSheet("PushButton {background: rgba%s; border-radius: 5px;}" % str(self.parent.backgroundColor))
        self.colorPickerMiniButton.setMaximumSize(32, 32)
        if self.parent.backgroundType == "Color":
            self.filePickerMiniButton.setVisible(False)
        else:
            self.colorPickerMiniButton.setVisible(False)
        self.HBoxLayout1.addWidget(self.colorPickerMiniButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout1)

        self.HBoxLayout2 = QHBoxLayout()
        self.borderColorPickerButton = PushButton('Set Border Color', self, FIF.PALETTE)
        self.borderColorPickerButton.clicked.connect(lambda: self.showColorDialog(self.updateBorderColor, self.parent.backgroundBorderColor))
        self.HBoxLayout2.addWidget(self.borderColorPickerButton)
        self.borderColorPickerMiniButton = PushButton(self)
        self.borderColorPickerMiniButton.clicked.connect(lambda: self.showColorDialog(self.updateBorderColor, self.parent.backgroundBorderColor))
        self.borderColorPickerMiniButton.setStyleSheet("PushButton {background: rgba%s; border-radius: 5px;}" % str(self.parent.backgroundBorderColor))
        self.borderColorPickerMiniButton.setMaximumSize(32, 32)
        self.HBoxLayout2.addWidget(self.borderColorPickerMiniButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout2)

        self.HBoxLayout3 = QHBoxLayout()
        self.borderOpacityLabel = QLabel(f"Border Opacity: %{self.parent.backgroundBorderOpacity}", self)
        self.borderOpacityLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.HBoxLayout3.addWidget(self.borderOpacityLabel)
        self.borderOpacitySlider = Slider(Qt.Horizontal, self)
        self.borderOpacitySlider.setMinimum(0)
        self.borderOpacitySlider.setMaximum(100)
        self.borderOpacitySlider.setTickInterval(1)
        self.borderOpacitySlider.setSingleStep(1)
        self.borderOpacitySlider.setValue(int(self.parent.backgroundBorderOpacity))
        self.borderOpacitySlider.valueChanged.connect(lambda value: self.sliderEvent("Border Opacity", self.borderOpacitySlider, self.borderOpacityLabel))
        self.HBoxLayout3.addWidget(self.borderOpacitySlider)
        self.mainVBoxLayout.addLayout(self.HBoxLayout3)

        self.HBoxLayout4 = QHBoxLayout()
        self.borderSizeLabel = QLabel(f"Border Size: {self.parent.backgroundBorderSize}", self)
        self.borderSizeLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.HBoxLayout4.addWidget(self.borderSizeLabel)
        self.borderSizeSlider = Slider(Qt.Horizontal, self)
        self.borderSizeSlider.setMinimum(0)
        self.borderSizeSlider.setMaximum(10)
        self.borderSizeSlider.setTickInterval(1)
        self.borderSizeSlider.setSingleStep(1)
        self.borderSizeSlider.setValue(int(self.parent.backgroundBorderSize))
        self.borderSizeSlider.valueChanged.connect(lambda value: self.sliderEvent("Border Size", self.borderSizeSlider, self.borderSizeLabel))
        self.HBoxLayout4.addWidget(self.borderSizeSlider)
        self.mainVBoxLayout.addLayout(self.HBoxLayout4)

        self.HBoxLayout5 = QHBoxLayout()
        self.borderRadiusLabel = QLabel(f"Border Radius: {self.parent.backgroundBorderRadius}", self)
        self.borderRadiusLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.HBoxLayout5.addWidget(self.borderRadiusLabel)
        self.borderRadiusSlider = Slider(Qt.Horizontal, self)
        self.borderRadiusSlider.setMinimum(0)
        self.borderRadiusSlider.setMaximum(int(self.parent.windowHeight / 2))
        self.borderRadiusSlider.setTickInterval(1)
        self.borderRadiusSlider.setSingleStep(1)
        self.borderRadiusSlider.setValue(int(self.parent.backgroundBorderRadius))
        self.borderRadiusSlider.valueChanged.connect(lambda value: self.sliderEvent("Border Radius", self.borderRadiusSlider, self.borderRadiusLabel))
        self.HBoxLayout5.addWidget(self.borderRadiusSlider)
        self.mainVBoxLayout.addLayout(self.HBoxLayout5)

        self.HBoxLayout6 = QHBoxLayout()
        self.opacityLabel = QLabel(f"Opacity: %{self.parent.backgroundOpacity}", self)
        self.opacityLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.HBoxLayout6.addWidget(self.opacityLabel)
        self.opacitySlider = Slider(Qt.Horizontal, self)
        self.opacitySlider.setMinimum(0)
        self.opacitySlider.setMaximum(100)
        self.opacitySlider.setTickInterval(1)
        self.opacitySlider.setSingleStep(1)
        self.opacitySlider.setValue(int(self.parent.backgroundOpacity))
        self.opacitySlider.valueChanged.connect(lambda value: self.sliderEvent("Opacity", self.opacitySlider, self.opacityLabel))
        self.HBoxLayout6.addWidget(self.opacitySlider)
        self.mainVBoxLayout.addLayout(self.HBoxLayout6)

        if self.parent.backgroundType == "Gif":
            self.HBoxLayout7 = QHBoxLayout()
            self.durationLabel = QLabel(f"Duration: {self.parent.backgroundAnimationDuration}", self)
            self.durationLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
            self.HBoxLayout7.addWidget(self.durationLabel)
            self.durationSlider = Slider(Qt.Horizontal, self)
            self.durationSlider.setMinimum(0)
            self.durationSlider.setMaximum(100)
            self.durationSlider.setTickInterval(1)
            self.durationSlider.setSingleStep(1)
            self.durationSlider.setValue(int(self.parent.backgroundAnimationDuration))
            self.durationSlider.valueChanged.connect(lambda value: self.sliderEvent("Duration", self.durationSlider, self.durationLabel))
            self.HBoxLayout7.addWidget(self.durationSlider)
            self.mainVBoxLayout.addLayout(self.HBoxLayout7)


    def updateToolTips(self):
        self.parent.setToolTip(self.backgroundTypeComboBox, 'Choose background type')
        if self.parent.backgroundType == "Image":
            self.parent.setToolTip(self.filePickerMiniButton, 'Set background image')
        elif self.parent.backgroundType == "Gif":
            self.parent.setToolTip(self.filePickerMiniButton, 'Set background gif')
            self.parent.setToolTip(self.durationSlider, 'Set background animation duration')
        self.parent.setToolTip(self.colorPickerMiniButton, 'Set background color')

        self.parent.setToolTip(self.borderColorPickerMiniButton, 'Set border color')
        self.parent.setToolTip(self.borderOpacitySlider, 'Set border opacity')
        self.parent.setToolTip(self.borderSizeSlider, 'Set border size')
        self.parent.setToolTip(self.borderRadiusSlider, 'Set border radius')
        self.parent.setToolTip(self.opacitySlider, 'Set background opacity')


    def updateBackgroundColor(self, color):
        r, g, b, _ = color.getRgb()
        self.parent.backgroundColor = (r, g, b, self.parent.backgroundColor[3])
        self.parent.backgroundLayer.setStyleSheet(f"background-color: rgba{self.parent.backgroundColor}; border-radius:{self.parent.backgroundBorderRadius}px;")
        self.colorPickerMiniButton.setStyleSheet("PushButton {background: rgba%s; border-radius: 5px;}" % str(self.parent.backgroundColor))


    def updateBorderColor(self, color):
        r, g, b, _ = color.getRgb()
        self.parent.backgroundBorderColor = (r, g, b, self.parent.backgroundBorderColor[3])
        self.parent.borderLayer.setStyleSheet(f'background-color: transparent; border: {self.parent.backgroundBorderSize}px solid rgba{self.parent.backgroundBorderColor}; border-radius: {self.parent.backgroundBorderRadius}')
        self.borderColorPickerMiniButton.setStyleSheet("PushButton {background: rgba%s; border-radius: 5px;}" % str(self.parent.backgroundBorderColor))


    def updateBorderOpacity(self):
        self.parent.borderLayer.setStyleSheet(f'background-color: transparent; border: {self.parent.backgroundBorderSize}px solid rgba{self.parent.backgroundBorderColor}; border-radius: {self.parent.backgroundBorderRadius}')


    def comboBoxSelect(self, text):
        self.parent.backgroundType = text
        self.parent.beforeRestart()


    def showColorDialog(self, callback, currentColor):
        color_dialog = QColorDialog(QColor(*currentColor), self)
        color_dialog.setStyleSheet("QColorDialog {background: QLinearGradient( x1: 0, y1: 0,x2: 1, y2: 0, stop: 0 rgb(7,43,71), stop: 1 rgb(12,76,125)); color: black;}")
        color_dialog.currentColorChanged.connect(callback)
        color_dialog.exec_()


    def showFileDialog(self):
        if self.parent.backgroundType == "Gif":
            pass
        elif self.parent.backgroundType == "Image":
            imagePath, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.webp)")

            if imagePath:
                try:
                    targetFolder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "assets", "images", "custom")
                    copiedImagePath = self.__copySelectedFile(imagePath, targetFolder)

                    if copiedImagePath:
                        self.parent.backgroundImagePath = "src/assets/images/custom/"
                        self.parent.backgroundTopImage = None
                        self.parent.backgroundNormalImage = os.path.basename(imagePath)
                        self.parent.backgroundLayer.setStyleSheet(f"border-image: url('{self.parent.backgroundImagePath}{self.parent.backgroundNormalImage}'); border-radius:{self.parent.backgroundBorderRadius}px;")
                        self.parent.topLayer.setStyleSheet(f"background-color: transparent; border-image: url('{self.parent.backgroundImagePath}{self.parent.backgroundTopImage}'); border-radius:{self.parent.backgroundBorderRadius}px;")
                        self.parent.backgroundBlurImage = f"blur{self.parent.backgroundNormalImage}"

                        image = Image.open(imagePath)

                        if image.format == "PNG":
                            convertedImage = image.convert('RGB')
                            bluredImage = convertedImage.filter(ImageFilter.GaussianBlur(10))
                            bluredImage.save(f"{self.parent.backgroundImagePath}{self.parent.backgroundBlurImage}")
                        else:
                            bluredImage = image.filter(ImageFilter.GaussianBlur(10))
                            bluredImage.save(f"{self.parent.backgroundImagePath}{self.parent.backgroundBlurImage}")

                    else:
                        self.parent.backgroundImagePath = "src/assets/images/custom/"
                        self.parent.backgroundTopImage = None
                        self.parent.backgroundNormalImage = os.path.basename(imagePath)
                        self.parent.backgroundLayer.setStyleSheet(f"border-image: url('{self.parent.backgroundImagePath}{self.parent.backgroundNormalImage}'); border-radius:{self.parent.backgroundBorderRadius}px;")
                        self.parent.topLayer.setStyleSheet(f"background-color: transparent; border-image: url('{self.parent.backgroundImagePath}{self.parent.backgroundTopImage}'); border-radius:{self.parent.backgroundBorderRadius}px;")
                        self.parent.backgroundBlurImage = f"blur{self.parent.backgroundNormalImage}"

                    self.__showInfoBar("success", "SUCCESS", "Selected image applied successfully.")

                except Exception as e:
                        self.__showInfoBar("error", "ERROR", "Please select a valid image file!")


    def sliderEvent(self, whichWidget, slider, label):
        value = slider.value()

        if whichWidget == "Opacity" or whichWidget == "Border Opacity":
            label.setText(f"{whichWidget}: %{value}")
        else:
            label.setText(f"{whichWidget}: {value}")

        if whichWidget == "Border Size":
            self.parent.backgroundBorderSize = value
            self.parent.borderLayer.setStyleSheet(f'background-color: transparent; border: {self.parent.backgroundBorderSize}px solid rgba{self.parent.backgroundBorderColor}; border-radius: {self.parent.backgroundBorderRadius}')

        elif whichWidget == "Border Opacity":
            if value == 0:
                value = 0.1
            self.parent.backgroundBorderOpacity = value
            self.parent.backgroundBorderColor = self.parent.backgroundBorderColor[:-1] + (int(value * 2.55),)
            self.updateBorderOpacity()

        elif whichWidget == "Border Radius":
            self.parent.backgroundBorderRadius = value
            self.parent.updateWidgets()

        elif whichWidget == "Opacity":
            if value == 0:
                value = 0.1
            self.parent.backgroundOpacity = value
            self.parent.updateBackgroundOpacity(self.parent.backgroundOpacity)

        elif whichWidget == "Duration":
            self.parent.backgroundAnimationDuration = value
            if value == 0:
                self.parent.animationTimer.stop()
                self.parent.backgroundAnimationDuration = 0
                self.parent.backgroundAnimation = False
            else:
                self.parent.animationTimer.start(self.parent.backgroundAnimationDuration)
                self.parent.backgroundAnimation = True


    def __showInfoBar(self, type, title, content):
        if type == "success":
            InfoBar.success(
                title=title,
                content=content,
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM,
                duration=3000,
                parent=self
            )
        elif type == "warning":
            InfoBar.warning(
                title=title,
                content=content,
                orient=Qt.Horizontal,
                isClosable=False,
                position=InfoBarPosition.BOTTOM,
                duration=3000,
                parent=self
            )
        elif type == "error":
            InfoBar.error(
                title=title,
                content=content,
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.BOTTOM_RIGHT,
                duration=3000,
                parent=self
            )


    def __copySelectedFile(self, filePath, targetFolder):
        fileName = os.path.basename(filePath)
        targetPath = os.path.join(targetFolder, fileName)

        if os.path.exists(targetPath):
            return None
        else:
            shutil.copy(filePath, targetPath)
            return targetPath
