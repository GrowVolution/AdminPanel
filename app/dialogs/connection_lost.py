from . import DIALOGS
from threads import THREADS
from utils import connection_check
from PySide6.QtCore import QTimer
from qt_ui.connection_lost import Ui_Dialog

_showing = False


@DIALOGS.register(
    'connection_lost',
    "Verbindung verloren",
    Ui_Dialog
)
def show(dialog, ui, window):
    global _showing
    if _showing:
        return

    counter = {'seconds': 5, 'failures': 1}

    button = ui.reconnect_btn
    btn_text = "Neu verbinden... ({seconds} Sekunden)"

    timer = QTimer()

    def update_btn_text():
        if counter['seconds'] <= 0:
            button.setEnabled(True)
            button.setText("Neu verbinden...")
            timer.stop()
        else:
            button.setText(btn_text.format(seconds=counter['seconds']))

    def countdown():
        counter['seconds'] -= 1
        update_btn_text()

    def try_reconnect():
        button.setEnabled(False)
        thread = THREADS.resolve('socket')
        socket = thread(window)
        socket.start()

        def connected():
            global _showing
            _showing = False

            window.show()
            dialog.close()

        def failed():
            counter['failures'] += 1
            counter['seconds'] = 5 * counter['failures']
            timer.start(1000)

        connection_check(socket, connected, failed)

    button.clicked.connect(try_reconnect)

    update_btn_text()
    button.setEnabled(False)
    timer.timeout.connect(countdown)
    timer.start(1000)

    _showing = True
    window.hide()
    dialog.exec()
