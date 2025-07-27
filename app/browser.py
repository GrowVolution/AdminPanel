from qt_ui.debug_browser import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWebEngineCore import QWebEngineUrlRequestInterceptor, QWebEngineProfile, QWebEnginePage
from PySide6.QtCore import QUrl
from urllib.parse import urlparse

_url_template = "https://{subdomain}growvolution.org{path}"


class BackendInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        parsed = urlparse(url)
        backend = self.window.ui.backend.text().strip()

        if parsed.netloc.endswith("growvolution.org") and not parsed.path.startswith(f"/{backend}"):
            info.block(True)
            path = parsed.path.lstrip("/").removeprefix(backend)
            self.window.ui.path.setText(f"/{path.strip('/')}")
            self.window.load_url()


class CustomPage(QWebEnginePage):
    def __init__(self, window, profile):
        super().__init__(profile)
        self.window = window

    def acceptNavigationRequest(self, url, nav_type, is_main_frame):
        url_str = url.toString()
        parsed = urlparse(url_str)
        backend = self.window.ui.backend.text().strip()

        if parsed.netloc.endswith("growvolution.org") and not parsed.path.startswith(f"/{backend}"):
            path = parsed.path.lstrip("/").removeprefix(backend)
            self.window.ui.path.setText(f"/{path.strip('/')}")
            self.window.load_url()
            return False

        return super().acceptNavigationRequest(url, nav_type, is_main_frame)


class BrowserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        from . import get_favicon
        self.setWindowTitle("Debug Browser")
        self.setWindowIcon(get_favicon())

        profile = QWebEngineProfile.defaultProfile()
        profile.setUrlRequestInterceptor(BackendInterceptor(self))
        self.page = CustomPage(self, profile)
        self.ui.browser.setPage(self.page)

        bar = self.menuBar()
        file_menu = bar.addMenu("Datei")
        reload_action = file_menu.addAction("Neu laden")
        reload_action.setShortcut("F5")
        reload_action.triggered.connect(self.load_url)
        quit_action = file_menu.addAction("Beenden")
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(self.close)

        self.ui.browser.loadFinished.connect(self._finished)

    def load_url(self):
        subdomain = self.ui.subdomain.text().strip()
        subdomain = f"{subdomain}." if subdomain else ""
        backend = self.ui.backend.text().strip()
        path = self.ui.path.text().strip().removeprefix("/")
        path = f"/{backend}/{path}".rstrip("/")

        url = _url_template.format(subdomain=subdomain, path=path)
        self.ui.browser.load(QUrl(url))

    def _finished(self):
        url = self.ui.browser.url().toString()
        parsed = urlparse(url)

        if not parsed.netloc.endswith("growvolution.org"):
            self.ui.subdomain.clear()
            self.ui.path.clear()
            return

        domain_parts = parsed.netloc.split(".")
        if len(domain_parts) > 2:
            subdomain = domain_parts[0]
            if subdomain != "growvolution" and self.ui.subdomain.text().strip() != subdomain:
                self.ui.subdomain.setText(subdomain)

        self.ui.path.setText(parsed.path)
