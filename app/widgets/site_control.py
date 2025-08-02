from . import WIDGETS, BaseWidget
from events import EVENTS
from qt_ui.site_control import Ui_Form


@WIDGETS.register('site_control')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)

        update = EVENTS.resolve('deploy_updates')
        self.ui.deploy_updates.clicked.connect(lambda: update(window))
