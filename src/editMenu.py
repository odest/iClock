from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon

from lib import SegmentedWidget, setTheme, Theme, PushButton, PrimaryPushButton
from lib import AcrylicWindow
from src import CustomTitleBar, BackgroundPage, TextPage, SettingsPage


class EditMenu(AcrylicWindow):
    """ EditMenu window """
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.initVar()
        self.initWindow()
        self.initMainPage()


    def initVar(self):
        """ initialize variables """
        self.windowWidth = 400
        self.windowHeight = 485


    def initWindow(self):
        """ initialize window """
        setTheme(Theme.DARK)
        _averageTitlebarHeight = 30
        if (self.parent.y() + self.parent.height() + _averageTitlebarHeight + self.windowHeight) > QApplication.desktop().availableGeometry().height():
            windowYCoord = self.parent.y() - _averageTitlebarHeight - self.windowHeight
        else:
            windowYCoord = self.parent.y() + self.parent.height() + _averageTitlebarHeight
        self.setGeometry(int(self.parent.x() - (self.windowWidth - self.parent.width()) / 2), windowYCoord, self.windowWidth, self.windowHeight)

        self.setTitleBar(CustomTitleBar(self))
        self.windowEffect.setAeroEffect(self.winId())
        self.setWindowIcon(QIcon(f"{self.parent.iconPath}edit.svg"))
        self.setWindowTitle("Edit iClock")
        self.setStyleSheet("background: rgb(0, 0, 127)")
        self.titleBar.raise_()


    def initMainPage(self):
        self.pivot = SegmentedWidget(self)
        self.stackedWidget = QStackedWidget(self)
        self.mainVBoxLayout = QVBoxLayout(self)

        self.backgroundPage = BackgroundPage(self.parent)
        self.textPage = TextPage(self.parent)
        self.settingsPage = SettingsPage(self.parent, self)

        self.addSubInterface(self.backgroundPage, 'backgroundPage', 'Background')
        self.addSubInterface(self.textPage, 'textPage', 'Text')
        self.addSubInterface(self.settingsPage, 'settingsPage', 'Settings')

        self.mainButtonWidget = QWidget(self)
        self.mainButtonHBoxLayout = QHBoxLayout(self.mainButtonWidget)
        self.cancelbutton = PushButton('CANCEL')
        self.cancelbutton.clicked.connect(self.closeEvent)
        self.saveButton = PrimaryPushButton('SAVE', self)
        self.mainButtonHBoxLayout.addWidget(self.cancelbutton)
        self.mainButtonHBoxLayout.addWidget(self.saveButton)
        self.mainButtonWidget.setLayout(self.mainButtonHBoxLayout)

        self.mainVBoxLayout.addWidget(self.pivot)
        self.mainVBoxLayout.addWidget(self.stackedWidget)
        self.mainVBoxLayout.addWidget(self.mainButtonWidget)
        self.mainVBoxLayout.setContentsMargins(10, 50, 10, 10)
        self.mainVBoxLayout.setSpacing(10)

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)
        self.stackedWidget.setCurrentWidget(self.backgroundPage)
        self.pivot.setCurrentItem(self.backgroundPage.objectName())


    def addSubInterface(self, widget, objectName, text):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget),
        )


    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())


    def closeEvent(self, event):
        self.parent.editMenu = None
        self.parent.isOpenEditMenu = False
        self.close()
