from . import DIALOGS
from qt_ui.actions_dialog import Ui_Dialog
from api_calls import CALLS
from utils import uneditable

from PySide6.QtWidgets import (QHeaderView, QTableWidgetItem, QWidget,
                               QHBoxLayout, QPushButton, QLabel)
from PySide6.QtCore import Qt
from functools import partial


@DIALOGS.register(
    'action_dialog',
    "Aktionen der Warteschlange",
    Ui_Dialog
)
def show_dialog(dialog, ui, queue_id):
    ui.action_table.setColumnCount(3)
    ui.action_table.setHorizontalHeaderLabels(['Aktion', 'Daten', 'Kommentare'])
    header = ui.action_table.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    ui.action_table.clearContents()
    ui.action_table.setRowCount(0)
    get_actions = CALLS.resolve('get_actions')
    actions, error = get_actions(queue_id)
    if error is not None:
        raise RuntimeWarning(error)

    row = 0
    for name, data in actions.items():
        ui.action_table.insertRow(row)
        ui.action_table.setItem(row, 0, uneditable(QTableWidgetItem(name)))

        action_data = data['data']
        if action_data:
            data_text = '\n'.join(
                [f"{k}: {v}" for k, v in action_data.items()]
            )
        else:
            data_text = "---"
        ui.action_table.setItem(row, 1, uneditable(QTableWidgetItem(data_text)))

        container = QWidget()
        hbox = QHBoxLayout(container)
        btn = QPushButton("💬")
        btn.setFixedSize(35, 35)
        btn.clicked.connect(partial(_show_comments, data['id']))
        hbox.addWidget(btn)

        hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ui.action_table.setCellWidget(row, 2, container)

        row += 1

    ui.action_table.resizeRowsToContents()

    ui.confirm.clicked.connect(dialog.close)
    dialog.exec()


def _show_comments(action_id):
    show_comments = DIALOGS.resolve('comment_dialog')
    show_comments(action_id)
