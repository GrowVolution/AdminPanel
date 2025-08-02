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

        bar = self.setup_menu()
        bar.hide()

        self.browser = BrowserWindow()

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
        bar = self.menuBar()

        file_menu = bar.addMenu("Datei")
        browser_action = file_menu.addAction("Browser")
        lock_action = file_menu.addAction("Sperren")
        quit_action = file_menu.addAction("Beenden")

        def browser_trigger():
            if self.browser.isHidden():
                self.browser.show()
            else:
                self.browser.hide()

        browser_action.setShortcut("Ctrl+B")
        browser_action.triggered.connect(browser_trigger)
        on_lock = EVENTS.resolve('on_lock')
        lock_action.setShortcut("Ctrl+L")
        lock_action.triggered.connect(lambda: on_lock(self))
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(self.close)

        interfaces = bar.addMenu("Interface")
        dashboard_interface = interfaces.addAction("Dashboard")
        control_interface = interfaces.addAction("Steuerung")
        env_interface = interfaces.addAction("Umgebungsvariablen")
        dev_token_interface = interfaces.addAction("Entwicklertokens")
        sandbox_interface = interfaces.addAction("Meine Sandbox")
        console_interface = interfaces.addAction("Konsole")

        update_widget = EVENTS.resolve('update_widget')
        dashboard_interface.triggered.connect(lambda: update_widget(self, 'dashboard'))
        control_interface.triggered.connect(lambda: update_widget(self, 'site_control'))
        env_interface.triggered.connect(lambda: update_widget(self, 'env'))
        dev_token_interface.triggered.connect(lambda: update_widget(self, 'dev_tokens'))
        sandbox_interface.triggered.connect(lambda: update_widget(self, 'sandbox'))
        console_interface.triggered.connect(lambda: update_widget(self, 'console'))

        administration = bar.addMenu("Administration")
        queue = administration.addAction("Ausstehend")
        add = administration.addAction("Einladen")

        return bar
