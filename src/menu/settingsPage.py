from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout

from lib import SwitchButton, PushButton
from lib import FluentIcon as FIF

from src import ListCard



class SettingsPage(QWidget):
    def __init__(self, parent, menu):
        super().__init__()

        self.parent = parent
        self.menu = menu
        self.mainVBoxLayout = QVBoxLayout(self)
        self.mainVBoxLayout.setSpacing(10)
        self.initWidgets()


    def initWidgets(self):
        self.showToolTipsCard = ListCard("Show ToolTips", self)
        self.showToolTipsCard.switch.setChecked(self.parent.showToolTips)
        self.showToolTipsCard.switch.setText("")
        self.showToolTipsCard.switch.checkedChanged.connect(lambda i: self.switchEvent(i, "Show ToolTips", self.showToolTipsCard.switch))
        self.mainVBoxLayout.addWidget(self.showToolTipsCard)

        self.taskbarCard = ListCard("Show on Taskbar", self)
        self.taskbarCard.switch.setChecked(self.parent.showOnTaskbar)
        self.taskbarCard.switch.setText("")
        self.taskbarCard.switch.checkedChanged.connect(lambda i: self.switchEvent(i, "Show on Taskbar", self.taskbarCard.switch))
        self.mainVBoxLayout.addWidget(self.taskbarCard)

        self.staysOnTopCard = ListCard("Stays on Top", self)
        self.staysOnTopCard.switch.setChecked(self.parent.staysOnTop)
        self.staysOnTopCard.switch.setText("")
        self.staysOnTopCard.switch.checkedChanged.connect(lambda i: self.switchEvent(i, "Stays on Top", self.staysOnTopCard.switch))
        self.mainVBoxLayout.addWidget(self.staysOnTopCard)

        self.blinkingColonCard = ListCard("Blinking Colon", self)
        self.blinkingColonCard.switch.setChecked(self.parent.blinkingColonAnimation)
        self.blinkingColonCard.switch.setText("")
        self.blinkingColonCard.switch.checkedChanged.connect(lambda i: self.switchEvent(i, "Blinking Colon", self.blinkingColonCard.switch))
        self.mainVBoxLayout.addWidget(self.blinkingColonCard)

        self.advancedOptionsCard = ListCard("Advanced Options", self)
        self.advancedOptionsCard.switch.setChecked(self.parent.advancedOptions)
        self.advancedOptionsCard.switch.setText("")
        self.advancedOptionsCard.switch.checkedChanged.connect(lambda i: self.switchEvent(i, "Advanced Options", self.advancedOptionsCard.switch))
        self.mainVBoxLayout.addWidget(self.advancedOptionsCard)

        self.HBoxLayout6 = QHBoxLayout()
        self.backToDefaultButton = PushButton('Back to Default', self, FIF.LEFT_ARROW)
        self.backToDefaultButton.setFixedHeight(48)
        self.backToDefaultButton.clicked.connect(self.parent.backToDefault)
        self.HBoxLayout6.addWidget(self.backToDefaultButton)
        self.mainVBoxLayout.addLayout(self.HBoxLayout6)


    def updateToolTips(self):
        self.parent.setToolTip(self.showToolTipsCard.title, 'Set tooltips visibility')
        self.parent.setToolTip(self.showToolTipsCard.switch, 'Set tooltips visibility')
        self.parent.setToolTip(self.taskbarCard.title, 'Set whether the widget logo appears on the taskbar')
        self.parent.setToolTip(self.taskbarCard.switch, 'Set whether the widget logo appears on the taskbar')
        self.parent.setToolTip(self.staysOnTopCard.title, 'Set whether the widget stays on top of other apps')
        self.parent.setToolTip(self.staysOnTopCard.switch, 'Set whether the widget stays on top of other apps')
        self.parent.setToolTip(self.blinkingColonCard.title, 'Set whether the colon between hour and minute is visible')
        self.parent.setToolTip(self.blinkingColonCard.switch, 'Set whether the colon between hour and minute is visible')
        self.parent.setToolTip(self.advancedOptionsCard.title, 'Set whether to open advanced configuration settings')
        self.parent.setToolTip(self.advancedOptionsCard.switch, 'Set whether to open advanced configuration settings')
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
            elif value == "Blinking Colon":
                self.parent.blinkingColonAnimation = True
            elif value == "Advanced Options":
                self.parent.advancedOptions = True
                self.menu.updateAdvancedOptions()

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
            elif value == "Blinking Colon":
                self.parent.blinkingColonAnimation = False
            elif value == "Advanced Options":
                self.parent.advancedOptions = False
                self.menu.updateAdvancedOptions()

        switch.setText("")
