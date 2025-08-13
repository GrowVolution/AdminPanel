from .browser import BrowserWindow
from events import EVENTS
from qt_ui.mainwindow import Ui_MainWindow
from debugger import log

from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QIcon
from pathlib import Path

STATIC_DIR = Path(__file__).parent / "static"
FAVICON = None


def get_favicon():
    global FAVICON
    if not FAVICON:
        log('info', "Loading favicon...", True)
        FAVICON = QIcon(str(STATIC_DIR / "favicon.png"))
    return FAVICON


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_widget = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Admin Panel")
        self.setWindowIcon(get_favicon())
        self.resize(600, 400)

        self.browser = BrowserWindow()

        self.setup_menu()
        self.menuBar().hide()

    def set_widget(self, widget: QWidget):
        self.setCentralWidget(widget)

    def show_status(self, message: str, category: str = '', timeout: int = 5000):
        match category:
            case 'success':
                template = "🟢 - {message}"
            case 'warning':
                template = "🟡 - {message}"
            case 'error':
                template = "🔴 - {message}"
            case _:
                template = "{message}"

        self.statusBar().showMessage(template.format(message=message), timeout)

    def setup_menu(self):
        def browser_trigger():
            if self.browser.isHidden():
                self.browser.show()
            else:
                self.browser.hide()

        self.ui.browser_action.setShortcut("Ctrl+B")
        self.ui.browser_action.triggered.connect(browser_trigger)
        on_lock = EVENTS.resolve('on_lock')
        self.ui.lock_action.setShortcut("Ctrl+L")
        self.ui.lock_action.triggered.connect(lambda: on_lock(self))
        self.ui.quit_action.setShortcut("Ctrl+Q")
        self.ui.quit_action.triggered.connect(self.close)

        update_widget = EVENTS.resolve('update_widget')
        self.ui.dashboard_interface.setShortcut("Ctrl+Shift+D")
        self.ui.dashboard_interface.triggered.connect(lambda: update_widget(self, 'dashboard'))
        self.ui.control_interface.triggered.connect(lambda: update_widget(self, 'site_control'))
        self.ui.console_interface.setShortcut("Ctrl+Shift+C")
        self.ui.console_interface.triggered.connect(lambda: update_widget(self, 'console'))
        self.ui.env_interface.triggered.connect(lambda: update_widget(self, 'env'))
        self.ui.env_group_interface.triggered.connect(lambda: update_widget(self, 'env_groups'))
        self.ui.dev_token_interface.triggered.connect(lambda: update_widget(self, 'dev_tokens'))
        self.ui.sandbox_interface.setShortcut("Ctrl+Shift+S")
        self.ui.sandbox_interface.triggered.connect(lambda: update_widget(self, 'sandbox'))

        self.ui.confirm_administration.triggered.connect(lambda: update_widget(self, 'queue'))
        self.ui.invite_administration.triggered.connect(lambda: update_widget(self, 'invite_admin'))
        self.ui.my_queue_administration.triggered.connect(lambda: update_widget(self, 'my_queue'))

        def log_widget(log_type: str):
            update_widget(self, 'server_logs', type=log_type)

        self.ui.api_logs_2.triggered.connect(lambda: log_widget('api'))
        self.ui.site_logs_2.triggered.connect(lambda: log_widget('site'))
        self.ui.worker_logs_2.triggered.connect(lambda: log_widget('worker'))
