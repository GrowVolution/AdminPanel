from . import DIALOGS
from qt_ui.show_password import Ui_Dialog


@DIALOGS.register(
    'password_info',
    "Passwort Info",
    Ui_Dialog
)
def show(dialog, ui, password: str):
    ui.psw_view.setText(password)
    ui.confirm_btn.clicked.connect(dialog.close)
    dialog.exec()
