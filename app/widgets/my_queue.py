from . import WIDGETS, BaseWidget
from qt_ui.my_queue import Ui_Form
from data import DATABASE, query, delete_model, get_actions
from api_calls import CALLS
from utils import uneditable

from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QPushButton, QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import Qt


@WIDGETS.register('my_queue')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.window = window

        self.ui.actions_table.setColumnCount(3)
        self.ui.actions_table.setHorizontalHeaderLabels(['Aktion', 'Daten', 'Löschen?'])
        header = self.ui.actions_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.ui.submit.clicked.connect(self._submit)
        self._update_table()

    def _update_table(self):
        self.ui.actions_table.clearContents()
        self.ui.actions_table.setRowCount(0)
        actions = get_actions()
        row = 0
        for action in actions:
            self.ui.actions_table.insertRow(row)
            self.ui.actions_table.setItem(row, 0, uneditable(QTableWidgetItem(action.name)))

            data = action.data
            if data:
                data_text = '\n'.join(
                    [f"{k}: {v}" for k, v in data.items()]
                )
            else:
                data_text = "---"
            self.ui.actions_table.setItem(row, 1, uneditable(QTableWidgetItem(data_text)))

            btn = QPushButton("🗑️")
            btn.setFixedSize(35, 35)
            btn.setProperty("action_id", action.id)
            btn.clicked.connect(self._del_action)

            container = QWidget()
            layout = QHBoxLayout(container)
            layout.addWidget(btn)
            layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)

            self.ui.actions_table.setCellWidget(row, 2, container)
            row += 1

        if row != 0:
            self.ui.actions_table.resizeRowsToContents()

    def _del_action(self):
        action_id = self.sender().property("action_id")
        actions = DATABASE.resolve('critical_action')
        action = query(actions, just_one=True, id=action_id)
        delete_model(action)
        self._update_table()

    def _clear(self):
        actions = get_actions()
        for action in actions:
            delete_model(action)
        self._update_table()

    def _submit(self):
        publish = CALLS.resolve('publish_queue')
        success = publish(self.window)
        if success:
            self._clear()
