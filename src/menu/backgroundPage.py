from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

from lib import Slider, PushButton, ComboBox, ToolButton
from lib import FluentIcon as FIF



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
        self.HBoxLayout1.addWidget(self.backgroundTypeComboBox)
        self.filePickerMiniButton = ToolButton(FIF.FOLDER_ADD, self)
        self.filePickerMiniButton.setMaximumSize(32, 32)
        self.HBoxLayout1.addWidget(self.filePickerMiniButton)
        self.bgColorPickerMiniButton = PushButton(self)
        self.bgColorPickerMiniButton.setStyleSheet("PushButton {background: rgba%s; border-radius: 5px;}" % str(self.parent.backgroundColor))
        self.bgColorPickerMiniButton.setMaximumSize(32, 32)
        if self.parent.backgroundType == "Color":
            self.filePickerMiniButton.setVisible(False)
        else:
            self.bgColorPickerMiniButton.setVisible(False)
        self.HBoxLayout1.addWidget(self.bgColorPickerMiniButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout1)

        self.HBoxLayout2 = QHBoxLayout()
        self.borderColorPickerButton = PushButton('Set Border Color', self, FIF.PALETTE)
        self.HBoxLayout2.addWidget(self.borderColorPickerButton)
        self.borderColorPickerMiniButton = PushButton(self)
        self.borderColorPickerMiniButton.setStyleSheet("PushButton {background: rgba%s; border-radius: 5px;}" % str(self.parent.backgroundBorderColor))
        self.borderColorPickerMiniButton.setMaximumSize(32, 32)
        self.HBoxLayout2.addWidget(self.borderColorPickerMiniButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout2)

        self.HBoxLayout3 = QHBoxLayout()
        self.borderOpacityLabel = QLabel(f"Border Opacity: {self.parent.backgroundBorderOpacity}", self)
        self.borderOpacityLabel.setVisible(self.parent.advancedOptions)
        self.borderOpacityLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.HBoxLayout3.addWidget(self.borderOpacityLabel)
        self.borderOpacitySlider = Slider(Qt.Horizontal, self)
        self.borderOpacitySlider.setVisible(self.parent.advancedOptions)
        self.borderOpacitySlider.setMinimum(0)
        self.borderOpacitySlider.setMaximum(100)
        self.borderOpacitySlider.setTickInterval(1)
        self.borderOpacitySlider.setSingleStep(1)
        self.borderOpacitySlider.setValue(int(self.parent.backgroundBorderOpacity))
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
            self.HBoxLayout7.addWidget(self.durationSlider)
            self.mainVBoxLayout.addLayout(self.HBoxLayout7)
