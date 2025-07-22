from events import EVENTS
from dispatcher import dispatch
import socketio

CLIENT = socketio.Client()
_about_to_quit = False


def setup_handling(window):
    global CLIENT
    @CLIENT.on('disconnect')
    def on_disconnect(*args):
        if _about_to_quit:
            return

        event = EVENTS.resolve('connection_lost')
        dispatch(lambda: event(window))

        global CLIENT
        CLIENT = socketio.Client()
        setup_handling(window)


def stop_handling():
    global _about_to_quit
    _about_to_quit = True
