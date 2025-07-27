from . import WIDGETS, BaseWidget
from threads import THREADS
from events import EVENTS
from qt_ui.sandbox import Ui_Form


@WIDGETS.register('sandbox')
class Sandbox(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.running = False
        self.window = window

        thread = THREADS.resolve('sandbox_status')
        self.status_updater = thread(self)
        self.status_updater.start()

        def control_sandbox():
            if self.running:
                self._stop()
                return
            self._start()

        self.ui.sandbox_control.clicked.connect(control_sandbox)
        self.ui.env_group.currentIndexChanged.connect(self.index_changed)
        self.selected_group = None

    def index_changed(self, index):
        self.selected_group = self.ui.env_group.itemText(index)

    def _start(self):
        note = self.ui.dev_note.text().strip()
        if not note:
            self.window.show_status("Du musst für die anderen eine Notiz hinterlassen, "
                                    "woran du arbeitest.", 'error')
            return

        container_key = self.ui.public_key.toPlainText().strip()
        if not container_key:
            self.window.show_status("Du musst einen öffentlichen SSH Schlüssel angeben, "
                                    "um die Session zu starten.", 'error')
            return

        if not self.selected_group:
            self.window.show_status("Um die Session zu starten, musst du eine "
                                    "Entwicklungsumgebung auswählen.", 'error')
            return

        start = EVENTS.resolve('start_sandbox')
        success = start(note, container_key, self.selected_group, self.window)
        if success:
            self.status_updater.force_update = True

    def _stop(self):
        stop = EVENTS.resolve('stop_sandbox')
        success = stop(self.window)
        if success:
            self.status_updater.force_update = True
