from . import THREADS
from .bases.status import StatusThread, status_template

_notes_template = """
    <html>
        <head>
            <style>
                .bold {{ font-weight: bold; }}
            </style>
        </head>
        <body>
            <p>
                {notes}
            </p>
        </body>
    </html>
"""

_note_template = "<span class='bold'>{name}</span> {note}<br>"
_btn_template = "Container {cmd}"


@THREADS.register('sandbox_status')
class Sandbox(StatusThread):
    def __init__(self, sandbox):
        super().__init__(sandbox, 'sandbox_status', 300)

    def update_ui(self, response):
        ui = self.widget.ui

        status = response.get('container_status', False)
        active = response.get('active_containers', 0)
        notes = response.get('notes', {})
        dev_note = response.get('dev_note', '')
        container_key = response.get('pub_key', '')
        groups = response.get('available_groups', [])

        ui.container_status.setText(status_template.format(
            color='green' if status else 'red',
            status='yep' if status else 'nope'
        ))
        ui.containers_active.setText(str(active))

        notes = ''.join(_note_template.format(name=k, note=v) for k, v in notes.items())
        ui.notes.setHtml(_notes_template.format(
            notes=notes if notes else '--- Keine weiteren Sessions ---',
        ))

        ui.dev_note.setText(dev_note)
        ui.public_key.setPlainText(container_key)
        ui.dev_note.setEnabled(not status)
        ui.public_key.setEnabled(not status)

        ui.sandbox_control.setText(_btn_template.format(
            cmd='ausschalten' if status else 'starten',
        ))

        ui.env_group.blockSignals(True)
        ui.env_group.clear()
        for group in groups:
            ui.env_group.addItem(group)

        if not groups:
            self.widget.window.show_status("Es sind keine Entwicklungsumgebungen verfügbar!", 'warning')
            self.widget.selected_group = None
        else:
            self.widget.index_changed(0)

        self.widget.running = status
