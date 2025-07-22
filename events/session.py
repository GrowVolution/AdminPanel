from . import EVENTS
from threads import THREADS, RUNNING
from socket_client import stop_handling
from app.widgets import WIDGETS
from app.dialogs import DIALOGS
from utils.crypt import clear_cached_key
from PySide6.QtCore import QTimer


@EVENTS.register('on_start')
def session_start(window, reconnect: bool = False):
    thread = THREADS.resolve('socket')
    socket = thread(window)
    socket.start()

    def check_connected():
        if socket.success:
            if not reconnect:
                update_widget(window, 'login')
            window.show()
            return

        elif socket.failed:
            return

        QTimer.singleShot(100, check_connected)

    check_connected()


@EVENTS.register('update_widget')
def update_widget(window, name):
    widget = WIDGETS.resolve(name)

    match name:
        case 'login':
            window.menuBar().hide()
        case 'dashboard':
            widget(window)
            return

    window.set_widget(widget(window))


@EVENTS.register('connection_lost')
def connection_lost(window):
    show_dialog = DIALOGS.resolve('connection_lost')
    show_dialog(window)


@EVENTS.register('dashboard_loaded')
def dashboard_loaded(window, dashboard):
    window.set_widget(dashboard)
    window.menuBar().show()


@EVENTS.register('on_lock')
def lock(window):
    clear_cached_key()
    update_widget(window, 'login')


@EVENTS.register('on_exit')
def exit_app():
    print("Stopping threads...")
    stop_handling()
    for thread in list(RUNNING.values()):
        thread.stop()

    print("Exiting...")
