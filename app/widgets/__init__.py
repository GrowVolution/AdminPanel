from packaging import Package
from PySide6.QtWidgets import QWidget
from pathlib import Path

WIDGETS = Package(Path(__file__).parent)


class BaseWidget(QWidget):
    def __init__(self, ui_cls):
        super().__init__()
        self.ui = ui_cls()
        self.ui.setupUi(self)
