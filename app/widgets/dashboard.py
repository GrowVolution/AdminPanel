from . import WIDGETS, BaseWidget
from threads import THREADS
from qt_ui.dashboard import Ui_Form


@WIDGETS.register('dashboard')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)

        self.loaded = False
        thread = THREADS.resolve('server_status')
        self.status_updater = thread(self, window)
        self.status_updater.start()
