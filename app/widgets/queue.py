from . import WIDGETS, BaseWidget
from ..dialogs import DIALOGS
from qt_ui.queue import Ui_Form
from utils import uneditable
from utils.api import call
from api_calls import CALLS

from PySide6.QtWidgets import (QTableWidgetItem, QHeaderView, QPushButton, QWidget,
                               QHBoxLayout, QVBoxLayout, QLabel, QProgressBar)
from PySide6.QtCore import Qt

_progress_style = """
    QProgressBar {
        border: 1px solid #000;
        border-radius: 5px;
        text-align: center;
        background-color: red;
    }
    QProgressBar::chunk {
        background-color: green;
        width: 1px;
    }
"""

_viewed_cache = []


@WIDGETS.register('queue')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.window = window

        self.ui.pending_table.setColumnCount(3)
        self.ui.pending_table.setHorizontalHeaderLabels(['Admin', 'Aktionen', 'Stimmen'])
        header = self.ui.pending_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self._update_table()

    def _update_table(self):
        self.ui.pending_table.clearContents()
        self.ui.pending_table.setRowCount(0)
        response = call('get_queues', { 'type': 'default' })
        queues = response.get('queues', {})
        if not queues:
            self.window.show_status("Keine Aktionen zum Bestätigen gefunden.", 'warning')
            return

        row = 0
        for user, queue_info in queues.items():
            self.ui.pending_table.insertRow(row)
            self.ui.pending_table.setItem(row, 0, uneditable(QTableWidgetItem(user)))

            queue_id = queue_info['id']

            container = QWidget()
            hbox = QHBoxLayout(container)
            show_actions = QPushButton("📖")
            show_actions.setFixedSize(35, 35)
            show_actions.setProperty("queue_id", queue_id)
            show_actions.clicked.connect(self._show_actions)
            hbox.addWidget(show_actions)

            hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.ui.pending_table.setCellWidget(row, 1, container)

            container = QWidget()

            if queue_info['voted']:
                pro = queue_info['pro']
                max_ = queue_info['max']

                vbox = QVBoxLayout(container)

                label = QLabel(f"{pro} / {max_}")
                label.setStyleSheet("font-weight: bold;")
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                vbox.addWidget(label)

                progress = QProgressBar()
                progress.setStyleSheet(_progress_style)
                progress.setRange(0, 100)
                progress.setValue((pro / max_) * 100)
                vbox.addWidget(progress)

                vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

            else:
                viewed = queue_info['viewed']
                hbox = QHBoxLayout(container)

                confirm = QPushButton("✔️")
                confirm.setFixedSize(35, 35)
                confirm.setProperty("queue_id", queue_id)
                confirm.setProperty("viewed", viewed)
                confirm.clicked.connect(lambda: self._vote('confirm'))
                hbox.addWidget(confirm)

                label = QLabel("/")
                label.setStyleSheet("font-weight: bold;")
                hbox.addWidget(label)

                deny = QPushButton("❌")
                deny.setFixedSize(35, 35)
                deny.setProperty("queue_id", queue_id)
                deny.setProperty("viewed", viewed)
                deny.clicked.connect(lambda: self._vote('deny'))
                hbox.addWidget(deny)

                hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.ui.pending_table.setCellWidget(row, 2, container)

        self.ui.pending_table.resizeRowsToContents()

    def _vote(self, action):
        sender = self.sender()
        viewed = sender.property("viewed")
        queue_id = sender.property("queue_id")
        if not (viewed or queue_id in _viewed_cache):
            self.window.show_status("Bitte schau dir die auszuführenden Aktionen an.", 'warning')
            return

        vote = CALLS.resolve('vote')
        success = vote(self.window, queue_id, action)
        if success:
            idx = _viewed_cache.index(queue_id)
            _viewed_cache.pop(idx)
            self._update_table()

    def _show_actions(self):
        queue_id = self.sender().property("queue_id")
        show_actions = DIALOGS.resolve('action_dialog')
        show_actions(queue_id)
        _viewed_cache.append(queue_id)
