from . import WIDGETS, BaseWidget
from qt_ui.env import Ui_Form
from utils.api import call
from events import EVENTS


def _get_key(ui):
    combo_box = ui.env_select
    index = combo_box.currentIndex()
    data = combo_box.itemData(index)
    return ui.new_var_name.text().strip() if data == 'add_var' else data


@WIDGETS.register('env')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.window = window

        self.last_selected = None
        self.ui.env_select.currentIndexChanged.connect(self._index_changed)
        self.ui.set_value.clicked.connect(self._set)
        self.ui.del_value.clicked.connect(self._del)
        self.update_vars()

    def update_vars(self):
        response = call('get_env', {'type': 'default'})
        keys = response.get('keys', [])
        if not keys:
            self.window.show_status("Keine Variablen gefunden.", 'warning')

        self.ui.env_select.blockSignals(True)
        self.ui.env_select.clear()
        for key in keys:
            self.ui.env_select.addItem(key, userData=key)

        self.ui.env_select.addItem("Variable hinzufügen...", userData='add_var')

        if self.last_selected and self.last_selected in keys:
            index = keys.index(self.last_selected)
        else:
            index = self.ui.env_select.count() - 1

        self.ui.env_select.setCurrentIndex(index)
        self.ui.env_select.blockSignals(False)

        self._index_changed(self.ui.env_select.currentIndex())

    def _index_changed(self, index):
        data = self.ui.env_select.itemData(index)
        if data == 'add_var':
            self.ui.new_var_name.clear()
            self.ui.new_var_name.show()
            self.ui.del_value.setEnabled(False)
        else:
            self.ui.new_var_name.hide()
            self.ui.del_value.setEnabled(True)
        self.ui.new_var_value.clear()

    def _set(self):
        var_name = _get_key(self.ui)
        var_value = self.ui.new_var_value.text().strip()
        if not (var_name and var_value):
            self.window.show_status("Die Textfelder dürfen nicht leer sein.", 'error')
            return

        self.ui.set_value.setEnabled(False)
        self.last_selected = var_name

        set_var = EVENTS.resolve('set_var')
        success = set_var(var_name, var_value, self.window)
        if success:
            self.update_vars()
        self.ui.set_value.setEnabled(True)

    def _del(self):
        self.ui.del_value.setEnabled(False)
        var_name = _get_key(self.ui)
        del_var = EVENTS.resolve('del_var')
        success = del_var(var_name, self.window)
        if success:
            self.update_vars()
        self.ui.del_value.setEnabled(True)
