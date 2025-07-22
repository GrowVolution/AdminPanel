from . import WIDGETS, BaseWidget
from events import EVENTS
from PySide6.QtWidgets import QCompleter
from PySide6.QtCore import Qt
from qt_ui.login import Ui_Form
from utils import key_list


def _setup_completer(keys: list[str]):
    completer = QCompleter(keys)
    completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
    completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
    completer.setFilterMode(Qt.MatchFlag.MatchContains)
    return completer


def _on_create_new(ui):
    if ui.create_new.isChecked():
        ui.psw_label.hide()
        ui.password.hide()
        ui.creation_token.show()
    else:
        ui.psw_label.show()
        ui.password.show()
        ui.creation_token.hide()


@WIDGETS.register('login')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)

        keys = key_list()
        keys_len = len(keys)

        self.ui.create_new.setChecked(False)
        _on_create_new(self.ui)
        match keys_len:
            case 0:
                self.ui.create_new.setChecked(True)
                _on_create_new(self.ui)
            case 1:
                self.ui.username.setText(keys[0])
            case _:
                completer = _setup_completer(keys)
                self.ui.username.setCompleter(completer)

        login_handler = EVENTS.resolve('on_login')
        self.ui.login_btn.clicked.connect(lambda: login_handler(window, self.ui))
        self.ui.create_new.toggled.connect(lambda: _on_create_new(self.ui))
