from . import WIDGETS, BaseWidget
from events import EVENTS
from ..dialogs import DIALOGS
from qt_ui.dev_tokens import Ui_Form
from utils.api import call

_info_template = """
    <html>
        <head>
            <style>
                .wrapped {{ 
                    display: flex; 
                    justify-content: center; 
                    align-items: center;
                    width: fit-content;
                    height: 100%;
                    text-align: center;
                }}
                p {{
                    margin-left: 25px;
                    margin-right: 25px;
                    margin-top: 10px;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <div class="wrapped">
                <h2>Antwort des Servers</h2>
                <p>
                    {info}
                </p>
            </div>
        </body>
    </html>
"""


def _get_name(ui):
    combo_box = ui.token_select
    index = combo_box.currentIndex()
    data = combo_box.itemData(index)
    return ui.new_token_name.text().strip() if data == 'create_token' else data


@WIDGETS.register('dev_tokens')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.window = window

        self.last_selected = None
        self.ui.token_select.currentIndexChanged.connect(self._index_changed)
        self.ui.create_token.clicked.connect(self._create)
        self.ui.del_token.clicked.connect(self._del)
        self.update_vars()

        def _show_info(info):
            dialog = DIALOGS.resolve('info_dialog')
            dialog(_info_template.format(info=info))

        self.show_info = _show_info

    def update_vars(self):
        response = call('dev_tokens', { 'type': 'default' },
                        { 'cmd': '3' })
        output = response.get('output', [])
        if not output or "No tokens found" in output:
            self.window.show_status("Keine Tokens gefunden.", 'warning')

        self.ui.token_select.blockSignals(True)
        self.ui.token_select.clear()
        index = None
        for line in output:
            if not line.startswith("Name: "):
                break

            parts = line.split(",")
            name_part = parts[0].strip()
            name = name_part.split(":", 1)[1].strip()

            self.ui.token_select.addItem(line, userData=name)
            if name == self.last_selected:
                index = output.index(line)

        self.ui.token_select.addItem("Neues Token erstellen...", userData="create_token")
        if index is None:
            index = self.ui.token_select.count() - 1

        self.ui.token_select.setCurrentIndex(index)
        self.ui.token_select.blockSignals(False)
        self._index_changed(self.ui.token_select.currentIndex())

    def _index_changed(self, index):
        data = self.ui.token_select.itemData(index)
        if data == "create_token":
            self.ui.new_token_settings.show()
            self.ui.new_token_label.show()
            self.ui.new_token_name.clear()
            self.ui.valid_select.setCurrentIndex(2)
            self.ui.del_token.setEnabled(False)
            self.ui.create_token.setEnabled(True)
        else:
            self.ui.new_token_settings.hide()
            self.ui.new_token_label.hide()
            self.ui.del_token.setEnabled(True)
            self.ui.create_token.setEnabled(False)

    def _create(self):
        token_name = _get_name(self.ui)
        if not token_name:
            self.window.show_status("Der Tokenname darf nicht leer sein.", 'error')
            return

        self.ui.create_token.setEnabled(False)
        self.last_selected = token_name

        valid_opt = self.ui.valid_select.currentIndex() + 1
        create_token = EVENTS.resolve('create_token')
        success, output = create_token(token_name, valid_opt, self.window)
        if success:
            self.update_vars()

        output = '<br>'.join(output)
        additional_info = "<br><br><span style='color: orange; text-align: center;'>Du siehst dieses Token nur einmal, bewahre es gut auf!</span>"
        self.show_info(f"<b>{output}</b>{additional_info if success else ''}")
        self.ui.create_token.setEnabled(True)

    def _del(self):
        self.ui.del_token.setEnabled(False)
        token_name = _get_name(self.ui)
        del_token = EVENTS.resolve('del_token')
        success, output = del_token(token_name, self.window)
        if success:
            self.update_vars()

        output = '<br>'.join(output)
        self.show_info(f"<b>{output}</b>")
        self.ui.del_token.setEnabled(True)
