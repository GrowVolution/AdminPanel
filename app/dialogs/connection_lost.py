from . import DIALOGS
from events import EVENTS
from socket_client import CLIENT
from PySide6.QtCore import QTimer
from qt_ui.connection_lost import Ui_Dialog
import time

_showing = False
_show_again = False
_counter = {'seconds': 5, 'failures': 1}


@DIALOGS.register(
    'connection_lost',
    "Verbindung verloren",
    Ui_Dialog
)
def show(dialog, ui, window):
    global _showing, _show_again
    if _showing:
        _show_again = True
        return

    button = ui.reconnect_btn
    btn_text = "Neu verbinden... ({seconds} Sekunden)"

    timer = QTimer()

    def update_btn_text():
        if _counter['seconds'] <= 0:
            button.setEnabled(True)
            button.setText("Neu verbinden...")
            timer.stop()
        else:
            button.setText(btn_text.format(seconds=_counter['seconds']))

    def countdown():
        _counter['seconds'] -= 1
        update_btn_text()

    def try_reconnect():
        button.setEnabled(False)
        start = EVENTS.resolve('on_start')
        start(window, True)

        QTimer.singleShot(2500, post_reconnect_check)
        timer.stop()

    def post_reconnect_check():
        global _showing, _show_again
        _showing = False

        if CLIENT.connected:
            _counter['failures'] = 1
        else:
            _counter['failures'] += 1

        _counter['seconds'] = 5 * _counter['failures']

        if _show_again:
            _show_again = False
            QTimer.singleShot(100, dialog.close)
            show(window)
        elif not CLIENT.connected:
            QTimer.singleShot(500, post_reconnect_check)
        else:
            dialog.close()

    button.clicked.connect(try_reconnect)

    update_btn_text()
    button.setEnabled(False)
    timer.timeout.connect(countdown)
    timer.start(1000)

    _showing = True
    window.hide()
    dialog.exec()
