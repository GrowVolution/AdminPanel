from . import THREADS, BaseThread
from events import EVENTS
from utils.api import call
from dispatcher import dispatch
import time

_status_template = "<span style='color:{color}'>{status}</span>"

_server_status_template = """
    <html>
        <head>
            <style>
                .bold {{ font-weight: bold; }}
            </style>
        </head>
        <body>
            <p>
                CPU Auslastung: <span class="bold">{cpu}</span><br/>
                Arbeitsspeicher: <span class="bold">{ram}</span><br/>
                Festplatte: <span class="bold">{disk}</span>
            </p>
        </body>
    </html>
"""

_log_template = """
    <html>
        <head />
        <body>
            <p>{log}</p>
        </body>
    </html>
"""


@THREADS.register('server_status')
class Thread(BaseThread):
    def __init__(self, dashboard, window):
        super().__init__()
        self.dashboard = dashboard
        self.window = window
        self.fetch_logs = True
        self.log_fetch_counter = 360

    def _update_ui(self, response):
        global _control_fn
        ui = self.dashboard.ui

        site_online = response.get('site_online', False)
        worker_running = response.get('worker_running', False)

        cpu = response.get('cpu_percent', 0.)
        memory_p = response.get('memory_percent', 0.)
        memory_u = response.get('memory_used', 0.)
        memory_t = response.get('memory_total', 0.)
        disk_p = response.get('disk_percent', 0.)
        disk_u = response.get('disk_used', 0.)
        disk_t = response.get('disk_total', 0.)

        api_log = response.get('api_log', [])
        site_log = response.get('site_log', [])
        worker_log = response.get('worker_log', [])

        admins = response.get('admins', 0)

        site_status_color = 'green' if site_online else 'red'
        site_status_text = 'online' if site_online else 'offline'
        ui.site_status.setText(_status_template.format(
            color=site_status_color, status=site_status_text
        ))

        worker_status_color = 'green' if worker_running else 'red'
        worker_status_text = 'läuft' if worker_running else 'aus'
        ui.worker_status.setText(_status_template.format(
            color=worker_status_color, status=worker_status_text
        ))

        ui.server_status.setText(_server_status_template.format(
            cpu=f"{cpu} %", ram=f"{memory_u} GB / {memory_t} GB ({memory_p} %)",
            disk=f"{disk_u} GB / {disk_t} GB ({disk_p} %)"
        ))

        if self.fetch_logs:
            ui.api_log.setHtml(_log_template.format(log='<br>'.join(api_log)))
            ui.site_log.setHtml(_log_template.format(log='<br>'.join(site_log)))
            ui.worker_log.setHtml(_log_template.format(log='<br>'.join(worker_log)))
            self.fetch_logs = False
        else:
            self.log_fetch_counter -= 1
            if self.log_fetch_counter <= 0:
                self.fetch_logs = True
                self.log_fetch_counter = 360

        ui.admins.setText(f"{admins}")

        if not self.dashboard.loaded:
            on_loaded = EVENTS.resolve('dashboard_loaded')
            on_loaded(self.window, self.dashboard)
            self.dashboard.loaded = True

    def loop(self):
        try:
            response = call('server_status', { 'type': 'default' },
                            { 'logs': self.fetch_logs })

            def update():
                try:
                    self._update_ui(response)
                except RuntimeError:
                    self.stop()

            dispatch(update)
            time.sleep(0.5)

        except ConnectionError:
            time.sleep(1)

        except ValueError:
            self.stop()
