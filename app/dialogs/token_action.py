from . import DIALOGS
from qt_ui.token_action_info import Ui_Dialog


@DIALOGS.register(
    'token_action',
    "Token Verwaltung",
    Ui_Dialog
)
def show(dialog, ui, info_html: str):
    ui.ack_btn.clicked.connect(dialog.close)
    ui.action_info.setHtml(info_html)
    width = ui.action_info.document().idealWidth()
    height = ui.action_info.document().size().height()
    dialog.resize(width + 20, height + 20)
    dialog.exec()