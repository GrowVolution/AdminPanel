from . import WIDGETS, BaseWidget
from qt_ui.console import Ui_Form
from utils import status
from utils.api import call

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


@WIDGETS.register('console')
class Widget(BaseWidget):
    def __init__(self, window):
        super().__init__(Ui_Form)
        self.window = window

        self.ui.command_line.returnPressed.connect(self.execute)
        self.clear_history()

    def clear_history(self):
        self.ui.shell.setHtml(_html_base.format(
            history=_new_line()
        ))

    def update_history(self):
        self.ui.shell.setHtml(_html_base.format(
            history=f"{''.join(_history)}{_new_line()}"
        ))

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
                _current_path = final_args[1]

            if _current_path == "/home/admin":
                _current_path = "~"

            response = call('check_path', { 'type': 'default' },
                          { 'path': _current_path })
            exists = response.get('exists', False)
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

        response = call('bash', { 'type': 'default' },
                        { 'cmd': final_args, 'path': _current_path })

        success = status(self.window, response)
        if success:
            output = response.get('output', '').strip()
            command = f'{command}<br>' if output else command
            _history.append(_output_base.format(
                path=_current_path, command=command, output=output
            ))
            self.update_history()
