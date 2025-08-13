from . import WIDGETS, BaseWidget
from qt_ui.logs import Ui_Form
from utils.api import call

_title_template = "{type} Logs"


@WIDGETS.register('server_logs')
class Widget(BaseWidget):
    def __init__(self, window, **kwargs):
        super().__init__(Ui_Form)
        self.window = window
        self.type = kwargs.get('type', None)
        if not self.type:
            raise ValueError("Missing 'type' argument!")
        else:
            self.type = self.type.lower()

        match self.type:
            case 'api':
                title = _title_template.format(type='API')
            case 'worker':
                title = _title_template.format(type='Worker')
            case _:
                title = _title_template.format(type='Site')

        self.ui.log_title.setText(title)
        self.ui.available_logs.currentIndexChanged.connect(self._load_log)
        self._load_log()

    def _load_log(self, index=None):
        log_name = self.ui.available_logs.currentText().strip()
        response = call('server_logs', {'type': 'default'},{
            'type': self.type,
            'log': log_name if log_name else None
        })
        if not response.get('success', False):
            self.window.show_status(f"Fehler beim Laden der Logs: {response.get('error', 'Unbekannter Fehler.')}.", 'error')
            return

        log = response.get('log', '')
        logs = response.get('logs', [])
        if not logs:
            self.window.show_status("Keine Logs gefunden.", 'warning')

        self.ui.available_logs.blockSignals(True)
        self.ui.available_logs.clear()

        counter = 0
        index = None
        for l in logs:
            self.ui.available_logs.addItem(l)
            if l == log_name:
                index = counter
            counter += 1

        if index is None:
            index = self.ui.available_logs.count() - 1
        self.ui.available_logs.setCurrentIndex(index)
        self.ui.available_logs.blockSignals(False)

        self.ui.log.setPlainText(log)
