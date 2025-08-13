from app import get_favicon
from packaging import Package
from PySide6.QtWidgets import QDialog
from pathlib import Path


def _setup_dialog(title: str, ui):
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.setWindowIcon(get_favicon())
    dialog.setWindowTitle(title)
    return dialog, ui


def wrap(title: str, ui_cls):
    def decorator(fn):
        def wrapper(*args):
            dialog, ui = _setup_dialog(title, ui_cls())
            return fn(dialog, ui, *args)
        return wrapper
    return decorator


DIALOGS = Package(Path(__file__).parent, wrap)
