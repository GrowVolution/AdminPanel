from . import DIALOGS
from qt_ui.info_dialog import Ui_Dialog

from PySide6.QtWidgets import QSizePolicy


@DIALOGS.register(
    'info_dialog',
    "Information",
    Ui_Dialog
)
def show(dialog, ui, info_html: str):
    ui.info.setHtml(info_html)

    document = ui.info.document()
    document.adjustSize()
    width = document.idealWidth() + 20
    height = document.size().height() + 20

    ui.info.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    ui.info.setFixedSize(width, height)

    dialog.adjustSize()
    dialog.setFixedSize(dialog.sizeHint())

    ui.ack_btn.clicked.connect(dialog.close)
    dialog.exec()
