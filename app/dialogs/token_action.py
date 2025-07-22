from . import DIALOGS
from qt_ui.token_action_info import Ui_Dialog


@DIALOGS.register(
    'token_action',
    "Token Verwaltung",
    Ui_Dialog
)
def show(dialog, ui, info_html: str):
    ui.ack_btn.clicked.connect(dialog.close)
    ui.action_info.setText(info_html)
    dialog.exec()