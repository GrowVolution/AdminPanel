from events import EVENTS
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QIcon
from qt_ui.mainwindow import Ui_MainWindow
from pathlib import Path

STATIC_DIR = Path(__file__).parent / "static"
FAVICON = None


def get_favicon():
    global FAVICON
    if not FAVICON:
        print("Loading favicon...")
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
        lock_action = file_menu.addAction("Sperren")
        quit_action = file_menu.addAction("Beenden")

        on_lock = EVENTS.resolve('on_lock')
        lock_action.triggered.connect(lambda: on_lock(self))
        quit_action.triggered.connect(self.close)

        interfaces = bar.addMenu("Interface")
        dashboard_interface = interfaces.addAction("Dashboard")
        env_interface = interfaces.addAction("Umgebungsvariablen")
        dev_token_interface = interfaces.addAction("Entwicklertokens")
        sandbox_interface = interfaces.addAction("Meine Sandbox")

        update_widget = EVENTS.resolve('update_widget')
        dashboard_interface.triggered.connect(lambda: update_widget(self, 'dashboard'))
        env_interface.triggered.connect(lambda: update_widget(self, 'env'))
        dev_token_interface.triggered.connect(lambda: update_widget(self, 'dev_tokens'))

        return bar
