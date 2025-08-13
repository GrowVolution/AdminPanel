from . import WIDGETS, BaseWidget
from ..dialogs import DIALOGS
from qt_ui.env_groups import Ui_Form
from utils import queued_info
from utils.api import call
from api_calls import CALLS
from data import queue_action

from PySide6.QtWidgets import QListWidgetItem, QLabel, QListWidget
from PySide6.QtCore import Qt


def _current_item(ui):
    for i in range(ui.my_groups.count()):
        item = ui.my_groups.item(i)
        if item.checkState() == Qt.CheckState.Checked:
            return item.data(Qt.ItemDataRole.UserRole)

    return None


def _can_continue(name, window):
    if not name:
        window.show_status("Du hast keine Gruppe ausgewählt.", 'error')
        return False
    return True


@WIDGETS.register('env_groups')
class EnvGroupsWidget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.window = window
        self.add_group = False
        self.last_selected = None
        self.protected = []

        self.ui.add_group.clicked.connect(self._add)
        self.ui.protect.clicked.connect(lambda: self._update(protected=True))
        self.ui.unprotect.clicked.connect(lambda: self._update(protected=False))

        def change_owner():
            select_new_owner = DIALOGS.resolve('select_env_owner')
            new_owner = select_new_owner()
            if not new_owner:
                return
            self._update(owner=new_owner)

        self.ui.change_ownership.clicked.connect(change_owner)
        self.ui.delete_2.clicked.connect(self._del)
        self.ui.suggest_for_production.clicked.connect(self._nominate)

        self.ui.existing_groups.setSelectionMode(QListWidget.SelectionMode.NoSelection)
        self.ui.my_groups.setSelectionMode(QListWidget.SelectionMode.NoSelection)

        self.ui.my_groups.itemChanged.connect(self._state_changed)
        self._update_groups()

    def _update_groups(self):
        response = call('get_groups', {'type': 'default'},
                        { 'all': True })
        groups = response.get('groups', {})
        if not groups:
            self.window.show_status("Keine Gruppen gefunden.", 'warning')
            return

        self.ui.existing_groups.blockSignals(True)
        self.ui.existing_groups.clear()

        for group, data in groups.items():
            item = QListWidgetItem()
            self.ui.existing_groups.addItem(item)
            if data['production']:
                label = QLabel(f"{group} <span style='color: grey;'>(Produktiv-Umgebung)</span>")
                label.setTextFormat(Qt.TextFormat.RichText)
                self.ui.existing_groups.setItemWidget(item, label)
            elif data['protected']:
                label = QLabel(f"{group} <span style='color: grey;'>(Geschützte Gruppe)</span>")
                label.setTextFormat(Qt.TextFormat.RichText)
                self.ui.existing_groups.setItemWidget(item, label)
            else:
                item.setText(group)

        self.ui.existing_groups.blockSignals(False)

        response = call('get_groups', {'type': 'default'})
        groups = response.get('groups', {})
        self.ui.my_groups.blockSignals(True)
        self.ui.my_groups.clear()
        self.protected = []

        checked_item = None
        for group, data in groups.items():
            item = QListWidgetItem()
            if data['protected']:
                label = QLabel(f"{group} <span style='color: grey;'>(Geschützt)</span>")
                label.setTextFormat(Qt.TextFormat.RichText)
                self.ui.existing_groups.setItemWidget(item, label)
                self.protected.append(group)
            else:
                item.setText(group)
            state = Qt.CheckState.Unchecked
            if self.last_selected == group:
                state = Qt.CheckState.Checked
                checked_item = item
            item.setCheckState(state)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setData(Qt.ItemDataRole.UserRole, group)
            self.ui.my_groups.addItem(item)

        item = QListWidgetItem()
        item.setText("Neue Gruppe hinzufügen...")
        state = Qt.CheckState.Unchecked
        if self.last_selected is None:
            state = Qt.CheckState.Checked
            checked_item = item
        item.setCheckState(state)
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
        item.setData(Qt.ItemDataRole.UserRole, 'add_group')
        self.ui.my_groups.addItem(item)

        self.ui.my_groups.blockSignals(False)
        self._state_changed(checked_item)

    def _state_changed(self, item):
        if item.checkState() == Qt.CheckState.Checked:
            for i in range(self.ui.my_groups.count()):
                itm = self.ui.my_groups.item(i)
                if itm.checkState() == Qt.CheckState.Checked and itm != item:
                    itm.setCheckState(Qt.CheckState.Unchecked)

            if item.data(Qt.ItemDataRole.UserRole) == 'add_group':
                self.ui.new_group.show()
                self.ui.add_group.show()
                self.add_group = True
            else:
                self.ui.new_group.hide()
                self.ui.add_group.hide()
                self.add_group = False

            if item.data(Qt.ItemDataRole.UserRole) in self.protected:
                self.ui.protect.hide()
                self.ui.unprotect.show()
            else:
                self.ui.protect.show()
                self.ui.unprotect.hide()

    def _add(self):
        if not self.add_group:
            return
        if not self.ui.new_group.text().strip():
            self.window.show_status("Du musst einen Gruppennamen angeben.", 'error')
            return

        add_group = CALLS.resolve('add_group')
        success = add_group(self.ui.new_group.text().strip(), self.window)
        if success:
            self.ui.new_group.clear()
            self._update_groups()

    def _update(self, **kwargs):
        if self.add_group:
            self.window.show_status("Du musst diese Gruppe erst hinzufügen.", 'error')
            return

        current_item = _current_item(self.ui)
        if _can_continue(current_item, self.window):
            update_group = CALLS.resolve('update_group')
            success = update_group(current_item, self.window, **kwargs)
            if success:
                self._update_groups()

    def _del(self):
        if self.add_group:
            self.window.show_status("Du kannst nur existierende Gruppen löschen.", 'error')
            return

        current_item = _current_item(self.ui)
        if _can_continue(current_item, self.window):
            del_group = CALLS.resolve('del_group')
            success = del_group(current_item, self.window)
            if success:
                self._update_groups()

    def _nominate(self):
        if self.add_group:
            self.window.show_status("Du hast diese Gruppe noch nicht erstellt.", 'error')
            return

        current_item = _current_item(self.ui)
        if _can_continue(current_item, self.window):
            queue_action('set_prod_env', {
                'name': current_item
            })
            queued_info("Der Vorschlag")
