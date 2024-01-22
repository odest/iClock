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
        self.showToolTipsSwitch.checkedChanged.connect(lambda i: self.switchEvent(i, "Show ToolTips", self.showToolTipsSwitch))
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
        self.tastbarSwitch.checkedChanged.connect(lambda i: self.switchEvent(i, "Show on Taskbar", self.tastbarSwitch))
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
        self.staysOnTopSwitch.checkedChanged.connect(lambda i: self.switchEvent(i, "Stays on Top", self.staysOnTopSwitch))
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
        self.backToDefaultButton.clicked.connect(self.parent.backToDefault)
        self.HBoxLayout6.addWidget(self.backToDefaultButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout6)


    def updateToolTips(self):
        self.parent.setToolTip(self.showToolTipsLabel, 'Set tooltips visibility')
        self.parent.setToolTip(self.showToolTipsSwitch, 'Set tooltips visibility')
        self.parent.setToolTip(self.taskbarLabel, 'Set whether the widget logo appears on the taskbar')
        self.parent.setToolTip(self.tastbarSwitch, 'Set whether the widget logo appears on the taskbar')
        self.parent.setToolTip(self.staysOnTopLabel, 'Set whether the widget stays on top of other apps')
        self.parent.setToolTip(self.staysOnTopSwitch, 'Set whether the widget stays on top of other apps')
        self.parent.setToolTip(self.blinkingColonLabel, 'Set whether the colon between hour and minute is visible')
        self.parent.setToolTip(self.blinkingColonSwitch, 'Set whether the colon between hour and minute is visible')
        self.parent.setToolTip(self.advancedOptionsLabel, 'Set whether to open advanced configuration settings')
        self.parent.setToolTip(self.advancedOptionsSwitch, 'Set whether to open advanced configuration settings')
        self.parent.setToolTip(self.backToDefaultButton, 'Back to default configuration settings')


    def switchEvent(self, isChecked: bool, value, switch):
        if isChecked:
            if value == "Show ToolTips":
                self.parent.showToolTips = True
                self.parent.updateToolTips()
                self.menu.updateToolTips()
            elif value == "Show on Taskbar":
                self.parent.showOnTaskbar = True
                self.parent.updateTaskbarEvent(self.parent)
                self.parent.updateTaskbarEvent(self.menu)
            elif value == "Stays on Top":
                self.parent.staysOnTop = True
                self.parent.updateStaysOnTopEvent(self.parent)
                self.parent.updateStaysOnTopEvent(self.menu)

        else:
            if value == "Show ToolTips":
                self.parent.showToolTips = False
                self.parent.updateToolTips()
                self.menu.updateToolTips()
            elif value == "Show on Taskbar":
                self.parent.showOnTaskbar = False
                self.parent.updateTaskbarEvent(self.parent)
                self.parent.updateTaskbarEvent(self.menu)
            elif value == "Stays on Top":
                self.parent.staysOnTop = False
                self.parent.updateStaysOnTopEvent(self.parent)
                self.parent.updateStaysOnTopEvent(self.menu)

        switch.setText("")
