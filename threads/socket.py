from . import THREADS, BaseThread
from socket_client import CLIENT
from events import EVENTS
from dispatcher import dispatch
from app.loading_screen import loading_message
from debugger import log

from socketio.exceptions import ConnectionError
import os, time


@THREADS.register('socket')
class Thread(BaseThread):
    def __init__(self, window):
        super().__init__()
        self.no_loop = True
        self.failed = False
        self.success = False
        self.window = window

    def task(self):
        if not CLIENT.connected:
            try:
                log('info', "Connecting socket...")
                loading_message("Verbinde mit dem Server...")
                backend = os.getenv("BACKEND")
                backend = '' if not backend or backend == "default" else f"{backend}/"
                CLIENT.connect(f"wss://admin.growvolution.org/{backend}")
            except ConnectionError:
                log('error',"Connection failed.")
                loading_message("Verbindung fehlgeschlagen!")
                event = EVENTS.resolve('connection_lost')
                dispatch(lambda: event(self.window))
                self.failed = True
                return
            except ValueError:
                CLIENT.disconnect()
                while CLIENT.eio.state != 'disconnected':
                    time.sleep(0.1)

                self.task()

        log('info', "Socket connected.")
        loading_message("Verbindung erfolgreich!")
        self.success = True

    def stop_task(self):
        if CLIENT.connected:
            CLIENT.disconnect()
