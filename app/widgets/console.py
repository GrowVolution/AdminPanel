from . import WIDGETS, BaseWidget
from ..dialogs import DIALOGS
from qt_ui.console import Ui_Form
from api_calls import CALLS
from data import queue_action
from utils import queued_info

_html_base = """
    <html>
        <head />
        <body>
            <p>{history}</p>
        </body>
    </html>
"""

_output_base = "<b>admin@growvolution.org:{path}$</b> {command}{output}<br>"
_current_path = "~"
_history = []


def _new_line():
    return _output_base.format(
        path=_current_path, command='', output=''
    )


def _invalid_command(window):
    window.show_status("Ungültiger Befehl!", 'error')


def _sudo_operation():
    show_info = DIALOGS.resolve('info_dialog')
    show_info("<h2 style='width: 100%; text-align: center;'>Sudo aktiviert!</h2>"
              "<p>Administrative Operationen gehen <b>ausschließlich</b> in deine Warteschlange.</p>")


@WIDGETS.register('console')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.window = window

        self.ui.command_line.returnPressed.connect(self.execute)
        self.ui.sudo.toggled.connect(self.sudo_check_action)
        self.clear_history()

    def clear_history(self):
        self.ui.shell.setHtml(_html_base.format(
            history=_new_line()
        ))

    def update_history(self):
        self.ui.shell.setHtml(_html_base.format(
            history=f"{''.join(_history)}{_new_line()}"
        ))

    def sudo_check_action(self):
        if self.ui.sudo.isChecked():
            _sudo_operation()

    def execute(self):
        global _current_path
        command = self.ui.command_line.text().strip()
        self.ui.command_line.clear()

        parts = command.split(' ')
        combined_parts = []
        add = False
        final_args = []
        for part in parts:
            if part.startswith('"'):
                add = True
                part = part.strip('"')
            elif part.endswith('"'):
                add = False
                part = part.strip('"')
                combined_parts.append(part)
                final_args.append(' '.join(combined_parts))
                combined_parts = []
                continue

            if add:
                combined_parts.append(part)
                continue

            final_args.append(part)

        if final_args[0] == 'cd' and len(final_args) == 2:
            old_path = _current_path

            new_path = final_args[1]
            if new_path == '..':
                _current_path = "/home/admin" if _current_path == "~" else _current_path
                _current_path = _current_path.rsplit('/', 1)[0] if _current_path != "/" else "/"
            else:
                _current_path = new_path

            if _current_path.startswith("/home/admin"):
                _current_path = _current_path.replace("/home/admin", "~")

            if not _current_path.startswith("/"):
                _current_path = f"{old_path}/{_current_path}"

            check_path = CALLS.resolve('check_path')
            exists = check_path(_current_path)
            output = '' if exists else f"<br>Path '{_current_path}' doesn't exist!"
            _current_path = _current_path if exists else old_path
            _history.append(_output_base.format(
                path=_current_path, command=command, output=output
            ))

            self.update_history()
            return

        elif final_args[0] == 'cd':
            _invalid_command(self.window)
            return

        if final_args[0] == 'clear' and len(final_args) == 1:
            _history.clear()
            self.clear_history()
            return
        elif final_args[0] == 'clear':
            _invalid_command(self.window)
            return

        if final_args[0] == 'exit' and len(final_args) == 1:
            self.window.close()
            return
        elif final_args[0] == 'exit':
            _invalid_command(self.window)
            return

        sudo = self.ui.sudo.isChecked()
        if final_args[0] == 'sudo' and len(final_args) > 1:
            sudo = True

        if sudo:
            queue_action('bash', {
                'cmd': final_args[1:],
                'path': _current_path
            })
            queued_info("Der Command")
            return

        execute = CALLS.resolve('bash')
        success, output = execute(self.window, command, _current_path)
        if success:
            command = f'{command}<br>' if output else command
            _history.append(_output_base.format(
                path=_current_path, command=command, output=output
            ))
            self.update_history()
