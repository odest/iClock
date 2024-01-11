from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

from lib import SwitchButton, PushButton
from lib import FluentIcon as FIF


class SettingsPage(QWidget):
    def __init__(self, parent, menu):
        super().__init__()

        self.parent = parent
        self.menu = menu
        self.mainVBoxLayout = QVBoxLayout(self)
        self.initWidgets()


    def initWidgets(self):
        self.HBoxLayout1 = QHBoxLayout()
        self.HBoxLayout1.setObjectName("HBoxLayout1")
        self.showToolTipsLabel = QLabel("Show ToolTips", self)
        self.showToolTipsLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.showToolTipsLabel.setObjectName("showToolTipsLabel")
        self.HBoxLayout1.addWidget(self.showToolTipsLabel)
        self.showToolTipsSwitch = SwitchButton(self)
        if self.parent.showToolTips:
            self.showToolTipsSwitch.setChecked(True)
        else:
            self.showToolTipsSwitch.setChecked(False)
        self.showToolTipsSwitch.setText("")
        self.HBoxLayout1.addWidget(self.showToolTipsSwitch)
        self.mainVBoxLayout.addLayout(self.HBoxLayout1)

        self.HBoxLayout2 = QHBoxLayout()
        self.HBoxLayout2.setObjectName("HBoxLayout2")
        self.taskbarLabel = QLabel("Show on Taskbar", self)
        self.taskbarLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.taskbarLabel.setObjectName("taskbarLabel")
        self.HBoxLayout2.addWidget(self.taskbarLabel)
        self.tastbarSwitch = SwitchButton(self)
        if self.parent.showOnTaskbar:
            self.tastbarSwitch.setChecked(True)
        else:
            self.tastbarSwitch.setChecked(False)
        self.tastbarSwitch.setText("")
        self.HBoxLayout2.addWidget(self.tastbarSwitch)
        self.mainVBoxLayout.addLayout(self.HBoxLayout2)

        self.HBoxLayout3 = QHBoxLayout()
        self.HBoxLayout3.setObjectName("HBoxLayout3")
        self.staysOnTopLabel = QLabel("Stays on Top", self)
        self.staysOnTopLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.staysOnTopLabel.setObjectName("staysOnTopLabel")
        self.HBoxLayout3.addWidget(self.staysOnTopLabel)
        self.staysOnTopSwitch = SwitchButton(self)
        if self.parent.staysOnTop:
            self.staysOnTopSwitch.setChecked(True)
        else:
            self.staysOnTopSwitch.setChecked(False)
        self.staysOnTopSwitch.setText("")
        self.HBoxLayout3.addWidget(self.staysOnTopSwitch)
        self.mainVBoxLayout.addLayout(self.HBoxLayout3)

        self.HBoxLayout4 = QHBoxLayout()
        self.HBoxLayout4.setObjectName("HBoxLayout4")
        self.blinkingColonLabel = QLabel("Blinking Colon", self)
        self.blinkingColonLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.blinkingColonLabel.setObjectName("blinkingColonLabel")
        self.HBoxLayout4.addWidget(self.blinkingColonLabel)
        self.blinkingColonSwitch = SwitchButton(self)
        if self.parent.blinkingColonAnimation:
            self.blinkingColonSwitch.setChecked(True)
        else:
            self.blinkingColonSwitch.setChecked(False)
        self.blinkingColonSwitch.setText("")
        self.HBoxLayout4.addWidget(self.blinkingColonSwitch)
        self.mainVBoxLayout.addLayout(self.HBoxLayout4)

        self.HBoxLayout5 = QHBoxLayout()
        self.HBoxLayout5.setObjectName("HBoxLayout5")
        self.advancedOptionsLabel = QLabel("Advanced Options", self)
        self.advancedOptionsLabel.setStyleSheet("font: 20px 'Segoe UI'; background: transparent; color: white;")
        self.advancedOptionsLabel.setObjectName("advancedOptionsLabel")
        self.HBoxLayout5.addWidget(self.advancedOptionsLabel)
        self.advancedOptionsSwitch = SwitchButton(self)
        if self.parent.advancedOptions:
            self.advancedOptionsSwitch.setChecked(True)
        else:
            self.advancedOptionsSwitch.setChecked(False)
        self.advancedOptionsSwitch.setText("")
        self.HBoxLayout5.addWidget(self.advancedOptionsSwitch)
        self.mainVBoxLayout.addLayout(self.HBoxLayout5)

        self.HBoxLayout6 = QHBoxLayout()
        self.backToDefaultButton = PushButton('Back to Default', self, FIF.LEFT_ARROW)
        self.HBoxLayout6.addWidget(self.backToDefaultButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout6)
