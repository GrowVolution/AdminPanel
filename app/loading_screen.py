from debugger import log

from PySide6.QtWidgets import (QWidget, QDialog, QGridLayout, QLabel,
                               QProgressBar, QSizePolicy, QVBoxLayout)
from PySide6.QtGui import QPainter, QColor, QBrush, QFont
from PySide6.QtCore import QTimer, QPointF, QCoreApplication, QMetaObject, QSize, Qt
import math


class LoadingUi(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(527, 319)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loading_animation = QWidget(Dialog)
        self.loading_animation.setObjectName(u"loading_animation")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.loading_animation.sizePolicy().hasHeightForWidth())
        self.loading_animation.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout()
        self.loading_animation.setLayout(self.gridLayout)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, -1)

        self.verticalLayout.addWidget(self.loading_animation)

        self.progress = QProgressBar(Dialog)
        self.progress.setObjectName(u"progress")
        self.progress.setEnabled(True)
        self.progress.setSizeIncrement(QSize(0, 0))
        self.progress.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        self.progress.setFont(font)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        self.progress.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progress)

        self.step = QLabel(Dialog)
        self.step.setObjectName(u"step")
        self.step.setFont(font)
        self.step.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.step)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.step.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))


class LoadingTrail(QWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.t = 0
        self.trail = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(16)

    def update_frame(self):
        self.t += 0.04
        if self.t > 2 * math.pi:
            self.t = 0

        pos = self.infinity_curve(self.t)
        self.trail.insert(0, pos)
        if len(self.trail) > 80:
            self.trail.pop()

        self.update()

    def infinity_curve(self, t):
        a = 100
        x = (a * math.cos(t)) / (1 + math.sin(t)**2)
        y = (a * math.sin(t) * math.cos(t)) / (1 + math.sin(t)**2)
        return QPointF(x + self.width() / 2, y + self.height() / 2)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        n = len(self.trail)
        for i, point in enumerate(self.trail):
            progress = i / n
            radius = 6 * (1 - progress)
            alpha = int(255 * (1 - progress))
            color = QColor(143, 188, 143, alpha)
            painter.setBrush(QBrush(color))
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(point, radius, radius)

_ui = LoadingUi()


def show_loading_screen():
    log('info', "Setting up loading screen...", True)
    loading_dialog = QDialog()
    _ui.setupUi(loading_dialog)

    loading_dialog.setWindowTitle("GrowVolution 2025 - GNU General Public License")
    from . import get_favicon
    loading_dialog.setWindowIcon(get_favicon())
    _ui.gridLayout.addWidget(LoadingTrail())

    log('info', "Loading...")
    loading_message("Panel wird geladen...")
    loading_dialog.show()
    return loading_dialog


def loading_message(msg: str):
    _ui.step.setText(msg)


def update_progress(value: int):
    _ui.progress.setValue(value)
