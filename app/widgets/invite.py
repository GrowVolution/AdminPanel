from . import WIDGETS, BaseWidget
from qt_ui.invite import Ui_Form
from data import queue_action
from utils import queued_info


@WIDGETS.register('invite_admin')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.window = window
        self.ui.invite.clicked.connect(self._invite)

    def _invite(self):
        name = self.ui.name.text().strip()
        email = self.ui.email.text().strip()
        info = self.ui.info.toPlainText().strip()
        if not (name and email and info):
            self.window.show_status("Die Felder dürfen nicht leer sein.", 'error')
            return

        queue_action('invite', {
            'name': name,
            'email': email,
            'info': info
        })
        queued_info("Die Einladung")

        self.ui.name.clear()
        self.ui.email.clear()
        self.ui.info.clear()
