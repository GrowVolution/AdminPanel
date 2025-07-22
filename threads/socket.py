from . import THREADS, BaseThread
from socket_client import CLIENT
from events import EVENTS
from dispatcher import dispatch
from socketio.exceptions import ConnectionError


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
                print("Connecting socket...")
                CLIENT.connect("wss://admin.growvolution.org")
            except ConnectionError:
                print("Connection failed.")
                event = EVENTS.resolve('connection_lost')
                dispatch(lambda: event(self.window))
                self.failed = True
                return

        print("Socket connected.")
        self.success = True

    def stop_task(self):
        if CLIENT.connected:
            CLIENT.disconnect()
