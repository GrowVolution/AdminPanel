from . import WIDGETS, BaseWidget
from qt_ui.site_control import Ui_Form
from api_calls import CALLS
from data import queue_action
from utils import queued_info

_critical_box_style = """
    QGroupBox {
        border: 2px solid red;
        border-radius: 5px;
        margin-top: 20px;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 3px;
    }
"""


def _info():
    queued_info("Die Aktion")


def _deploy():
    queue_action('deploy_updates')
    _info()


def _clear():
    queue_action('clear_logs')
    _info()


@WIDGETS.register('site_control')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.window = window

        self.ui.sync_sandbox.clicked.connect(self._sync)

        self.ui.critical_actions.setStyleSheet(_critical_box_style)

        self.ui.deploy_updates.clicked.connect(_deploy)
        self.ui.clear_logs.clicked.connect(_clear)

    def _sync(self):
        sync_sandbox = CALLS.resolve('sync_sandbox')
        success = sync_sandbox(self.window)
        if success:
            self.window.show_status("Sandbox Branch ist nun aktuell.", 'success')
