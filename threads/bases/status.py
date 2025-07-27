from .. import BaseThread
from dispatcher import dispatch
from utils.api import call
import time

status_template = "<span style='color:{color}'>{status}</span>"


class StatusThread(BaseThread):
    def __init__(self, widget, api_command: str, interval: float):
        super().__init__()
        self.widget = widget
        self.api_command = api_command
        self.interval = interval
        self.force_update = False
        self.counter = interval

    def api_data(self):
        return {}

    def update_ui(self, response):
        raise NotImplementedError("update_ui() not implemented")

    def loop(self):
        time.sleep(.5)
        if self.counter < self.interval and not self.force_update:
            self.counter += .5
            return

        self.counter = 0
        self.force_update = False

        try:
            response = call(self.api_command,
                            { 'type': 'default' },
                            self.api_data())

            def update():
                try:
                    self.update_ui(response)
                except RuntimeError:
                    self.stop()

            dispatch(update)

        except ConnectionError:
            time.sleep(1)

        except ValueError:
            self.stop()
