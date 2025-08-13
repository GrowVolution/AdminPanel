from . import DIALOGS
from qt_ui.change_ownership import Ui_Dialog
from utils.api import call


@DIALOGS.register(
    'select_env_owner',
    "Umgebungseigentum übertragen",
    Ui_Dialog
)
def show(dialog, ui):
    response = call('admin_list', { 'type': 'default' })
    admins = response.get('admins', [])

    ui.admins.clear()
    for admin in admins:
        ui.admins.addItem(admin)

    new_owner = None
    def commit():
        nonlocal new_owner
        new_owner = ui.admins.currentText().strip()
        dialog.close()

    ui.commit.clicked.connect(commit)
    ui.cancel.clicked.connect(dialog.close)

    dialog.exec()
    return new_owner
