from PySide6.QtCore import QObject, Signal, Slot, Qt

DISPATCHER = None


class Dispatcher(QObject):
    call = Signal(object)

    def __init__(self):
        super().__init__()
        self.call.connect(self._dispatch, Qt.ConnectionType.QueuedConnection)

    @Slot(object)
    def _dispatch(self, fn):
        fn()


def init_dispatcher():
    global DISPATCHER
    DISPATCHER = Dispatcher()


def dispatch(fn):
    DISPATCHER.call.emit(fn)
