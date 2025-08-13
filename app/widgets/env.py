from . import WIDGETS, BaseWidget
from qt_ui.env import Ui_Form
from utils import queued_info
from utils.api import call
from events import EVENTS
from data import queue_action

from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Qt


def _get_key(ui):
    combo_box = ui.env_select
    index = combo_box.currentIndex()
    data = combo_box.itemData(index)
    return ui.new_var_name.text().strip() if data == 'add_var' else data, data == 'add_var'


@WIDGETS.register('env')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.window = window

        self.last_selected = None
        self.var_groups = []
        self.ui.env_select.currentIndexChanged.connect(self._index_changed)
        self.ui.set_value.clicked.connect(self._set)
        self.ui.del_value.clicked.connect(self._del)
        self.update_vars()

        self.queue_prod_change = False

    def update_vars(self):
        response = call('get_env', {'type': 'default'})
        env_vars = response.get('vars', {})
        if not env_vars:
            self.window.show_status("Keine Variablen gefunden.", 'warning')

        self.ui.env_select.blockSignals(True)
        self.ui.env_select.clear()
        index = None
        counter = 0
        for vid, key in env_vars.items():
            self.ui.env_select.addItem(key, userData=vid)
            if self.last_selected == key or self.last_selected == vid:
                index = counter
            counter += 1

        self.ui.env_select.addItem("Variable hinzufügen...", userData='add_var')

        if index is None:
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
            self._update_groups()
        else:
            self.ui.new_var_name.hide()
            self.ui.del_value.setEnabled(True)
            self._update_groups(data)
        self.ui.new_var_value.clear()

    def _update_groups(self, vid=None):
        response = call('get_groups', {'type': 'default'},
                        { 'vid': vid })
        groups = response.get('groups', {})
        if not groups:
            self.window.show_status("Keine Gruppen gefunden.", 'warning')

        self.ui.env_groups.blockSignals(True)
        self.ui.env_groups.clear()
        self.var_groups = []
        for group, data in groups.items():
            item = QListWidgetItem()
            item.setText(group)
            state = None
            if data['checked']:
                self.var_groups.append(group)
                state = Qt.CheckState.Checked

            item.setCheckState(state if state else Qt.CheckState.Unchecked)
            flags = item.flags()
            if data['production'] and data['checked']:
                flags &= ~Qt.ItemFlag.ItemIsUserCheckable
            else:
                flags |= Qt.ItemFlag.ItemIsUserCheckable
            item.setFlags(flags)
            item.setData(Qt.ItemDataRole.UserRole, data['production'])
            self.ui.env_groups.addItem(item)

        self.ui.env_groups.blockSignals(False)

    def _get_groups(self):
        groups = []
        for i in range(self.ui.env_groups.count()):
            item = self.ui.env_groups.item(i)
            checked = item.checkState() == Qt.CheckState.Checked
            if not checked:
                continue

            if item.data(Qt.ItemDataRole.UserRole):
                self.queue_prod_change = True
                continue

            groups.append(item.text())

        return groups

    def _set(self):
        key, add = _get_key(self.ui)
        if not key:
            self.window.show_status("Du musst einen Variablennamen angeben.", 'error')
            return

        groups = self._get_groups()
        var_value = self.ui.new_var_value.text().strip()
        if not groups or not var_value and groups == self.var_groups:
            if not groups and groups is not None:
                self.window.show_status("Die Variable muss mindestens einer Gruppe angehören.", 'error')
            elif groups and not var_value:
                self.window.show_status("Die Gruppe oder der Wert muss sich ändern.", 'error')
            return

        self.ui.set_value.setEnabled(False)
        self.last_selected = key

        if self.queue_prod_change:
            queue_action('update_prod_env', {
                'key': key,
                'value': var_value,
                'add': add
            })
            queued_info("Die Änderung")
            self.queue_prod_change = False

        set_var = EVENTS.resolve('set_var')
        success = set_var(key, var_value, groups, add, self.window)
        if success:
            self.update_vars()
        self.ui.set_value.setEnabled(True)

    def _del(self):
        self.ui.del_value.setEnabled(False)
        var_name, _ = _get_key(self.ui)
        del_var = EVENTS.resolve('del_var')
        success = del_var(var_name, self.window)
        if success:
            self.update_vars()
        self.ui.del_value.setEnabled(True)
