from . import DIALOGS
from qt_ui.comments_dialog import Ui_Dialog
from api_calls import CALLS
from utils import get_user

from PySide6.QtWidgets import QLabel


@DIALOGS.register(
    'comment_dialog',
    "Kommentare",
    Ui_Dialog
)
def show(dialog, ui, action_id):
    get_comments = CALLS.resolve('get_comments')
    comments, commented, error = get_comments(action_id)
    if error is not None:
        raise RuntimeWarning(error)

    for name, content in comments.items():
        ui.comments.addRow(f"<b>{name}:</b>", QLabel(content))

    if commented:
        ui.comment.hide()
        ui.add_comment.hide()
    else:
        ui.add_comment.clicked.connect(
            lambda: _add_comment(action_id, ui.comment.text().strip(), ui)
        )

    ui.confirm.clicked.connect(dialog.close)
    dialog.exec()


def _add_comment(action_id, content, ui):
    if not content:
        return

    add_comment = CALLS.resolve('add_comment')
    error = add_comment(action_id, content)
    if error is not None:
        raise RuntimeWarning(error)

    ui.comments.addRow(f"<b>{get_user()}:</b>", QLabel(content))
    ui.comment.hide()
    ui.add_comment.hide()
