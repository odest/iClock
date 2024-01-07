# coding:utf-8
import typing
from PyQt5.QtCore import QEasingCurve, Qt
from PyQt5.QtGui import QWheelEvent
from PyQt5.QtWidgets import QScrollArea, QWidget

from ...common.smooth_scroll import SmoothScroll, SmoothMode
from .scroll_bar import ScrollBar, SmoothScrollBar, SmoothScrollDelegate


class ScrollArea(QScrollArea):
    """ Smooth scroll area """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.scrollDelagate = SmoothScrollDelegate(self)


class SingleDirectionScrollArea(QScrollArea):
    """ Single direction scroll area"""

    def __init__(self, parent=None, orient=Qt.Vertical):
        """
        Parameters
        ----------
        parent: QWidget
            parent widget

        orient: Orientation
            scroll orientation
        """
        super().__init__(parent)
        self.orient = orient
        self.smoothScroll = SmoothScroll(self, orient)
        self.vScrollBar = SmoothScrollBar(Qt.Vertical, self)
        self.hScrollBar = SmoothScrollBar(Qt.Horizontal, self)

    def setVerticalScrollBarPolicy(self, policy):
        super().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.vScrollBar.setForceHidden(policy == Qt.ScrollBarAlwaysOff)

    def setHorizontalScrollBarPolicy(self, policy):
        super().setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.hScrollBar.setForceHidden(policy == Qt.ScrollBarAlwaysOff)

    def setSmoothMode(self, mode):
        """ set smooth mode

        Parameters
        ----------
        mode: SmoothMode
            smooth scroll mode
        """
        self.smoothScroll.setSmoothMode(mode)

    def keyPressEvent(self, e):
        if e.key() in [Qt.Key_Left, Qt.Key_Right]:
            return

        return super().keyPressEvent(e)

    def wheelEvent(self, e: QWheelEvent):
        if e.angleDelta().x() != 0:
            return

        self.smoothScroll.wheelEvent(e)
        e.setAccepted(True)


class SmoothScrollArea(QScrollArea):
    """ Smooth scroll area """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delegate = SmoothScrollDelegate(self, True)

    def setScrollAnimation(self, orient, duration, easing=QEasingCurve.OutCubic):
        """ set scroll animation

        Parameters
        ----------
        orient: Orient
            scroll orientation

        duration: int
            scroll duration

        easing: QEasingCurve
            animation type
        """
        bar = self.delegate.hScrollBar if orient == Qt.Horizontal else self.delegate.vScrollBar
        bar.setScrollAnimation(duration, easing)

